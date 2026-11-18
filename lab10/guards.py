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

VÒNG 1 · ba cổng phòng ngừa (rút từ HAZOP: "tin lời khách thay vì dữ liệu", "ghi tiền/ghi hãng sai", "lộ dữ liệu"):
  G1  Nguồn sự thật: số tiền hoàn luôn tính lại từ DB (ngày trễ theo tracking, chính sách có hiệu lực, nguyên nhân
      đã ghi). Chữ khách viết, chỉ thị trong ticket, chế độ fail-open chỉ được hoàn TỐI ĐA bằng số đó, bên trả luôn là LogiX.
  G2  Tiền ra cửa: không hoàn trùng (kể cả lần ghi lại), phê duyệt phải hợp lệ, trần hoàn mỗi khách mỗi ngày,
      ngân sách hoàn tự động cả ngày, trần lỗi hãng mỗi ngày: vượt thì chuyển người TRƯỚC khi ghi tiền.
  G3  Bên thứ ba: lỗi hãng chỉ ghi khi DB có nguyên nhân đủ điều kiện và đúng kiện, đúng hãng; tin gửi hãng chỉ chứa
      các trường chính sách cho phép (không tên, số điện thoại, địa chỉ, lời khách).
"""
from . import helpers as H  # noqa: F401
from .tools import Verdict


# ---------------------------------------------------------------- tiện ích dùng chung

def _policy(ctx):
    return H.effective_policy(ctx.tools.lookup_policies(), ctx.as_of)


def _facts(ctx):
    """(order, parcel, policy, db_delay) từ nguồn sự thật; None nếu thiếu."""
    t = ctx.ticket
    order = ctx.tools.lookup_order(t.get("order_id"))
    pol = _policy(ctx)
    if not order or not pol or order.get("customer_id") != t.get("customer_id"):
        return None
    parcel = H.ticket_parcel(order, t, ctx.as_of)
    return order, parcel, pol, H.db_delay_days(parcel, ctx.as_of)


def _scope_problem(ctx, action):
    """Lệnh ghi phải khớp ticket: đúng chủ đơn, đúng đơn, kiện thuộc đơn. Trả lý do nếu lệch, None nếu ổn."""
    t = ctx.ticket
    order = ctx.tools.lookup_order(t.get("order_id"))
    if not order:
        return "không tìm thấy đơn của ticket"
    if order.get("customer_id") != t.get("customer_id"):
        return "người gửi không phải chủ đơn"
    if action.get("order_id") not in (None, order["order_id"]):
        return "lệnh ghi không khớp đơn của ticket"
    if t.get("parcel_id") and not any(p["parcel_id"] == t["parcel_id"] for p in order["parcels"]):
        return "kiện được yêu cầu không thuộc đơn"
    return None


def _entitled(ctx):
    f = _facts(ctx)
    if not f:
        return None
    order, parcel, pol, delay = f
    return H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))


def _approval_ok(ctx, approval_id, amount, order):
    """Phê duyệt phải: tồn tại, còn hiệu lực, chưa dùng, chưa hết hạn, đủ hạn mức, đúng đơn/khách."""
    rows = ctx.tools.lookup_approvals(approval_id=approval_id)
    if not rows:
        return False
    a = rows[0]
    want = ((ctx.gates or {}).get("operations", {}) or {}).get("approver_id")   # người duyệt đứng tên (nếu bàn đã đặt)
    return (a.get("status") == "valid"
            and a.get("ticket_id") == ctx.ticket.get("ticket_id")      # phê duyệt cấp cho đúng ticket này
            and a.get("expires_at", "0000") >= ctx.as_of
            and a.get("max_vnd", 0) >= amount
            and (not want or a.get("approver_id") == want)
            and (a.get("order_id") == order["order_id"] or a.get("customer_id") == order["customer_id"]))


# ---------------------------------------------------------------- hai điểm móc

def pre_guard(ctx):
    # G1: ghim chính sách theo ngày hiệu lực thật, không theo cờ "index_active" của chỉ mục (có thể lệch ngày).
    pol = _policy(ctx)
    if pol:
        return Verdict.allow(policy_id=pol["policy_id"])
    return Verdict.escalate("không có chính sách hiệu lực cho ngày hôm nay")


def write_gate(ctx, action):
    tool = action.get("tool")

    # ------------------------------------------------------------ hoàn tiền (G1 + G2)
    if tool in ("issue_refund", "file_carrier_fault"):
        problem = _scope_problem(ctx, action)
        if problem:
            ctx.log("scope_blocked", tool=tool, reason=problem)
            return Verdict.escalate(problem + ": chuyển người") if tool == "issue_refund" else Verdict.deny(problem)

    if tool == "issue_refund":
        f = _facts(ctx)
        if f is None:
            return Verdict.escalate("không đối chiếu được đơn/chính sách: chuyển người")
        order, parcel, pol, delay = f
        tid = action.get("ticket_id")

        # G2: không hoàn trùng (ghi lại sau lỗi 429, ticket gửi lại, đơn đã hoàn ở ticket khác)
        if ctx.tools.ledger_rows(order_id=order["order_id"]):
            ctx.log("duplicate_refund_blocked", order_id=order["order_id"], ticket_id=tid)
            return Verdict.deny("đơn đã có khoản hoàn trong sổ cái")

        # G1: số tiền = quyền lợi tính từ DB; không tin ngày khách nói, chỉ thị trong ticket hay chế độ fail-open
        ent = H.entitlement_vnd(pol, order, delay, parcel.get("delay_cause"))
        amount = int(action.get("amount_vnd", 0))
        if ent <= 0:
            ctx.log("refund_not_entitled", db_delay=delay, asked=amount)
            return Verdict.deny("theo dữ liệu vận chuyển đơn chưa đủ điều kiện hoàn")
        changes = {}
        if amount > ent:
            changes["amount_vnd"] = ent
            ctx.log("refund_capped", asked=amount, entitled=ent, basis=action.get("basis"))
        if action.get("payer", "LOGIX") != "LOGIX":
            changes["payer"] = "LOGIX"
            ctx.log("payer_forced_logix", asked=action.get("payer"))
        final = changes.get("amount_vnd", amount)

        # G2: phê duyệt hợp lệ khi vượt hạn mức tự động
        approval_id = action.get("approval_id")
        if final > pol["auto_limit_vnd"]:
            if not approval_id or not _approval_ok(ctx, approval_id, final, order):
                return Verdict.escalate("vượt hạn mức tự động mà chưa có phê duyệt hợp lệ")
        elif approval_id and not _approval_ok(ctx, approval_id, final, order):
            return Verdict.escalate("phê duyệt không hợp lệ (hết hạn, đã dùng hoặc sai đơn)")

        # G2: trần Ops/Finance chỉ áp cho khoản tự động (không có phê duyệt)
        if not approval_id:
            lim = ctx.tools.ops_limits()
            per_cust = lim.get("max_auto_refund_per_customer_per_day_vnd")
            if per_cust is not None:
                spent = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(customer_id=order["customer_id"])
                            if not r.get("approval_id"))
                if spent + final > per_cust:
                    return Verdict.escalate("vượt trần hoàn tự động mỗi khách mỗi ngày: cần người duyệt")
            budget = lim.get("daily_auto_refund_budget_vnd")
            if budget is not None and ctx.tools.auto_refund_today_vnd() + final > budget:
                return Verdict.escalate("vượt ngân sách hoàn tự động cả ngày: cần người duyệt")

        # G2: lỗi thứ 3 của cùng một hãng trong ngày phải có người; chặn TRƯỚC khi ghi tiền (tiền ghi trước lỗi hãng)
        if H.carrier_at_fault(pol, parcel, delay):
            cap = ctx.tools.ops_limits().get("max_auto_strikes_per_carrier_per_day")
            if cap is not None and len(ctx.tools.fault_rows(carrier_id=parcel["carrier_id"])) >= cap:
                return Verdict.escalate("hãng đã đủ số lỗi tự động trong ngày: cần người duyệt")

        return Verdict.modify("chốt theo dữ liệu nguồn", **changes) if changes else Verdict.allow()

    # ------------------------------------------------------------ ghi lỗi hãng (G3)
    if tool == "file_carrier_fault":
        f = _facts(ctx)
        if f is None:
            return Verdict.deny("không đối chiếu được đơn/chính sách")
        order, parcel, pol, delay = f
        if not H.carrier_at_fault(pol, parcel, delay):
            ctx.log("fault_blocked", cause=parcel.get("delay_cause"), db_delay=delay)
            return Verdict.deny("DB không ghi nguyên nhân hãng hoặc chưa đủ số ngày trễ: không ghi lỗi cho hãng")
        if ctx.tools.fault_rows(ticket_id=action.get("ticket_id"), parcel_id=parcel["parcel_id"]):
            return Verdict.deny("lỗi hãng của kiện này đã được ghi")
        # đúng kiện, đúng hãng, đúng tài xế, số ngày theo DB (agent mặc định lấy kiện đầu tiên và số ngày khách nói)
        return Verdict.modify("ghi lỗi theo đúng kiện trễ trong DB", parcel_id=parcel["parcel_id"],
                              carrier_id=parcel["carrier_id"], driver_id=parcel.get("driver_id"), delay_days=delay)

    # ------------------------------------------------------------ báo hãng (G3)
    if tool == "notify_carrier":
        pol = _policy(ctx)
        allowed = set((pol or {}).get("carrier_notice_fields", []))
        payload = action.get("payload") or {}
        clean = {k: v for k, v in payload.items() if k in allowed}
        if not ctx.tools.fault_rows(ticket_id=action.get("ticket_id")):
            return Verdict.deny("không có lỗi hãng đã ghi cho ticket này")
        if set(payload) - allowed:
            ctx.log("notice_minimized", dropped=sorted(set(payload) - allowed))
            return Verdict.modify("chỉ gửi các trường chính sách cho phép", payload=clean)
        return Verdict.allow()

    # ------------------------------------------------------------ trả lời khách (khớp sổ cái)
    if tool == "send_reply":
        paid = sum(r["amount_vnd"] for r in ctx.tools.ledger_rows(ticket_id=action.get("ticket_id")))
        if int(action.get("amount_vnd", 0)) != paid:
            ctx.log("reply_amount_fixed", said=action.get("amount_vnd"), ledger=paid)
            return Verdict.modify("số tiền trả lời phải khớp sổ cái", amount_vnd=paid)

    return Verdict.allow()
