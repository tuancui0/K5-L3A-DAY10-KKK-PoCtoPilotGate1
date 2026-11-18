# Phiếu C · Sự cố và quyết định v2 · Khối 3 (phút 125–200)

**Bàn:** KKK (K5-L3A-DAY10-KKK-PoCtoPilotGate1) · **Thẻ đã bốc:** S8

Mở `incidents/Sx/card.md` của đúng số đã bốc. Các bước trên thẻ trỏ về đúng mục trong phiếu này. Mục C3 chỉ điền phần ứng với
số thẻ của bàn; các phần khác để trống.

**Mục lục**
- [C0 · Nhật ký lần chạy vòng 2 (suốt khối)](#c0)
- [C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem · phút 125–135 · bước 0 trên thẻ](#c1)
- [C2 · Câu 3.1 · Bảng soát lỗi của thẻ · phút 135–145 · bước 1–2](#c2)
- [C3 · Câu 3.1 · Phần riêng theo thẻ · phút 135–145 · bước 3](#c3)
- [C4 · Câu 3.1 · HAZOP của thẻ (≥ 3 dòng) · phút 145–150 · bước 4](#c4)
- [C5 · Câu 3.2, 3.3 · Specification và giả định môi trường · phút 145–150 · bước 4](#c5)
- [C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa · phút 150–155 · bước 4](#c6)
- [C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn · phút 155–180 · bước 5–7](#c7)
- [C8 · Câu 3.6 · Chỉ số theo dõi mới · phút 155–180 · bước 5](#c8)
- [C9 · Câu 3.7 · Fault tree SAU khi sửa · phút 180–185 · bước 8](#c9)
- [C10 · Câu 3.7 · Risk register (≥ 1 dòng) · phút 180–185 · bước 8](#c10)
- [C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5 · phút 180–185 (runbook có thể xong trong 185–200) · bước 8](#c11)
- [C12 · Quyết định Gate 1 · v2 và ba dòng bắt buộc · phút 185–200 · bước 9](#c12)

---

<a id="c0"></a>

## C0 · Nhật ký lần chạy vòng 2

Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi một dòng vào `runs/journal.jsonl`. Điền cột "Đổi MỘT thứ gì" (tham số `--note`) và "Kết luận".

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | Sx · prepared | nhận thẻ đã bốc, chưa sửa thêm (đúng cổng vòng 1 đã chốt) | | | | | |
| 2 | | Sx · after | | | | | | |
| 3 | | Sx · after | | | | | | |
| 4 | | base · after | (kiểm không regression) | | | | | |

---

<a id="c1"></a>

## C1 · Câu 3.0 · Mốc prepared và đối chiếu pre-mortem

Chạy **trước khi sửa bất cứ thứ gì**:

```bash
python3 -m lab10.grade --incident Sx
```

- Mã lần chạy grade: `__________` · base: `__________` · prepared: `__________`
- Cổng vòng 1 đỡ được ô / con số nào (so cột base với cột prepared): …
- Khối kinh doanh và vận hành còn dòng nào vượt trần: …

**Mở lại pre-mortem (Phiếu B mục B6), viết bằng bút khác màu.** Với thẻ S1, S3, S4, S5 đây là một phần của phần riêng theo thẻ.

- Sự cố trên thẻ thuộc lăng kính nào (kỹ thuật, kinh doanh, con người và vận hành, pháp lý)? …
- Có nằm trong các lý do bàn đã viết không? Nếu có: cổng vòng 1 đã đỡ được bao nhiêu (đọc cột prepared trong report)? Nếu không: vì sao cả bàn không nghĩ tới? …
- Lý do còn thiếu, thêm bây giờ:

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được bằng gì (trace / data / config nào) |
|---|---|---|
| | | |

---

<a id="c2"></a>

## C2 · Câu 3.1 · Bảng soát lỗi của thẻ

Dò ít nhất 2 ticket hỏng theo kiểu KHÁC nhau:

```bash
python3 -m lab10.trace --suite Sx --ticket <ID> --seed 11
```

Ba loại lỗi: **giới hạn của hệ thống** · **lỗi ngữ cảnh** · **lỗi chìm** (cả người dùng lẫn hệ thống đều không nhận ra; nguy hiểm nhất,
người chịu hại thường là bên thứ ba). Định nghĩa đầy đủ và ví dụ: Phiếu B mục B2.

**Tác hại của thẻ:** cho ai `____` · đo bằng gì `____` · bao nhiêu ở mốc base `____`

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 | Lỗi 3 |
|---|---|---|---|
| Vì sao người gặp coi đây là lỗi | | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | | |

Yêu cầu: ít nhất **hai lỗi có nguồn khác nhau** ở phần 2, và ít nhất một lỗi được xếp đúng là **lỗi chìm**.

---

<a id="c3"></a>

## C3 · Câu 3.1 · Phần riêng theo thẻ (chỉ điền phần của số đã bốc; làm trong khoảng 5 phút)

| Thẻ | Điền phần nào |
|---|---|
| S1 | Mục C1 (đối chiếu pre-mortem) + **C3.5** (mở lại bản đồ dữ liệu: các trường của `parcel`) |
| S2 | **C3.1** Mức kiểm soát của con người |
| S3 | Mục C1 + **C3.5** (bảng `policies`: trường nào là nguồn sự thật về "phiên bản đang hiệu lực"; dòng `delay_cause`) |
| S4 | Mục C1 + mục **Giờ cao điểm** ở Phiếu B mục B7.6 (bổ sung bằng bút khác màu nếu đã viết) |
| S5 | Mục C1 + **C3.5** + mục **C8** dùng cho một con số kinh doanh (chi phí mỗi ticket theo kho) |
| S6 | **C3.2** Hình dung của người và của hệ thống |
| S7 | **C3.3** Hiệu chỉnh lòng tin (người đặt hàng, người nhận hàng) |
| S8 | **C3.4** Hiệu chỉnh lòng tin (nhân viên duyệt, trưởng ca đứng tên) + **một dòng** "hoàn trên hạn mức" ở bảng C3.1 Bước 2 |

### C3.1 · Mức kiểm soát của con người ở từng lệnh ghi (S2; S8 chỉ một dòng)

**Cách làm:** (1) soát các dấu hiệu cho thấy con người **cần giữ nhiều quyền kiểm soát hơn**; (2) lập bảng
*ai · ở việc nào · cần mức kiểm soát nào* (thấp / vừa / cao / chưa rõ), thêm một cột: **hệ thống hiện đang cho mức nào**.
Chỗ hai cột lệch nhau chính là nơi đặt gate.

**Bước 1 · Dấu hiệu cần nhiều quyền kiểm soát hơn (đánh dấu, ghi bằng chứng từ thẻ)**

| Dấu hiệu | Có? | Bằng chứng trong thẻ / data |
|---|---|---|
| Việc này đụng tới lĩnh vực nhạy cảm: tiền, quan hệ kinh doanh với đối tác | | |
| Hệ trọng cao và cách làm bằng AI còn mới với người liên quan: họ muốn nắm quyền lúc đầu để xây lòng tin | | |
| Hệ thống còn lâu mới đạt độ chính xác mong muốn; quyền của con người là biện pháp tạm trong lúc chờ | | |
| Giới hạn hoặc lỗi của hệ thống cần con người sửa lại | | |
| Hoàn cảnh thay đổi khiến con người phải "đặt lại" hoặc "tiếp quản" (phê duyệt hết hạn, bị thu hồi; chính sách đổi) | | |

**Bước 2 · Bảng mức kiểm soát**

| Ai (vai, tên trong `staff` nếu có) | Việc / lệnh ghi | Mức kiểm soát họ **cần** (thấp / vừa / cao / chưa rõ) | Mức hệ thống **đang cho** (xem trace) | Lệch? |
|---|---|---|---|---|
| | `issue_refund` dưới hạn mức tự động | | | |
| Trần Thị Hạnh — `NV-HANH`, người duyệt đứng tên | `issue_refund` trên hạn mức tự động (S8 chỉ điền dòng này) | **Cao**: khoản hoàn phải có phê duyệt hợp lệ, đúng ticket/đơn/khách, đủ số tiền và còn hiệu lực; mã đã dùng hoặc bị thu hồi không được chấp nhận. Không đủ điều kiện thì chuyển người duyệt, không tự ghi tiền. | Thẻ S8 phản ánh việc dùng phê duyệt không hợp lệ; cần trace xác định hành vi thực tế ở mốc prepared, chưa kết luận từ mô tả thẻ về bản code hiện tại. | Theo thẻ, quyền của người đứng tên bị vượt qua khi hệ thống dùng mã ngoài phạm vi hoặc không còn hiệu lực. Chưa kết luận mức lệch còn lại ở bản prepared cho tới khi đối chiếu trace. |
| | `issue_refund` mà người trả là shop | | | |
| | nhiều khoản hoàn tự động cho một khách trong ngày | | | |
| | | | | |

→ Mỗi dòng "Lệch" là một nhánh của fault tree và một ứng viên cho gate. Ghi rõ gate **trả quyền về cho ai** (chuyển người
duyệt, chờ duyệt, trần).

**Ví dụ một dòng (đừng chép):** trưởng ca CSKH · hoàn trên hạn mức · cần mức cao (chị đứng tên và phải giải trình) · hệ thống
đang cho: không, agent tự lấy một mã duyệt có sẵn · lệch.

### C3.2 · Hình dung của người và hình dung của hệ thống (S6)

**Cách làm:** thảo luận theo nhóm rồi ghi cho **từng nhóm người dùng**: họ là ai, mục tiêu chính là gì, và hiện
nay họ làm việc này **từng bước ra sao**, đồng đều hay mỗi nơi một kiểu. Dòng cuối: **hệ thống đang mang hình dung nào**, đọc từ trace.

| | Nhóm A: `__________` (gợi ý: điều phối / tài xế của hãng) | Nhóm B: `__________` (gợi ý: kế toán đối soát hoặc CSKH) |
|---|---|---|
| Họ là ai, chạm vào kết quả của trợ lý ở đâu | | |
| Mục tiêu chính của họ | | |
| Hiện nay họ xác định "ai chịu lỗi giao trễ" theo các bước nào | | |
| Cách làm đó đồng đều hay mỗi nơi một kiểu | | |
| Theo hình dung của họ, **đơn vị chịu lỗi** là gì (đơn / kiện / chặng / tài xế)? | | |

**Hệ thống đang mang hình dung nào?** (đọc trace một ticket hỏng: `tracking.parcels` so với dòng `file_carrier_fault`)

- Với hệ thống, đơn vị chịu lỗi là: `__________`. Bằng chứng: ticket `______@seed ____`, dòng trace: `__________`.
- Chỗ hai hình dung vênh nhau: `__________`.
- Khi đầu vào không đủ để áp hình dung của con người (không biết kiện nào), hệ thống đang làm gì: `__________`; nên làm gì: `__________`.

→ Mỗi chỗ vênh là một nhánh của fault tree. Gate tốt làm cho hệ thống hành xử theo hình dung của người chịu hậu quả.

### C3.3 · Hiệu chỉnh lòng tin · người đặt hàng và người nhận hàng (S7)

**Cách làm:** đặt ba mốc trên một trục: **không tin · tin vừa đủ · tin quá mức**. Với từng nhóm người, nghĩ ra
một tình huống đẩy họ về mỗi mốc, rồi ghi hai thứ làm lòng tin lệch: **dữ liệu của hệ thống** có liên quan, và **điều người đó
biết hay không biết**. Mục tiêu là lòng tin khớp với việc hệ thống thực sự làm. Người nhận hàng không dùng hệ thống, không ký gì với LogiX.
Chỉ cần hai mốc có trong thẻ; mốc còn lại để trống nếu không có bằng chứng.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** | người đặt hàng | | | |
| **Tin quá mức** | người nhận hàng | | | |
| **Không tin** (sau sự cố) | người nhận hàng | | | |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | | | |

**Rút ra:**
- Dữ liệu nào rời hệ thống mà người liên quan **không biết** là nó rời đi: `__________` → tới `__________`.
- Để lòng tin khớp thực tế, có hai đường: **giải thích** cho người dùng dữ liệu đi đâu, hoặc **làm cho hệ thống chỉ làm đúng
  điều người ta tưởng**. Với người nhận hàng (không có kênh nào để giải thích), đường khả thi là: `__________`.
- Biện pháp đó là giảm khả năng lộ hay bảo đảm không lộ: `__________`.

### C3.4 · Hiệu chỉnh lòng tin · nhân viên duyệt và trưởng ca đứng tên (S8)

Cùng cách làm như C3.3. Mốc "tin quá mức" là trước kiểm toán, mốc "không tin" là sau kiểm toán.

| Mốc | Nhóm | Tình huống cụ thể (lấy từ thẻ / ticket) | Dữ liệu của hệ thống liên quan (trường nào, đi tới đâu) | Điều người đó biết / không biết |
|---|---|---|---|---|
| **Tin quá mức** (trước kiểm toán) | nhân viên duyệt | Giả thuyết cần kiểm chứng: nhân viên có thể coi việc khoản hoàn có mã phê duyệt và tên trưởng ca là đủ để tin khoản đó đã được duyệt đúng. Thẻ không xác nhận trực tiếp mức tin trước kiểm toán. | `approvals`: `ticket_id`, `order_id`, `customer_id`, `approver_id`, `max_vnd`, `expires_at`, `status`; mã phê duyệt được dùng cho quyết định hoàn và thể hiện trong kiểm toán. Cần trace để xác định cách sử dụng ở mốc prepared. | Có thể thấy mã/tên người duyệt nhưng chưa biết mã có đúng giao dịch, còn hiệu lực và đủ hạn mức hay không; đây là giả thuyết, chưa phải kết quả quan sát nhân viên. |
| **Tin quá mức** (trước kiểm toán) | trưởng ca đứng tên | Giả thuyết cần kiểm chứng: người cấp mã có thể kỳ vọng hệ thống chỉ dùng mã đúng phạm vi đã duyệt. Theo thẻ, chị Hạnh chỉ phát hiện qua kiểm toán rằng tên mình gắn với những khoản chị không duyệt; chưa đủ bằng chứng khẳng định chị từng tin hệ thống quá mức. | `approver_id = NV-HANH` cùng phạm vi `ticket_id`, `order_id`, `customer_id`, hạn mức `max_vnd`, hạn dùng `expires_at` và `status`; các trường này xác định quyền mà mã thực sự cấp. | Chị biết mình đã duyệt việc gì, nhưng theo thẻ không biết mã bị dùng cho các khoản ngoài ý chí phê duyệt cho tới khi xem bảng kiểm toán. |
| **Không tin** (sau kiểm toán) | nhân viên duyệt | Theo tin nhắn S8, cả ca kiểm lại bằng tay mọi quyết định, kể cả khoản 20.000đ; trợ lý không giải thích vì sao quyết định nên phải tra lại từ đầu. | `staff_behavior.recheck_auto_decisions_pct = 100`; thiếu ghi chú giải thích quyết định. Khi kiểm lại phải đối chiếu đơn, chính sách, số tiền và các trường phê duyệt liên quan. | Biết đã có khoản dùng phê duyệt sai nên không còn dựa vào kết quả tự động; thiếu căn cứ rõ ràng ở từng quyết định để phân biệt ca đáng tin với ca cần xác minh. |
| **Không tin** (sau kiểm toán) | trưởng ca đứng tên | Chị Hạnh phản ánh mình bị ghi là người duyệt khoản không duyệt: mã cho ticket khác, mã hết hạn, mã bị thu hồi hoặc chỉ duyệt tới 150.000đ trong khi khoản chi là 235.000đ. Chị yêu cầu cả ca kiểm tay vì người đứng tên phải giải trình. | Bảng `approvals`: A-2801 gắn ticket cũ và `status = used`; A-2802 hết hạn 10/11; A-2803 có `max_vnd = 150000`; A-2804 gắn đơn/ticket khác; A-2806 có `status = revoked`. Đối chiếu thêm `customer_id`, `approver_id` và giao dịch thực tế qua trace. | Biết tên mình xuất hiện trong kiểm toán nhưng không đồng ý với những khoản bị gán; cần biết mã được chọn và kiểm như thế nào, đồng thời giữ quyền cho phép khoản vượt hạn mức. |
| **Tin vừa đủ** (trạng thái muốn tới) | cả hai | Phương án: mỗi quyết định có căn cứ tính tiền, lý do và kết quả kiểm phê duyệt rõ ràng; khoản vượt hạn mức chỉ ghi khi có phê duyệt hợp lệ, nếu không thì chuyển người. Chỉ giảm kiểm tay khi đáp ứng đủ điều kiện S8. | `operations.decision_note = true`, `review_sampling_pct >= 10`, `approver_id = NV-HANH`; kiểm đầy đủ `ticket_id`, `order_id`, `customer_id`, `max_vnd`, `expires_at`, `status` của phê duyệt. Dữ liệu S8 còn yêu cầu trong ngày không có khoản hoàn dùng phê duyệt không hợp lệ. | Hiểu hệ thống dựa vào đâu, trường hợp nào phải duyệt và có quyền yêu cầu xác minh; kiểm mẫu để theo dõi thay vì mặc định mọi quyết định đều đúng. Đây là trạng thái mục tiêu, chưa xác nhận đã đạt. |

**Rút ra:**
- Dữ liệu nào của hệ thống làm lòng tin lệch: mã phê duyệt và tên người duyệt xuất hiện như bằng chứng hợp lệ trong khi mã có thể sai ticket/đơn/khách, hết hạn, đã dùng hoặc bị thu hồi, hay không đủ hạn mức. Thiếu giải thích quyết định khiến nhân viên khó tự kiểm căn cứ và sau kiểm toán phải tra lại toàn bộ.
- Để người duyệt thôi kiểm tay từng quyết định, họ cần **thấy** gì ở mỗi quyết định, cần **giữ quyền** ở đâu, và
  tỉ lệ kiểm mẫu nào hai bên chấp nhận: cần thấy dữ kiện đơn/chính sách, căn cứ tính tiền, lý do quyết định và thông tin phê duyệt đã được kiểm; người duyệt giữ quyền với khoản vượt hạn mức, mã không hợp lệ phải chuyển người. Theo `staff_behavior.trust_conditions` của S8, phương án phải có ghi chú quyết định, kiểm mẫu tối thiểu **10%**, người duyệt **NV-HANH**, đồng thời không còn khoản hoàn dùng phê duyệt không hợp lệ trong ngày. Các điều kiện này là yêu cầu của dữ liệu mô phỏng, chưa phải bằng chứng nhân viên thực tế đã đồng thuận hay kết quả after đã đạt. Ghi các con số đó vào `config/operating_gates.json` mục `operations` sau khi lưu mốc prepared; phần này mới phân tích, chưa sửa cấu hình.
- Kèm **một dòng** "`issue_refund` trên hạn mức tự động" ở bảng C3.1 Bước 2.

### C3.5 · Mở lại bản đồ dữ liệu (S1, S3, S5; viết bằng bút khác màu)

Mở lại Phiếu B mục B3. Ghi ở đây những dòng đổi so với vòng 1:

| Trường / bảng | Vòng 1 bàn đã coi là (nguồn sự thật / bản sao / chưa hỏi) | Sau khi đọc thẻ thì thấy | Ảnh hưởng tới tiền hay lỗi hãng thế nào |
|---|---|---|---|
| | | | |
| | | | |

---

<a id="c4"></a>

## C4 · Câu 3.1 · HAZOP của thẻ (ít nhất 3 dòng, viết bằng dữ kiện của thẻ)

*Mục riêng, không ghi đè HAZOP vòng 1 ở Phiếu B mục B4. Năm guideword và nghĩa của chúng: xem Phiếu B mục B4.*

Tool chọn phân tích: `issue_refund` và quy trình nhân viên kiểm lại quyết định hoàn của tool này.

**Bản nháp phân tích từ thẻ S8 và dữ liệu, chưa phải kết luận trên mốc prepared.** Các cổng hiện hữu, hành vi thực tế và nhánh chưa thấy trên trace cần kỹ sư xác minh sau khi đọc trace.

| Tham số / dòng dữ liệu | Guideword (WRONG / INVALID / INCOMPLETE / PERTURBED / INCAPABLE) | Lệch cụ thể (mã ticket, trường dữ liệu của thẻ) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| `approvals.expires_at`, `status` | INVALID | A-2802 hết hạn 10/11/2026; A-2806 có `status = revoked`. Nếu vẫn dùng mã để hoàn thì quyền cho phép không còn hiệu lực. Nguồn: `incidents/S8/world_patch.json`; chưa xác nhận hành vi prepared. | Khoản hoàn mang tên NV-HANH dù không còn được cho phép; chị Hạnh phải giải trình, kế toán phải đối soát. | Chờ đối chiếu code và trace prepared; chưa xác nhận cổng đang ngăn được các ca này. | Kiểm hạn dùng và trạng thái ngay trước `issue_refund`; mã không hợp lệ thì chuyển người, không ghi tiền. Tầng: chặn/quyền hạn. |
| `approvals.ticket_id`, `order_id`, `customer_id` | INVALID | A-2801 gắn ticket cũ và đã dùng; A-2804 gắn đơn O-2808/ticket cũ. Nếu chọn cho giao dịch hiện tại thì phê duyệt sai phạm vi. Nguồn: bảng `approvals` S8; cần trace xác nhận mã thực sự được dùng. | Người đứng tên chịu trách nhiệm cho khoản họ không duyệt; mất khả năng kiểm soát quyền chi tiền. | Chờ trace prepared xác định cổng và điểm kiểm phạm vi thực tế; không suy ra thiếu cổng chỉ từ thẻ. | Đối chiếu đủ ticket/đơn/khách, người duyệt và số tiền với phê duyệt còn hiệu lực trước khi ghi; sai hoặc thiếu thì chuyển người. Tầng: chặn/quyền hạn. |
| Giải thích quyết định hoàn | INCOMPLETE | Tin nhắn S8 phản ánh trợ lý không nói vì sao quyết định; nhân viên phải tra lại từ đầu. Chưa xác nhận ghi chú của bản prepared. | Nhân viên tăng công kiểm tay; khách chờ lâu; chi phí vận hành tăng. | Chờ kiểm cấu hình và đầu ra thực tế; chưa xác nhận ghi chú hiện có đủ căn cứ để người duyệt sử dụng. | Bật và kiểm chất lượng ghi chú: dữ kiện, căn cứ tính tiền, lý do và kết quả kiểm phê duyệt. Tầng: vận hành/phát hiện. |

**Nhánh vận hành bổ sung để kiểm chứng:** nhân viên vẫn kiểm 100% dù đã có ghi chú. Đây là rủi ro về hành vi con người, chưa gán một guideword hay coi là sự kiện đã quan sát trên bản after. Hậu quả có thể là hàng chờ và chi phí vẫn cao. Đề xuất đào tạo, kiểm mẫu có giám sát, trao đổi với người duyệt và đo hành vi thực tế; không coi bật ghi chú là đủ khôi phục lòng tin. Đây là ứng viên cho yêu cầu “nhánh chưa thấy trên trace”; chỉ xác nhận sau khi nhóm đã đọc trace.

Bắt buộc: ít nhất ba dòng, trong đó **một dòng là nhánh bàn chưa thấy trên trace** lúc viết.

---

<a id="c5"></a>

## C5 · Câu 3.2, 3.3 · Specification và giả định môi trường

### Câu 3.2 · Một specification mà nếu bị vi phạm thì gây ra tác hại trên thẻ

Kiểm được bằng code hoặc bằng một con số trong report: …

Kiểm bằng gì (hàm trong `guards.py`, dòng report nào): …

### Câu 3.3 · Một giả định về môi trường mà người thiết kế đã ngầm tin, nhưng nhiều khả năng sai ngoài thực tế

Giả định (thứ nằm NGOÀI phần mềm): Khi hệ thống cung cấp giải thích dễ hiểu, bảo đảm quyền phê duyệt và có quy trình kiểm mẫu rõ ràng, nhân viên sẽ giảm kiểm lại toàn bộ quyết định, chuyển sang kiểm mẫu theo quy trình đã thống nhất.

Vì sao có thể sai: Sau sự cố bị đứng tên duyệt sai, nhân viên có thể tiếp tục kiểm tay mọi quyết định vì sợ trách nhiệm, chưa hiểu lời giải thích hoặc chưa tin cơ chế kiểm tra. Đây là hành vi và sự chấp nhận của con người, nằm ngoài khả năng bảo đảm chỉ bằng cấu hình phần mềm. Trong pilot thật cần quan sát tỉ lệ kiểm lại, trao đổi trực tiếp với người duyệt và xác minh họ hiểu, chấp nhận quy trình; không coi việc bật ghi chú và đặt kiểm mẫu là bằng chứng đã khôi phục lòng tin.

---

<a id="c6"></a>

## C6 · Câu 3.4 · Fault tree TRƯỚC khi sửa (mã lần chạy: `__________`)

**Khung tư duy.** Đi từ **tác hại** ngược về nguyên nhân, không đi từ lỗi mình tình cờ thấy. Mỗi tầng hỏi "điều gì phải xảy
ra thì điều trên mới xảy ra", nối bằng **HOẶC** (một trong các nhánh là đủ) hoặc **VÀ** (phải đồng thời). Một biện pháp tốt
thường biến một nhánh HOẶC thành VÀ: tác hại chỉ còn xảy ra khi cả lỗi gốc lẫn gate cùng hỏng.

**Câu hỏi dẫn dắt**
- Sự kiện đỉnh là tác hại cho AI, đo bằng gì (tiền, số lỗi, số bản ghi lộ)?
- Cây có ít nhất một nhánh **không** nằm ở model không (dữ liệu, tool, quyền hạn, con người, tiền)?
- **Specification** nào của phần mềm bị vi phạm ở mỗi lá? **Giả định về môi trường** nào (thứ nằm ngoài phần mềm) đã sai?
- Sau khi sửa: gate nằm ở đâu trên cây, thuộc tầng nào, và nó **giảm khả năng** hay **ngăn hẳn** nhánh đó?

Ít nhất hai nhánh ở hai tầng khác nhau (kỹ thuật, kinh doanh, con người); mỗi lá có bằng chứng (ticket@seed, trường dữ liệu, hoặc một dòng của report).

```
[ĐỈNH] Tác hại: ______________________________ (cho ai: __________, đo bằng: __________)
 └─ HOẶC
 ├─ [1] ______________________________ tầng: đầu vào / data / hành động / quyền hạn / vận hành / kinh doanh
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 ├─ [2] ______________________________ tầng: ______
 │ └─ vì: ________________________ bằng chứng: ticket ______@seed ____
 └─ [3] ______________________________ tầng: ______
 └─ vì: ________________________ bằng chứng: ______
```

**Nhánh vận hành soạn trước từ S8 (chưa hoàn tất cây toàn nhóm):**

```text
[Tác hại cần kiểm chứng bằng report] Tăng công kiểm tay, hàng chờ và chi phí
  cho nhân viên CSKH, trưởng ca, LogiX và khách đang chờ
  └─ VÀ
     ├─ Nhân viên kiểm lại mọi quyết định
     │  └─ Người đứng tên mất lòng tin sau khi thấy phê duyệt bị dùng sai
     │     └─ Thẻ phản ánh mã sai phạm vi, hết hạn, thu hồi hoặc thiếu hạn mức
     └─ Công kiểm lại vượt nguồn lực/thời gian/ngân sách có thể đáp ứng
        └─ Thiếu giải thích khiến nhân viên phải tra lại từ đầu
```

Nguồn: tin nhắn chị Hạnh trong `incidents/S8/card.md`; `staff_behavior.recheck_auto_decisions_pct = 100` và các điều kiện lòng tin trong `incidents/S8/world_patch.json`. Quan hệ từ việc kiểm tay sang quá tải cần đối chiếu công suất, thời gian kiểm và report; không mặc định kiểm tay luôn gây ùn. Chưa ghi số tác hại hoặc run ID. Kỹ sư cần bổ sung nhánh kỹ thuật và bằng chứng trace để hoàn tất cây trước sửa.

| Lá | Specification bị vi phạm (phần mềm phải làm gì) | Giả định môi trường đã sai (thế giới ngoài phần mềm) |
|---|---|---|
| [1] | | |
| [2] | | |
| [3] | | |

**Ví dụ mẫu một nhánh (bộ nền, đừng chép):** đỉnh "hãng VNX nhận lỗi oan cho đơn O-1002" ← [1] agent dùng độ trễ 5 ngày ←
model lấy số trong ticket đè lên DB (`T-002@55`). Spec bị vi phạm: độ trễ dùng để ghi lỗi phải lấy từ tracking DB. Giả định
môi trường sai: "khách ghi đúng số ngày trễ". Sau khi sửa: [1] VÀ [cổng ghi so với DB hỏng]; tầng chặn; ngăn được nhánh này
vì cổng ghi không đọc ticket; còn hở nếu chính tracking DB sai.

---

<a id="c7"></a>

## C7 · Câu 3.5 · Bảng sửa: nguyên nhân → chỗ sửa → giảm hay ngăn

Sửa NGOÀI model, đúng chỗ cho từng nguyên nhân. Code: `lab10/guards.py` (`pre_guard`, `write_gate`). Con số và quy trình:
`config/operating_gates.json` (phạm vi, người trực, trần, ngân sách, kiểm mẫu, ghi chú giải thích, cổng pháp lý). Rồi chạy:

```bash
python3 -m lab10.eval --suite Sx --stage after --note "đổi MỘT thứ: ..."
python3 -m lab10.grade --incident Sx
```

| Nhánh fault tree | Nguyên nhân | Chỗ sửa (hàm + nhánh trong `guards.py`, hoặc khoá trong `operating_gates.json`) | Tầng (phát hiện / chặn / giới hạn thiệt hại / vận hành) | GIẢM khả năng hay NGĂN hẳn? Vì sao | Mã lần chạy sau khi sửa |
|---|---|---|---|---|---|
| [1] | | | | | |
| [2] | | | | | |
| [3] | | | | | |

---

<a id="c8"></a>

## C8 · Câu 3.6 · Chỉ số theo dõi mới (thước đo → dữ liệu → cách tính)

Thêm **ít nhất một hàm** trong `lab10/monitors.py` và đăng ký vào `MONITORS`. Chỉ số `escalation_rate` có sẵn không tính là chỉ số mới.
Thẻ S5 dùng mục này cho một con số kinh doanh: chi phí mỗi ticket theo kho (tách tiền máy, công người, tiền mất).

| | Chỉ số theo dõi mới của bàn |
|---|---|
| **Tên trong `MONITORS`** | |
| **Bước / hành vi được đo** | |
| **Thước đo** (một câu, có đơn vị) | |
| **Dữ liệu** (trường nào của trial, không có nhãn) | |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | |
| **Khung thời gian / ngưỡng báo động** | |
| **Điểm mù** (chỉ số này KHÔNG thấy gì) | |
| Giá trị trên bộ nền · trên thẻ (đọc mục `monitor` của report) | |

---

<a id="c9"></a>

## C9 · Câu 3.7 · Fault tree SAU khi sửa (mã lần chạy: `__________`)

Vẽ lại cây ở C6. Ở mỗi nhánh đã xử lý, thêm một nút `VÀ [gate … hỏng]` và ghi:

```
[ĐỈNH] ______________________________
 └─ HOẶC
 ├─ [1] ______________ VÀ [gate ______ hỏng]
 ├─ [2] ______________ VÀ [gate ______ hỏng]
 └─ [3] ______________ (còn hở?)
```

| Nhánh | Gate (hàm trong `guards.py` / khoá config / metric trong `monitors.py`) | Tầng gate (phát hiện / chặn / giới hạn thiệt hại / vận hành) | Giảm hay ngăn? Vì sao | Nhánh còn hở |
|---|---|---|---|---|
| [1] | | | | |
| [2] | | | | |
| [3] | | | | |

---

<a id="c10"></a>

## C10 · Câu 3.7 · Risk register (thêm ít nhất 1 dòng sau sự cố)

| Rủi ro | Khả năng | Tác động | Người phụ trách (PIC, một người) | Dấu hiệu (metric nào, ngưỡng nào) | Xử lý | Ảnh hưởng bước đánh giá | Nhóm chức năng (GOVERN / MAP / MEASURE / MANAGE) |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

Quy tắc: **mỗi dòng phải đổi được một quyết định.** Cột "Dấu hiệu" phải là một metric có trong `monitors.py` hoặc trong report.

---

<a id="c11"></a>

## C11 · Câu 3.7 · Cập nhật checklist 9 nhóm việc và Runbook phần 4–5

### Cập nhật checklist (bảng gốc ở Phiếu B mục B5)

Ghi các dòng đổi sau sự cố. Mỗi dòng vẫn phải có một PIC có tên.

| # nhóm | Trạng thái mới (Xong / Chưa / Không áp dụng) | Bằng chứng mới (mã lần chạy, mục phiếu, số trong report) | PIC |
|---|---|---|---|
| | | | |
| | | | |

### Runbook 4 · Sau sự cố trên thẻ (vòng 2)

**Phương án xử lý S8, chưa phải biên bản đã triển khai hoặc diễn tập.** Các thay đổi thực tế, số đo và mã lần chạy sẽ bổ sung sau khi đối chiếu code/config và report prepared/after.

| Câu hỏi | Trả lời |
|---|---|
| Tín hiệu nào ở Runbook 2 (Phiếu B mục B7.5) lẽ ra phải báo trước sự cố này? Nó đã có chưa? | Đối chiếu các tín hiệu hàng chờ, thời gian chờ và chi phí ở Runbook 2; bổ sung kiểm tra khoản hoàn dùng phê duyệt không hợp lệ, phản ánh của người đứng tên và mức kiểm lại quyết định tự động. Đây là các tín hiệu cần theo dõi cho S8; chờ kiểm code, metric và report để xác nhận tín hiệu nào đã được triển khai, có dữ liệu và thực sự phát cảnh báo. |
| Bàn thêm hoặc đổi ngưỡng nào, từ bao nhiêu thành bao nhiêu? | Phương án theo điều kiện S8: có ghi chú giải thích, kiểm mẫu tối thiểu 10%, người duyệt NV-HANH và không còn khoản hoàn dùng phê duyệt không hợp lệ trong ngày mới đủ điều kiện chuyển từ kiểm tay sang kiểm mẫu. Có phản ánh nghi phê duyệt sai thì xác minh ngay; xác nhận có sai thì tạm dừng thao tác hoàn liên quan và đối soát. Chưa ghi thay đổi thực tế “từ … sang …”; cần đối chiếu config prepared/after và report. |
| Bàn đổi gì về **người** (số người trực, ai đứng tên, ai được gọi)? | Phương án: NV-HANH giữ quyền duyệt khoản vượt hạn mức, không dùng tên/mã của chị thay cho sự cho phép hợp lệ; NV-TUNG tiếp nhận cảnh báo, điều phối và quyết định tạm dừng luồng liên quan; NV-OANH đối soát khoản đã ghi. Chưa đề xuất tăng số người trực khi chưa đo tải và chi phí; số người thực tế sẽ đối chiếu cấu hình cuối. |
| Bàn đổi gì về **phạm vi** hoặc **quy trình** (kiểm mẫu, ghi chú giải thích, trần)? | Kiểm đúng ticket/đơn/khách, người duyệt, hạn mức, hạn dùng và trạng thái phê duyệt trước khi ghi tiền; không hợp lệ thì chuyển người. Mỗi quyết định có ghi chú căn cứ và lý do. Chỉ chuyển sang kiểm mẫu khi đủ điều kiện S8; kiểm mẫu không thay quyền duyệt khoản vượt hạn mức. Phạm vi và trần tiền chỉ thay khi có bằng chứng, đánh giá chi phí và thống nhất với vai kinh doanh. |
| Nói gì với bên thứ ba bị ảnh hưởng (hãng, shop, người nhận, nhân viên duyệt), ai nói, trong bao lâu? | Phương án: NV-TUNG tiếp nhận phản ánh của chị Hạnh/nhân viên, lưu ticket, mã phê duyệt, khoản tiền và thời điểm; thông báo đã tiếp nhận và biện pháp tạm thời trong 5 phút từ lúc nhận cảnh báo. NV-OANH đối soát khoản đã ghi; NV-TUNG cập nhật kết quả xác minh, phạm vi ảnh hưởng và hướng xử lý sau khi có bằng chứng, nếu chưa xong thì cập nhật tiến độ trong 60 phút. Đây là thời hạn đề xuất, chưa đo hoặc diễn tập; không hứa đã đảo giao dịch hay sửa trách nhiệm khi chưa xác minh. |
| Dữ liệu cá nhân nào đã rời hệ thống mà không thu hồi được? Báo cho ai? | Thẻ S8 chưa cung cấp bằng chứng về dữ liệu cá nhân đã rời hệ thống; cần kiểm tra trace, payload và nhật ký trước khi kết luận. Nếu phát hiện, giữ bằng chứng, báo NV-TUNG điều phối cùng đầu mối pháp lý phù hợp và NV-OANH đối soát tác động; xác định người nhận và dữ liệu đã gửi, không mặc định có thể thu hồi. |
| Sự cố lộ ra trước qua số máy đo, phản hồi của người, hay đọc nội dung? Nguồn nào bàn chưa có? | Theo câu chuyện trên thẻ, chị Hạnh phát hiện tên mình trên bảng kiểm toán rồi phản ánh với quản lý. Chưa có bằng chứng về thứ tự phát hiện trong lần chạy của nhóm hoặc cảnh báo tự động. Cần bổ sung report prepared/after, trace sự kiện dùng phê duyệt, dữ liệu kiểm tay/hàng chờ và nhật ký cảnh báo để xác định nguồn đã có, nguồn còn thiếu. |

### Runbook 5 · Ba kịch bản "nếu … thì …" cho tuần đầu chạy thử thật

**Phương án đề xuất cho tuần đầu, chưa diễn tập; cần đối chiếu cấu hình cuối, năng lực thực tế và kết quả đánh giá trước khi áp dụng.**

1. Nếu số ticket tăng gấp **3 lần** trong một giờ so với mức bình thường đã đo thì: NV-HANH theo dõi hàng chờ và thời gian chờ. Khi chờ từ **30 phút** hoặc tồn từ **3 ca**, Hạnh báo NV-TUNG tìm người hỗ trợ có đủ thẩm quyền; không mặc định đã có người dự phòng. Khi chờ vượt **60 phút** hoặc có ít nhất **1 ca ùn**, Tùng dừng nhận thêm vào luồng tự động đang quá tải và điều phối xử lý thủ công, bảo đảm kênh thủ công có người nhận và theo dõi ca tồn. Mục tiêu hoàn tất hành động tạm dừng trong **5 phút** từ tín hiệu đỏ. Nếu không đủ nguồn lực thì thống nhất với kinh doanh phương án thu hẹp có bằng chứng. Mốc tăng gấp 3, ngưỡng hàng chờ và thời hạn phản ứng là phương án cần kiểm lại với cấu hình và report cuối; chưa phải số đo tải thực tế.
2. Nếu nhà cung cấp LLM lỗi liên tục quá **5 phút** thì: người trực ghi thời điểm bắt đầu, loại lỗi và ticket bị ảnh hưởng; không thử lại vô hạn. Trước mỗi lần xử lý lại phải kiểm nhật ký/sổ cái, không phát lại khoản hoàn đã ghi; giới hạn thử lại và ngân sách cần kỹ sư xác nhận khả năng thực hiện. NV-TUNG chuyển các ca cần xử lý sang NV-HANH hoặc người đủ quyền, thông báo tình trạng cho người nhận ca; mục tiêu hoàn tất chuyển luồng trong **5 phút** sau khi chạm ngưỡng lỗi. Khi dịch vụ phục hồi, chỉ bật lại sau kiểm tra luồng đọc/ghi, đối soát ca dở dang và xác nhận không ghi lặp. Các mốc 5 phút là đề xuất chưa diễn tập, không phải cơ chế tự động đã triển khai.
3. Nếu người duyệt báo không tin một quyết định của trợ lý thì: NV-HANH yêu cầu xác minh và lưu ticket, mã phê duyệt, căn cứ tính tiền, thời điểm và dấu vết quyết định. NV-TUNG tiếp nhận, nếu nghi có tác hại thì tạm dừng thao tác liên quan và chuyển người; mục tiêu phản ứng trong **5 phút**, chưa diễn tập. NV-OANH đối soát khoản đã ghi, kiểm phạm vi/hiệu lực phê duyệt cùng kỹ sư; không tự hoàn lại hoặc ghi lại giao dịch để sửa số. Tùng cập nhật kết quả hoặc tiến độ cho người phản ánh trong **60 phút** theo phương án Runbook 4. Chỉ khôi phục khi đã xác định nguyên nhân, có bằng chứng kiểm tra lại, Hạnh xác nhận quy trình duyệt phù hợp và Tùng xác nhận điều kiện vận hành; chuyển sang kiểm mẫu phải đủ các điều kiện S8, không chỉ dựa vào việc đã bật ghi chú.

**Danh sách bằng chứng vận hành cần nhận trước khi chốt C9–C12 và bài nộp** — hiện là danh sách chờ, không phải xác nhận đã nhận hoặc đã đạt:

- [ ] Report S8 ba mốc `base`, `prepared`, `after`, kèm mã lần chạy và journal để đối chiếu thời điểm/code/config.
- [ ] Trace các kiểu phê duyệt không hợp lệ (sai phạm vi, hết hạn, thu hồi, thiếu hạn mức) và ca phê duyệt hợp lệ đối chứng; ghi ticket@seed, sự kiện dùng mã và kết quả lệnh ghi.
- [ ] Chỉ số mới: tên đăng ký trong `MONITORS`, công thức, dữ liệu đầu vào, cách xử lý thiếu dữ liệu, ngưỡng và giá trị trên bộ nền/S8.
- [ ] Số kiểm lại quyết định, hàng chờ, thời gian chờ, ca ùn, chi phí và ROI sau thay đổi; kiểm cả phân khúc kho/hãng, đối chiếu số người trực và quy trình kiểm mẫu.
- [ ] Bằng chứng kiểm hồi quy bộ nền: các ca trước đạt không bị hỏng lại; nếu có khác biệt phải giải thích trước khi kết luận.
- [ ] Cấu hình cuối khớp phiếu/runbook và report; các thời hạn phản ứng, kênh cảnh báo, người dự phòng chưa diễn tập phải được ghi rõ.

---

<a id="c12"></a>

## C12 · Quyết định Gate 1 · v2 (phút 185–200)

Quyết định phải khớp bằng chứng và khớp tiêu chí đã ký. Chọn **Tiếp tục** khi report còn dòng vượt trần, hoặc còn ngưỡng đã ký
chưa đạt, là quyết định không đạt. **Thu hẹp**, **Cải tiến thêm**, **Dừng** có lý do và có số thì đều là quyết định đạt.
Cột v1 nằm ở Phiếu B mục B8; không sửa cột đó.

| | **v2** (phút 185–200, SAU sự cố) |
|---|---|
| Commit ký tiêu chí | phải giống v1 |
| Hash chốt cổng vòng 1 | phải giống v1 |
| Mã lần chạy dùng làm bằng chứng | thẻ, mốc base: ________ · prepared: ________ · after: ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Khối "theo kho và hãng" trong output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt kho nào / còn bao nhiêu phần trăm / mấy người trực, và ticket bị cắt đi đâu | |
| Nếu Cải tiến thêm: giả thuyết cụ thể (nhánh nào của fault tree) + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

**Chỉ ở v2**
- Quyết định đổi hay giữ so với v1? Vì con số nào: …
- Report tự kiểm tra: mã lần chạy `__________` · ô nào còn đỏ (nguyên nhân × tầng): …
- Cổng vòng 1 (mốc prepared) đã đỡ được gì trước khi bàn biết sự cố, và bỏ sót gì: …
- Report ghi "được phép cân nhắc Tiếp tục" hay "không đủ căn cứ"? Quyết định của bàn có khớp không: …
- Một thứ bộ thử hôm nay chưa đo, và nó ảnh hưởng quyết định ra sao: …

**Ba dòng bắt buộc** (chép nguyên ba câu này sang `submission/submission.json`, mục `three_lines`)
1. Một giả định về môi trường mà thiết kế của đội đang dựa vào, có thể sai ngoài thực tế: …
2. Gate của đội chỉ GIẢM khả năng hay thực sự NGĂN được tác hại? Vì sao: …
3. Vì data là mock, cần đo lại gì trong pilot thật trước Bước đánh giá 2: …
