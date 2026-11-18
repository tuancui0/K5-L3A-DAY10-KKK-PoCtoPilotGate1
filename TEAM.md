# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng): KKK
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-KKK-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S8

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 | Đỗ Tuấn Anh | 2A202603465 | Kỹ sư cổng 1 | Trưởng nhóm |
|   2 | Nguyễn Tiến Khoa | 2A202603460 | Kỹ sư cổng 2 | |
|   3 | Vũ Quang Dũng | 2A202603486 | Sản phẩm và kinh doanh | |
|   4 | Phạm Tuấn Anh | 2A202603503 | Vận hành và pháp lý | |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DoTuanAnh-2A202603465

### Phần việc phụ trách

Vai **Kỹ sư cổng 1** và trưởng nhóm.
- File: `lab10/guards.py` (hàm `pre_guard`, `write_gate`); tạo repo, gắn `upstream`, ký tiêu chí, gộp xung đột Git.
- Phiếu B: câu 2.6 (mục B7.1, ba cổng phòng ngừa), câu 2.7 (B7.2), câu 2.8 (B7.3, behavioral test).
- Phiếu A: mục A5 (giờ ký, mã commit, ghi chú người ký).
- Eval card chung của nhóm (`docs/team_eval_card.md`).

### Đóng góp cụ thể

- Viết ba cổng trong `lab10/guards.py`, đều dựa vào nguồn sự thật trong `data/world.json`, không theo mã ticket:
  - **G1 · Nguồn sự thật:** `pre_guard` ghim chính sách theo ngày hiệu lực. `write_gate` (`issue_refund`) tính lại quyền lợi từ tracking và chính sách, chặn hoàn khi quyền lợi bằng 0, giới hạn số tiền ở mức quyền lợi, ép bên trả là LOGIX (chặn số ngày khách tự khai, chỉ thị "hoàn toàn bộ", chế độ fail-open).
  - **G2 · Tiền ra cửa:** chặn hoàn trùng theo đơn, kiểm tra phê duyệt (còn hiệu lực, chưa hết hạn, đủ hạn mức, gắn đúng ticket và đơn hoặc khách), trần hoàn tự động theo khách mỗi ngày và theo ngày, trần lỗi hãng mỗi ngày (kiểm trước khi ghi tiền).
  - **G3 · Bên thứ ba:** `file_carrier_fault` chỉ ghi khi DB có nguyên nhân đủ điều kiện, sửa về đúng kiện, hãng, tài xế, số ngày; `notify_carrier` chỉ giữ các trường chính sách cho phép (bỏ `customer_note`, `recipient_contact`); `send_reply` ép số tiền khớp sổ cái.
  - Thêm kiểm tra người gửi là chủ đơn, lệnh khớp đơn, kiện thuộc đơn (tham khảo bản của đồng đội).
- Tự chạy `trace --adhoc` với hai ticket hiểm và dán kết quả vào B7.3 (đơn `O-1002` khách khai trễ 9 ngày; đơn `O-1001` có chỉ thị hoàn toàn bộ tính cho shop).
- Phát hiện và sửa lỗi hash của tiêu chí đã ký: Git trên Windows đổi LF thành CRLF làm lệch hash. Tắt `core.autocrlf` cho repo và khôi phục đúng byte đã ký.
- Gộp xung đột Git trong `guards.py` và `templates/form-b-evaluation-gates.md` sau các lần merge của nhóm, để `guards.py` chạy lại được.
- Ghi chú người ký ở Phiếu A mục A5 (người ký đại diện vai Sản phẩm và kinh doanh theo ủy quyền của bàn).

### Bằng chứng

- Commit: `4856d0b` (ký tiêu chí), `5ddc1f5` (Phiếu B mục B7.1–B7.3), `6f8f3f8` (gộp xung đột, `guards.py` sạch). Hash tiêu chí `446d401cddbe9d63a4956aea24832deb33d3af960b4e7d91cc4f7d2dc6199bb8`.
- Mã lần chạy: `R-base-after-20261118-164113-57e844` (mốc `after` với `guards.py` vòng 1): pass_rate 1.0, pass^k 1.0, hoàn sai 0đ, lỗi oan hãng 0, lộ PII 0, chuyển người 22.73%, chi phí 4.202đ/ticket, ROI 1.38, 0 ca ùn.
- Phiếu B: mục B7.1 (ba cổng), B7.2, B7.3; Phiếu A mục A5.
- Ticket hiểm (mốc `after`, seed 11): `O-1002/C-02` sổ cái `[]`, không ghi lỗi hãng; `O-1001/C-01` hoàn 25.000đ do LOGIX trả, tin gửi hãng không còn `customer_note`.

### Exit ticket

- **Một điều học được:** Đặt cổng ở tầng hệ thống, tính lại từ nguồn sự thật (tracking, chính sách, sổ cái) rồi mới cho ghi, hiệu quả hơn nhờ model "hiểu đúng". Lỗi chìm như hoàn theo số ngày khách khai không hiện ra với khách mà làm hãng chịu thiệt, và chỉ trace mới thấy.
- **Một điều còn chưa chắc:** Các cổng tổng quát được với bài kiểm tra ẩn và gói sự cố hay chưa. Bộ nền đạt 100% nhưng chỉ có 22 ticket, nên chưa chứng minh được gì ngoài đó.

## NguyenTienKhoa-2A202603460

### Phần việc phụ trách

Vai **Kỹ sư cổng 2**.
- Phụ trách phân tích kỹ thuật thẻ sự cố S8 (mất lòng tin người duyệt, lạm dụng approval).
- Viết bổ sung và hoàn thiện các cổng kiểm soát phê duyệt trong `lab10/guards.py` cho vòng 2: kiểm tra trạng thái approval, chống tái sử dụng mã (`ctx.tools.ledger_rows(approval_id=approval_id)`), kiểm tra đúng ticket/đơn/khách, hạn mức tối đa, thời hạn hiệu lực, và trần tự động hàng ngày.
- Xây dựng các hàm monitor trong `lab10/monitors.py` (`approval_invalid_attempt_rate`, `manual_recheck_rate`, `queue_wait_max_minutes`) để phát hiện bất thường không cần nhãn ground-truth.
- Chạy đánh giá `lab10.grade --incident S8`, `lab10.eval`, kiểm thử unit test 13/13, và chạy lệnh gom bài nộp `lab10.check_submission --collect`.

### Đóng góp cụ thể

- Dò trace các ticket lỗi của thẻ S8: S8-01 (dùng mã đã used A-2801), S8-02 (mã hết hạn), S8-03 (vượt hạn mức max_vnd 150k chi 235k), S8-06 (mã revoked A-2806); đối chứng với ca hợp lệ S8-05.
- Cập nhật `write_gate` trong `lab10/guards.py`:
  - Ghim kiểm tra tính hợp lệ của approval trước khi ghi lệnh hoàn tiền `issue_refund`.
  - Chặn triệt để việc tái sử dụng `approval_id` bằng cách kiểm tra sự tồn tại trong `ledger_rows`.
  - Kiểm tra đối soát với trần vận hành `ops_limits` (trần mỗi khách mỗi ngày, ngân sách ngày, trần vi phạm của hãng) trước khi thực hiện lệnh ghi.
  - Ghi log sự kiện `approval_invalid_attempt` và `customer_daily_cap_blocked` vào trace.
- Thêm 3 monitors mới trong `lab10/monitors.py` giúp `lab10.grade` bật đèn tín hiệu giám sát (sáng đèn ở cả before và after khi có biến động).
- Đảm bảo toàn bộ 13/13 test trong `tests/test_public.py` vượt qua không có lỗi suy thoái (regression).
- Đóng góp nội dung kỹ thuật vào Phiếu C: mục C2 (bảng soát lỗi), C4 (HAZOP S8), C7 (bảng sửa nguyên nhân kỹ thuật), C8 (chỉ số theo dõi mới).

### Bằng chứng

- Commit và code: `lab10/guards.py`, `lab10/monitors.py`.
- Mã lần chạy grade tự kiểm tra: `R-S8-grade-20261118-172346-d6d69c` đạt 5/5 tiêu chí visible, criteria, integrity, regression, monitor.
- Báo cáo mốc after `R-S8-after-20261118-172351-d6d69c`: pass_rate 1.0, 0 hoàn sai, 0 lỗi oan hãng, 0 lộ PII, 0 ca ùn, thời gian chờ tối đa 5.0 phút, chi phí 2.952đ/ticket, ROI 2.39.
- Test suites: `Ran 13 tests ... OK`.

### Exit ticket

- **Một điều học được:** Cổng kiểm soát kỹ thuật ở tầng ghi (write_gate) là phòng tuyến cốt lõi để bảo vệ ngân sách và tuân thủ thẩm quyền. Tuy nhiên, nếu không giải quyết bài toán niềm tin con người (cung cấp giải thích và tỷ lệ kiểm mẫu hợp lý) thì hệ thống dù an toàn về mặt code vẫn sẽ bị tê liệt trong vận hành do con người kiểm tay 100%.
- **Một điều còn chưa chắc:** Tính nguyên tử (atomicity) giữa thời điểm đọc approval và thời điểm ghi ledger trong môi trường chịu tải cao thực tế (nhiều yêu cầu đồng thời) cần được bảo đảm bằng cơ chế khóa phân tán hoặc transaction DB.

## VuQuangDung-2A202603486

### Phần việc phụ trách

Vai **Sản phẩm và kinh doanh**.
- Phụ trách tiêu chí chấp nhận ở Phiếu A và cấu hình `config/acceptance_criteria.json`.
- Phụ trách phân tích bản đồ dữ liệu và drift ở Phiếu B mục B3; cấu hình kinh doanh `business` trong `config/operating_gates.json` (mục B7.4).
- Phân tích hiệu quả kinh tế mốc after của S8 (chi phí mỗi ticket, ROI, trần ngân sách hoàn tự động) và đánh giá quyết định Gate 1 (v1 ở Phiếu B mục B8, v2 ở Phiếu C mục C12).

### Đóng góp cụ thể

- Xác lập các ngưỡng kinh doanh trong `config/acceptance_criteria.json`: pass_rate >= 0.97, pass_k >= 0.92, hoàn sai = 0, lỗi oan hãng = 0, PII = 0, chi phí <= 8.000đ/ticket (thấp hơn làm tay 10.000đ), ROI >= 0.3, queue_stuck = 0.
- Điền các con số kinh doanh trong `config/operating_gates.json`: trần hoàn ngày 1.800.000đ, ngân sách chi phí mỗi ticket 900đ, pilot_scope 100%, ROI tối thiểu 0.3.
- Phân tích tác động kinh doanh của sự cố S8: khi nhân viên CSKH mất niềm tin và kiểm tay 100%, chi phí mỗi ticket vọt lên 11.225đ (đắt hơn làm tay 10.000đ), làm toàn bộ dự án bị âm ROI (-2.45) và xuất hiện 36 ca ùn.
- Phân tích và đối chiếu mốc after sau khi bật `decision_note: true` và `review_sampling_pct: 10`: chi phí giảm xuống 2.952đ/ticket, ROI vọt lên 2.39, tiết kiệm ròng 366.479đ/ngày, 0 kho nào đắt hơn làm tay.
- Ký quyết định Gate 1 v1 ở Phiếu B mục B8: **Tiếp tục**, chỉ sang vòng sự cố, chưa mở cho khách thật. Bằng chứng là bộ nền prepared đạt cả 5 chỉ số, chi phí 4.202đ, ROI 1,38, 0 ca ùn. Vế "gói sự cố" của dòng Tiếp tục để lại cho v2 kiểm.
- Hoàn thiện lập luận quyết định Gate 1 v2 chọn **Tiếp tục** mở pilot do toàn bộ tiêu chí đã ký và các trần kinh tế/vận hành đều đạt.
- Thống nhất mã lần chạy trong C12 theo bộ nộp (`submission/runs/`) và điền phân khúc xấu nhất (kho DN, 3.200đ/ticket ở after).

### Bằng chứng

- File cấu hình: `config/acceptance_criteria.json` (commit ký `4856d0b`), `config/operating_gates.json`.
- Bộ nền vòng 1: base `R-base-before-20261118-151326-bde05c`, prepared `R-base-prepared-20261118-151855-6053af` (Phiếu B mục B8).
- Gói S8: after `R-S8-after-20261118-185846-d6d69c`, grade `R-S8-grade-20261118-185843-d6d69c`. Chi phí 2.952đ ≤ 8.000đ, ROI 2,39 ≥ 0,3, tiết kiệm ròng 366.479đ/ngày.
- Phiếu A: mục A1–A4; Phiếu B: mục B3, B7.4, B8; Phiếu C: mục C12.
- Dùng AI (Claude Code) để đọc report, đối chiếu số giữa report và Phiếu B, C, `submission.json`, và soát câu chữ B8, C12. Các ngưỡng, con số trong config và quyết định v1, v2 là của bàn.

### Exit ticket

- **Một điều học được:** Bài toán kinh tế của ứng dụng AI phụ thuộc mật thiết vào hành vi con người. Trợ lý AI chỉ tạo ra ROI dương khi tỷ lệ kiểm tra của con người giảm về mức kiểm mẫu có kiểm soát; nếu con người hoài nghi và kiểm tra lại toàn bộ thì chi phí vận hành sẽ cao hơn cả khi không dùng AI.
- **Một điều còn chưa chắc:** Mức độ tiết kiệm chi phí thực tế khi triển khai trên diện rộng có thể bị ảnh hưởng bởi biến động số lượng ticket trong các dịp khuyến mãi lớn hoặc đợt bão lũ làm tăng tỷ lệ chậm trễ của các hãng vận chuyển.

## PhamTuanAnh-2A202603503

### Phần việc phụ trách

Vai **Vận hành và pháp lý**.
- Phụ trách câu 1.2, 1.4 trong Phiếu A (luật chơi vận hành, telemetry).
- Phân tích HAZOP ngoài kỹ thuật (B4) và checklist 9 nhóm việc (B5) trong Phiếu B.
- Cấu hình vận hành và pháp lý trong `config/operating_gates.json` (`operations`, `legal`), xây dựng Runbook 1–3 và kế hoạch giờ cao điểm (B7.5, B7.6).
- Phụ trách phân tích vận hành và pháp lý trong sự cố S8: mục C3.4 (hiệu chỉnh lòng tin), C5 câu 3.3 (giả định môi trường), xây dựng Runbook 4–5 và kịch bản ứng phó khẩn cấp ở Phiếu C mục C11.

### Đóng góp cụ thể

- Hoàn thiện cấu hình vận hành và pháp lý trong `config/operating_gates.json`:
  - `operations.pic`: NV-TUNG, `approver_id`: NV-HANH, `reviewers_on_shift`: 1, `review_capacity_per_hour`: 6 ca/giờ, `max_queue_wait_minutes`: 60.
  - Điều kiện dừng `stop_conditions` và kênh cảnh báo `alert_channel`.
  - Cổng pháp lý: chặn các trường PII (`customer_note`, `recipient_contact`, `name`, `phone`, `street`) và yêu cầu lỗi hãng phải có nguyên nhân tracking.
  - Cập nhật điều kiện khôi phục niềm tin ở vòng 2: `decision_note: true`, `review_sampling_pct: 10`.
- Phân tích hiệu chỉnh lòng tin tại C3.4: phân tích sự sai lệch giữa mức tin quá mức trước kiểm toán và mất niềm tin sau kiểm toán của nhân viên duyệt và trưởng ca đứng tên.
- Xây dựng Runbook 5 với 3 kịch bản ứng phó sự cố tuần đầu chạy thử: quá tải ticket gấp 3, nhà cung cấp LLM gián đoạn > 5 phút, và người duyệt báo không tin trợ lý.
- Cập nhật checklist 9 nhóm việc với phân công người phụ trách (PIC) rõ ràng.

### Bằng chứng

- File cấu hình: `config/operating_gates.json` (mục `operations` và `legal`).
- Phiếu A: mục A1, A2; Phiếu B: mục B4 (ngoài kỹ thuật), B5, B7.5, B7.6.
- Phiếu C: mục C3.4, C5 (giả định môi trường), C10 (Risk register), C11 (checklist cập nhật và Runbook 4–5).
- Kết quả vận hành mốc after: số ca ùn giảm từ 36 về 0 ca, thời gian chờ tối đa giảm từ 216 phút xuống 5.0 phút, tỷ lệ kiểm lại giảm về 10%, niềm tin nhân viên duyệt đạt.

### Exit ticket

- **Một điều học được:** Quản trị rủi ro AI không chỉ dừng lại ở thuật toán mà bắt buộc phải có các quy trình vận hành dự phòng (SOP/Runbook), cơ chế ngắt tự động (kill switch) và phân định rõ ràng thẩm quyền của người đứng tên chịu trách nhiệm pháp lý.
- **Một điều còn chưa chắc:** Khả năng đáp ứng thực tế của ca trực khi có sự cố kép (vừa quá tải ticket vừa gián đoạn dịch vụ LLM) nếu đội ngũ chưa được trải qua các buổi diễn tập mô phỏng (tabletop exercise).
