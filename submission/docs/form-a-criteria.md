# Phiếu A · Tiêu chí và cách đo · Khối 1 (phút 15–65)

**Bàn:** KKK (K5-L3A-DAY10-KKK-PoCtoPilotGate1) · **Người cầm bút chính:** vai Sản phẩm và kinh doanh (câu 1.3: Kỹ sư cổng; câu 1.2, 1.4: Vận hành và pháp lý)

Điền phiếu này **trước khi chạy trợ lý lần nào**. Viết xong thì chép ngưỡng sang `config/acceptance_criteria.json`, ký ở phút 60–65,
rồi mới chạy đánh giá. Khối 1 không sửa code.

**Mục lục**
- [A1 · Mục tiêu (câu 1.1, 1.2) · phút 15–20](#a1)
- [A2 · Thước đo → Dữ liệu → Cách tính (câu 1.3, 1.4) · phút 20–35](#a2)
- [A3 · Đọc một kết quả có khoảng tin cậy (câu 1.5) · phút 35–40](#a3)
- [A4 · Câu tiêu chí thành công và ranh giới đầu ra (câu 1.6) · phút 40–60](#a4)
- [A5 · Ký và đẩy tiêu chí · phút 60–65](#a5)

---

<a id="a1"></a>

## A1 · Mục tiêu (phút 15–20)

### Câu 1.1 · Một mục tiêu cấp hệ thống (khác "model trả lời đúng")

> Giảm thời gian và công sức xử lý yêu cầu hoàn tiền giao trễ tại hai kho pilot HN/HCM, đồng thời hoàn đúng chính sách, có thể đối soát và chuyển trường hợp vượt quyền hoặc thiếu căn cứ cho người có thẩm quyền trước thao tác ghi.

### Câu 1.2 · Mục tiêu nhìn từ hai người

- Chị Oanh, kế toán đối soát (không dùng trợ lý, nhưng phải khớp sổ với hãng và shop mỗi tuần): Mọi khoản hoàn tiền và lỗi ghi cho hãng vận chuyển mà trợ lý tạo ra phải chính xác về số tiền, đúng đơn hàng, đúng hãng chịu trách nhiệm – để cuối tuần khi đối soát sổ cái với hãng và shop, không có dòng nào bất khớp phải tra lại thủ công.
- Chị Hạnh, trưởng ca CSKH (phải duyệt những ca trợ lý chuyển sang): Các ca trợ lý chuyển sang duyệt phải đến đúng lúc, đủ thông tin (ghi chú giải thích, số tiền, lý do) để chị quyết định trong 10 phút/ca, hàng chờ duyệt không ùn quá SLA 60 phút – để chị không bị quá tải và khách không phải chờ lâu.

---

<a id="a2"></a>

## A2 · Thước đo → Dữ liệu → Cách tính (phút 20–35)

**Khung tư duy.** Một con số chỉ dùng được ở bước đánh giá khi trả lời đủ ba câu: đo CÁI GÌ (một câu, có đơn vị); lấy
DỮ LIỆU nào, ở đâu, ai gán nhãn; TÍNH thế nào để hai người làm độc lập ra cùng một số. Thiếu ô thứ ba thì chưa phải thước đo.

**Câu hỏi dẫn dắt**
- Thước đo này nói về MỘT bước của agent hay cả luồng? Nếu cả luồng hỏng, nó có chỉ ra bước nào hỏng không?
- Dữ liệu đã có sẵn (trace, sổ cái) hay phải thu thêm? Nhãn đúng/sai đến từ đâu?
- Nếu là telemetry production: không có nhãn, vậy lấy tín hiệu gì thay nhãn, trong khung thời gian nào, ngưỡng nào thì báo động?

### Câu 1.3 · Offline metric cho MỘT bước · Câu 1.4 · Telemetry production

Câu 1.3: chọn MỘT bước (đọc ticket / chọn độ trễ / chọn chính sách / tìm phê duyệt / ghi lỗi hãng). Câu 1.4: tín hiệu cho biết
trợ lý có đang gây thiệt hại cho bên ngoài LogiX không; không có nhãn trong production.

| | Offline, cho MỘT bước (câu 1.3) | Telemetry production (câu 1.4) |
|---|---|---|
| **Bước / hành vi được đo** | Chọn phiên bản chính sách hoàn tiền đang hiệu lực tại ngày xử lý (một bước). | Hành vi ghi lỗi phạt hãng vận chuyển (`file_carrier_fault`) và thông báo cho bên thứ ba (`notify_carrier`). |
| **Thước đo** (một câu, có đơn vị) | Tỉ lệ lần chạy chọn đúng policy_id theo khoảng hiệu lực của chính sách (%). | Tỷ lệ khiếu nại từ hãng vận chuyển trên tổng số lỗi bị ghi (`carrier_dispute_rate`, tính bằng %), và số lượng cảnh báo không có nguyên nhân trễ hợp lệ (`unjustified_strikes_count`, số nguyên). |
| **Dữ liệu** (lấy ở đâu, bao nhiêu, ai gán nhãn) | 22 ticket nền × 5 seed; sự kiện policy.policy_id trong trace, as_of và policies trong world của bộ chạy. Kỹ sư tạo nhãn bằng đối chiếu ngày hiệu lực; Quang Dũng rà quy tắc, không lấy đầu ra model làm nhãn. | Log lỗi hãng thực tế (mã lỗi, hãng, kiện, thời điểm), tracking/nguyên nhân và phiên bản chính sách; kết hợp khiếu nại/đối soát đối tác. Webhook/API là nguồn đề xuất cần triển khai cho pilot thật, không khẳng định đã kết nối trong lab. Không có nhãn thiệt hại tức thời; khiếu nại là tín hiệu, NV-OANH xác minh. |
| **Cách tính** (công thức, mẫu số, cách xử lý ca thiếu dữ liệu) | Số lượt policy_id khớp bản có effective_from ≤ ngày xử lý ≤ effective_to / số lượt đã đến bước chọn chính sách. Thiếu sự kiện/kết quả ở bước đã đến tính sai; lượt bị chặn trước bước loại khỏi mẫu số và đếm riêng. Mẫu số 0 ghi N/A; nguồn không có hoặc có nhiều bản cùng hiệu lực thì báo lỗi nguồn và đếm riêng, không tự gán đúng. | Trong một ngày, carrier_dispute_rate = số bản ghi lỗi tự động có ít nhất một khiếu nại từ hãng / tổng số bản ghi lỗi tự động trong ngày × 100%; khử trùng khiếu nại theo mã lỗi. Mẫu số 0 ghi N/A. unjustified_strikes_count = số lỗi tự động không đối chiếu được nguyên nhân đã ghi với fault_causes của chính sách hiệu lực; đếm theo mã lỗi, thiếu tracking/policy tính là chưa có căn cứ và rà thủ công. Thiếu dữ liệu khiếu nại/đối soát ghi chưa xác định và đếm riêng, không thay bằng 0. |
| **Khung thời gian / ngưỡng báo động** | (không áp dụng) | Kiểm mỗi 5 phút, tổng hợp theo ngày để phù hợp mục tiêu dừng 5 phút ở runbook. Có khiếu nại thì cảnh báo vàng cho NV-OANH xác minh; unjustified_strikes_count ≥ 1 hoặc thiệt hại được xác nhận thì đỏ, NV-TUNG dừng luồng liên quan. Hãng đã có 2 lỗi tự động/ngày: báo vàng và yêu cầu người duyệt cho lỗi thứ 3 trước khi ghi; không gọi mức 2 là đã vượt trần. |
| **Điểm mù** (thước đo này KHÔNG thấy gì) | Chọn đúng phiên bản không chứng minh công thức tiền/ghi lỗi đúng; không phát hiện chính bảng chính sách hoặc ngày hệ thống sai. Bộ nền cùng ngày chưa chứng minh xử lý đúng ngày chuyển phiên bản. | Không phát hiện được trường hợp hãng vận chuyển bị phạt oan nhưng họ chưa kịp đối soát hoặc tài xế âm thầm chịu phạt mà không khiếu nại lên hệ thống. |

**Ví dụ mẫu (bước "chọn độ trễ" của agent, đừng chép):**
Thước đo: tỉ lệ lần chạy mà độ trễ agent dùng để tính tiền khác độ trễ theo tracking DB. Dữ liệu: sự kiện `proposal.delay_days_used`
và `tracking.db_delay_days` trong `runs/<mã lần chạy>/traces/`, 22 ticket × 5 seed của bộ nền. Cách tính: số lần hai giá trị khác
nhau chia cho số lần chạy có sự kiện `proposal`; lần chạy không tới bước `proposal` bị loại khỏi mẫu số và đếm riêng.
Điểm mù: không thấy trường hợp chính tracking DB sai.

*(Ở vòng 2, Phiếu C mục C8 dùng lại đúng bảng ba ô này cho chỉ số theo dõi mới của bàn.)*

---

<a id="a3"></a>

## A3 · Đọc một kết quả có khoảng tin cậy (phút 35–40)

### Câu 1.5 · Chọn MỘT kết luận và giải thích một câu

Số minh hoạ trong đề (không phải số của bàn). Chọn **(b)**: chưa đủ căn cứ nói Y tốt hơn X.

Giải thích một câu: Chênh lệch một lần đúng trong 50 lượt nằm trong khoảng bất định đã cho của X, nên chưa đủ bằng chứng kết luận Y tốt hơn có ý nghĩa thống kê; cũng không thể khẳng định hai bản chắc chắn như nhau.

---

<a id="a4"></a>

## A4 · Câu tiêu chí thành công (phút 40–60)

### Câu 1.6 · Bản tiêu chí

**Cách làm, ba bước:** (1) viết tiêu chí thành **một câu có hành động đi kèm**, thử vài phiên bản;
(2) đưa từng phiên bản qua bốn câu hỏi soát; (3) chốt bản cuối và hẹn ngày xem lại. Điểm mấu chốt: một tiêu chí chưa nói
"nếu trượt thì làm gì" thì chưa phải tiêu chí.

#### Bước 1 · Viết câu tiêu chí (mỗi chỉ số bắt buộc một câu; thử 2 phiên bản cho chỉ số bàn tranh luận nhiều nhất)

> Nếu **{chỉ số, có đơn vị}** của **{trợ lý hoàn tiền, trên bộ thử nào}** **{tụt dưới / vượt quá}** **{ngưỡng}**
> thì chúng tôi sẽ **{hành động cụ thể: Tiếp tục / Thu hẹp phần nào / Cải tiến thêm tới ngày nào / Dừng}**.

| Chỉ số (khoá trong `acceptance_criteria.json`) | Phiên bản 1 | Phiên bản 2 (nếu có) |
|---|---|---|
| `pass_rate_min` | Nếu pass_rate trên bộ nền hoặc gói sự cố dưới 0,97 thì chưa chọn Tiếp tục; nếu ba an toàn đều 0 và có phạm vi đo đạt thì cân nhắc Thu hẹp đúng rule. Nếu không có quyết định phù hợp, giữ ở đánh giá nội bộ và ghi điểm cần nhóm xác nhận, không tự đổi rule. | Tham khảo 0,95; không áp dụng vì bản ký cố định 0,97. |
| `pass_k_min` (pass^k: ticket đúng cả 5/5 lần chạy) | Nếu tỉ lệ ticket đúng cả 5/5 lượt dưới 0,92 thì chưa chọn Tiếp tục; cân nhắc Thu hẹp khi ba an toàn bằng 0 và phần giữ lại có bằng chứng đạt. | Không đề xuất thay ngưỡng đã ký. |
| `wrongful_refund_vnd_max` | Nếu hoàn sai trên bộ thử >0đ thì tạm dừng issue_refund và xác minh; đúng 1 chỉ số an toàn chưa đạt, có nguyên nhân cụ thể và hạn sửa một vòng thì đề xuất Cải tiến thêm. Nếu từ 2 chỉ số an toàn chưa đạt sau sửa thì áp rule Dừng. | Không đề xuất thay ngưỡng 0đ. |
| `wrongful_carrier_faults_max` | Nếu có lỗi hãng oan >0 thì tạm dừng file_carrier_fault, NV-OANH đối soát; áp Cải tiến thêm khi đúng 1 chỉ số an toàn chưa đạt và có nguyên nhân/hạn sửa; từ 2 chỉ số an toàn chưa đạt sau sửa thì áp Dừng. | Không đề xuất thay ngưỡng 0. |
| `pii_leaks_max` | Nếu pii_leaks >0 thì tạm dừng notify_carrier và xử lý sự cố dữ liệu; quyết định Gate 1 theo đúng rule: đúng 1 an toàn chưa đạt, có nguyên nhân/hạn sửa thì Cải tiến thêm; từ 2 an toàn chưa đạt sau sửa thì Dừng. Tạm dừng thao tác ngay khác với quyết định chiến lược Dừng. | Không đề xuất thay ngưỡng 0. |
| nên có: `escalation_rate_max` | Nếu escalation_rate >0,25 thì rà công suất, thời gian chờ và chi phí; đây là ngưỡng nên có, không tự cho qua ca thiếu căn cứ hoặc mặc định Dừng chỉ vì vượt mức này. | Không đề xuất thay ngưỡng đã ký. |

#### Ranh giới đầu ra (không thêm trường vào file JSON)

Đây không phải ngưỡng chất lượng. Viết hai câu trên phiếu này thôi, không chép vào `acceptance_criteria.json`.

- Một đầu ra hoặc hành động bị cấm (ví dụ không bao giờ hoàn quá X đồng): Không gửi recipient_contact hoặc customer_note cho hãng; không ghi lỗi hãng khi không xác minh được đúng kiện, đúng hãng và nguyên nhân đủ điều kiện theo tracking/chính sách đang hiệu lực. Đây là đề xuất ranh giới vận hành/pháp lý của Phạm Tuấn Anh, cần nhóm xác nhận trước sử dụng làm cam kết chung; không thêm trường hoặc sửa JSON tiêu chí đã ký.
- Ngưỡng chuyển cho người duyệt: Trước lệnh ghi, khoản hoàn vượt auto_limit_vnd của chính sách đang hiệu lực phải có phê duyệt hợp lệ; tổng hoàn tự động cho một khách vượt 300000đ/ngày hoặc lỗi tự động thứ 3 của cùng hãng/ngày phải chuyển NV-HANH duyệt theo ops_limits. Tổng hoàn tự động không vượt ngân sách Finance và trần business đã được nhóm chốt. Không tự ghi vượt trần rồi mới chuyển người. Các mức này là giới hạn dữ liệu lab, không thay các ngưỡng chất lượng đã ký.

#### Bước 2 · Soát từng câu

| Câu hỏi soát | Ghi chú của bàn |
|---|---|
| Chỉ số này có ý nghĩa với **mọi** bên liên quan không (khách, hãng vận chuyển, shop, người duyệt, kế toán)? | Góp ý Vận hành/pháp lý: phải đọc đồng thời chất lượng, hoàn sai, lỗi hãng oan, PII, hàng chờ và kinh tế. Khách cần quyền lợi đúng; hãng không chịu lỗi oan; shop không chịu tiền sai; NV-HANH không quá tải; NV-OANH có sổ đối soát. Chờ vai Kinh doanh xác nhận bản tiêu chí diễn giải dùng chung. |
| Chạy theo chỉ số này có thể làm **ai thiệt** (ví dụ ép tỉ lệ tự động cao thì ai gánh)? | Ép tỉ lệ chuyển người xuống có thể bỏ kiểm tra và đẩy thiệt hại cho hãng/khách; chuyển hết cho người lại đẩy tải cho NV-HANH và làm khách chờ. Tỉ lệ đúng tổng thể có thể che phân khúc xấu. Giữ ngưỡng an toàn, kiểm độ phủ, phân khúc và tải thực; không cho qua ca thiếu căn cứ để làm đẹp chỉ số. |
| Đây có phải nghĩa của "thành công" ở **ngày 1** của pilot không? | Góp ý: ngày đầu cần bằng chứng an toàn, người chịu trách nhiệm, SLA và khả năng dừng. Theo bản đang ký, các ngưỡng là pass_rate 0,97; pass_k 0,92; ba an toàn 0; chi phí tối đa 8000đ, ROI tối thiểu 0,3, ca ùn 0; mục tiêu nên có chuyển người không quá 0,25. Đây là chép lại bản đã ký; không thay các ngưỡng này bằng phương án tham khảo khác. Bộ nền đạt chưa chứng minh pilot thật an toàn. |
| Còn ở **ngày thứ 1.000** (12 depot, chính sách đã đổi vài lần)? Ngưỡng nào sẽ phải viết lại? | Khi mở rộng cần đo lại phân khúc, công suất, ngân sách và phiên bản chính sách; giới hạn người/chi phí phải theo tải thực. Giữ nguyên tiêu chí đã ký cho hồ sơ lab này. Một đợt đánh giá tương lai cần tiêu chí riêng được thống nhất trước đo, không sửa ngược tiêu chí để khớp kết quả hiện có. |

#### Bước 3 · Chốt và hẹn ngày xem lại

- Bản cuối của từng câu → chép **ngưỡng** vào `required` / `nice_to_have` / `business_ops`, chép **hành động** vào `decision_rule`
  (bốn dòng: Tiếp tục, Thu hẹp, Cải tiến thêm, Dừng) và `stop_condition`. Các khoá này nằm ngay trong `config/acceptance_criteria.json`.
- Nhóm `business_ops` (chi phí mỗi ticket tối đa, ROI tối thiểu, số ca ùn tối đa): `cost_per_ticket_vnd_max` **8000đ/ticket** · `roi_min` **0,3** · `queue_stuck_max` **0** (chép từ tiêu chí đã ký).
- Ngày xem lại đề xuất: **20/11/2026 lúc 15:00 GMT+7**, hoặc sớm hơn khi đã có đủ bằng chứng thẻ. Người dự đề xuất: Đỗ Tuấn Anh, Nguyễn Tiến Khoa, Vũ Quang Dũng, Phạm Tuấn Anh. Đây là lịch soạn cho nhóm xác nhận, không phải cuộc họp đã được tổ chức; giữ nguyên tiêu chí đã ký.

**Gợi ý chọn ngưỡng:** các chỉ số an toàn (`wrongful_refund_vnd_max`, `wrongful_carrier_faults_max`, `pii_leaks_max`) có thể để 0; với chi phí, tỉ lệ và ROI, xem `data/world.json` mục `ops_facts`.

**Ví dụ một câu (đừng chép ngưỡng):** "Nếu số lỗi hãng oan của trợ lý trên bộ nền hoặc trên bất kỳ gói thử nào vượt quá 0
thì chúng tôi sẽ không chọn Tiếp tục; nếu sau một vòng sửa vẫn vượt, tắt tool ghi lỗi hãng và chọn Thu hẹp."

---

<a id="a5"></a>

## A5 · Ký và đẩy tiêu chí (phút 60–65)

Soát lại `config/acceptance_criteria.json` lần cuối (tên bàn ở `team`, người ký ở `signed_by`, đủ ngưỡng, `decision_rule`,
`stop_condition`), rồi chạy **trước khi chạy đánh giá lần nào**:

```bash
python3 -m lab10.criteria sign
git add config/acceptance_criteria.json config/acceptance_criteria.lock && git commit -m 'Sign acceptance criteria' && git push -u origin main
```

| Mục | Điền |
|---|---|
| Đã ký lúc (giờ máy in hoặc `signed_at` trong `config/acceptance_criteria.lock`) | 2026-11-18T14:52:52 |
| Mã commit `Sign acceptance criteria` (7 ký tự đầu, `git log --oneline -1`) | 4856d0b |
| Đã push lên `origin main` thành công? | có |

**Ghi chú về người ký.** Trường `signed_by` trong file đã ký ghi "Trưởng nhóm KKK (vai Sản phẩm và kinh doanh)". Người thực hiện lệnh ký
và đứng tên là trưởng nhóm (Kỹ sư cổng 1), ký **đại diện cho vai Sản phẩm và kinh doanh theo ủy quyền của cả bàn**; các ngưỡng
trong file do cả bàn thống nhất. Vai Sản phẩm và kinh doanh chính thức của bàn là Vũ Quang Dũng (xem `TEAM.md`). File tiêu chí đã
khoá bằng hash nên giữ nguyên dòng `signed_by`, không sửa sau khi ký.

Sau bước này **không sửa** `config/acceptance_criteria.json`, kể cả mở rồi lưu lại bằng trình soạn thảo tự định dạng.
