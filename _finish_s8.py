from pathlib import Path
import json, re

p = Path('lab10/guards.py')
s = Path('lab10/guards_round1.py').read_text(encoding='utf-8')
s = s.replace('Mặc định dưới đây cho qua tất cả (= mốc base).', 'Bản vòng 2: giữ cổng vòng 1, bổ sung giới hạn cộng dồn và nhật ký phê duyệt S8.')
s = s.replace('        if action.get("order_id") != order["order_id"]:', '        if action.get("ticket_id") != ctx.ticket["ticket_id"] or action.get("order_id") != order["order_id"]:')
s = s.replace('            if not any(a.get', '            if not approval_id or ctx.tools.ledger_rows(approval_id=approval_id) or not any(a.get')
s = s.replace('                return Verdict.escalate("Thiếu phê duyệt', '                ctx.log("approval_invalid_attempt", approval_id=approval_id, amount_vnd=entitled)\n                return Verdict.escalate("Thiếu phê duyệt')
s = s.replace('        if action.get("amount_vnd") != entitled', '''        # Kiểm trên số tiền cuối cùng TRƯỚC modify: host không gọi lại gate sau modify.
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
        if action.get("amount_vnd") != entitled''')
p.write_text(s, encoding='utf-8', newline='\n')

# Giải quyết ba xung đột bằng phần HEAD đầy đủ, giữ nguyên nội dung B0-B8 đã làm.
p = Path('templates/form-b-evaluation-gates.md')
s = p.read_text(encoding='utf-8')
s = re.sub(r'^<<<<<<< HEAD\n(.*?)^=======\n.*?^>>>>>>>[^\n]*\n', r'\1', s, flags=re.M|re.S)
p.write_text(s, encoding='utf-8', newline='\n')
