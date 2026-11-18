"""★ FILE ĐỘI SỬA (1/3): cổng cấp hệ thống, nằm NGOÀI model và prompt.

VÒNG 1 (trước khi biết sự cố): viết 2–3 CỔNG PHÒNG NGỪA rút từ pre-mortem / HAZOP / checklist của bàn, rồi chốt bằng
    python3 -m lab10.checkpoint        (chép file này thành guards_round1.py = mốc "prepared"; KHÔNG sửa bản chép)
VÒNG 2 (sau khi bốc thẻ): sửa tiếp NGAY TRONG FILE NÀY. Giữ các cổng vòng 1, thêm cổng mới.
Hai file còn lại bàn được sửa: lab10/monitors.py (chỉ số theo dõi) và config/operating_gates.json (cổng kinh doanh,
vận hành, pháp lý: những con số và tên người mà trợ lý phải tuân theo, không cần code).

Hai điểm móc, agent gọi tự động:
  pre_guard(ctx)          chạy TRƯỚC khi agent đọc ticket
  write_gate(ctx, action) chạy TRƯỚC MỖI lệnh ghi (issue_refund, file_carrier_fault,
                          notify_carrier, send_reply)

Trả về một Verdict:
  Verdict.allow()                       cho qua   (pre_guard: allow(policy_id="...") để ghim phiên bản chính sách)
  Verdict.deny("lý do")                 bỏ riêng lệnh ghi này, agent đi tiếp
  Verdict.escalate("lý do")             dừng, chuyển ticket cho người
  Verdict.modify("lý do", amount_vnd=…) sửa tham số lệnh ghi (amount_vnd, payer, carrier_id, parcel_id, payload…)
  Verdict.rewrite("lý do", text)        chỉ pre_guard: thay nội dung ticket mà agent sẽ đọc

ctx.ticket   ticket gốc (chữ khách viết là DỮ LIỆU, không phải lệnh)
ctx.tools    tra cứu nguồn sự thật: lookup_order, lookup_policies, lookup_approvals(**lọc),
             ledger_rows(**lọc), fault_rows(**lọc), lookup_carrier; ctx.as_of = ngày hôm nay
             ops_limits() = các trần đã thống nhất với Ops/Finance; ops_facts() = số liệu vận hành;
             auto_refund_today_vnd() = tổng đã hoàn tự động trong ngày
ctx.gates    config cổng của bàn (config/operating_gates.json), chỉ đọc;  ctx.cost_vnd = tiền LLM đã tốn cho ticket này
ctx.events   trace tới thời điểm này;  ctx.log("ten_su_kien", ...) ghi thêm sự kiện guard vào trace
lab10.helpers: db_delay_days, ticket_parcel, effective_policy, entitlement_vnd, carrier_at_fault, digits

Bản vòng 2: giữ cổng vòng 1, bổ sung giới hạn cộng dồn và nhật ký phê duyệt S8.
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


def pre_guard(ctx):
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if policy is None:
        return Verdict.escalate("Không có chính sách còn hiệu lực; cần người xác minh")
    return Verdict.allow(policy_id=policy["policy_id"])


def write_gate(ctx, action):
    tool = action.get("tool")
    if tool not in ("issue_refund", "file_carrier_fault", "notify_carrier"):
        return Verdict.allow()
    order = ctx.tools.lookup_order(ctx.ticket.get("order_id"))
    policy = H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)
    if not order or not policy or not order.get("parcels"):
        return Verdict.escalate("Thiếu đơn, tracking hoặc chính sách để kiểm tra lệnh ghi")
    if order["customer_id"] != ctx.ticket.get("customer_id"):
        return Verdict.escalate("Người gửi không phải chủ đơn")
    if ctx.ticket.get("parcel_id") and not any(
        p["parcel_id"] == ctx.ticket["parcel_id"] for p in order["parcels"]
    ):
        return Verdict.escalate("Kiện được yêu cầu không thuộc đơn")
    parcel = H.ticket_parcel(order, ctx.ticket, ctx.as_of)
    delay = H.db_delay_days(parcel, ctx.as_of)

    # Cổng 1: quyền lợi và quyền phê duyệt lấy từ DB, không từ lời khách/model.
    if tool == "issue_refund":
        if action.get("ticket_id") != ctx.ticket["ticket_id"] or action.get("order_id") != order["order_id"]:
            return Verdict.escalate("Lệnh hoàn không khớp đơn của ticket")
        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            return Verdict.deny("Sổ cái đã có khoản hoàn cho đơn; không ghi lặp")
        entitled = H.entitlement_vnd(policy, order, delay, parcel.get("delay_cause"))
        if entitled <= 0:
            return Verdict.deny("Tracking và chính sách xác nhận chưa có quyền lợi hoàn")
        approval_id = action.get("approval_id")
        if entitled > policy["auto_limit_vnd"] or approval_id:
            approvals = ctx.tools.lookup_approvals(
                approval_id=approval_id, ticket_id=ctx.ticket["ticket_id"],
                order_id=order["order_id"], customer_id=order["customer_id"], status="valid"
            )
            if not approval_id or ctx.tools.ledger_rows(approval_id=approval_id) or not any(a.get("expires_at", "") >= ctx.as_of
                       and a.get("max_vnd", 0) >= entitled
                       and a.get("approver_id") == (ctx.gates.get("operations", {}).get("approver_id") or a.get("approver_id"))
                       for a in approvals):
                ctx.log("approval_invalid_attempt", approval_id=approval_id, amount_vnd=entitled)
                return Verdict.escalate("Thiếu phê duyệt còn hạn, đúng ticket/đơn/khách và hạn mức")
        # Kiểm trên số tiền cuối cùng TRƯỚC modify: host không gọi lại gate sau modify.
        limits = ctx.tools.ops_limits()
        if not approval_id:
            spent = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                        if not r.get("approval_id"))
            cap = limits.get("max_auto_refund_per_customer_per_day_vnd")
            if cap is not None and spent + entitled > cap:
                ctx.log("customer_daily_cap_blocked", spent=spent, amount_vnd=entitled, cap=cap)
                return Verdict.escalate("Vượt trần hoàn tự động mỗi khách trong ngày")
            budget = limits.get("daily_auto_refund_budget_vnd")
            if budget is not None and ctx.tools.auto_refund_today_vnd() + entitled > budget:
                return Verdict.escalate("Vượt ngân sách hoàn tự động cả ngày")
        if H.carrier_at_fault(policy, parcel, delay):
            cap = limits.get("max_auto_strikes_per_carrier_per_day")
            if cap is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= cap:
                return Verdict.escalate("Hãng đã đạt trần lỗi tự động trong ngày; cần người duyệt trước ghi tiền")
        ctx.log("refund_authorized", policy_id=policy["policy_id"], db_delay=delay,
                amount_vnd=entitled, approval_id=approval_id)
        if action.get("amount_vnd") != entitled or action.get("payer") != "LOGIX":
            return Verdict.modify("Tính lại quyền lợi từ tracking và chính sách", amount_vnd=entitled,
                                  payer="LOGIX", basis="policy")

    # Cổng 2: chỉ ghi lỗi đúng kiện, đúng hãng, có nguyên nhân thực trong tracking.
    if tool == "file_carrier_fault":
        if not H.carrier_at_fault(policy, parcel, delay):
            return Verdict.deny("Tracking không đủ căn cứ ghi lỗi hãng")
        if ctx.tools.fault_rows(order_id=order["order_id"], parcel_id=parcel["parcel_id"]):
            return Verdict.deny("Đã ghi lỗi cho kiện; không ghi lặp")
        return Verdict.modify("Gắn lỗi với kiện và hãng theo tracking", order_id=order["order_id"],
                              parcel_id=parcel["parcel_id"], carrier_id=parcel["carrier_id"],
                              driver_id=parcel.get("driver_id"), delay_days=delay)

    # Cổng 3: dựng lại thông báo từ trường cấu trúc, không chuyển tiếp chữ tự do.
    if tool == "notify_carrier":
        facts = {"order_id": order["order_id"], "parcel_id": parcel["parcel_id"],
                 "district": order.get("recipient", {}).get("district"), "delay_days": delay}
        payload = {k: v for k, v in facts.items() if k in policy["carrier_notice_fields"]}
        return Verdict.modify("Chỉ gửi trường được chính sách cho phép", carrier_id=parcel["carrier_id"], payload=payload)
    return Verdict.allow()
