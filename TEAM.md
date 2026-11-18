
# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):KKK
- Lớp: `L3A`
- Repo của bàn: `K5-L3A-DAY10-KKK-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8): S8

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |Đỗ Tuấn Anh|2A202603465 |Kỹ sư cổng 1 |Trưởng nhóm|
|   2 |Nguyễn Tiến Khoa        |2A202603460     |Kỹ sư cổng 2     | |
|   3 |Vũ Quang Dũng           |2A202603486     |Sản phẩm và kinh doanh     ||
|   4 |Phạm Tuấn Anh           |2A202603503     |Vận hành và pháp lý     |             |

Ghi `members` trong `submission/submission.json` theo dạng `"HoVaTen-MSSV"`, khớp bảng trên.

## Cá nhân

Mỗi thành viên tự viết một mục bên dưới (chép mẫu, đổi tiêu đề thành họ tên không dấu và MSSV, ví dụ `## NguyenVanAn-20241234`).

## DoTuanAnh-2A202603465

### Phần việc phụ trách

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## PhamTuanAnh-2A202603503

### Phần việc phụ trách

Vận hành và pháp lý: câu 1.2, 1.4 (Phiếu A); HAZOP ngoài kỹ thuật và checklist B4–B5; cổng operations/legal, runbook và giờ cao điểm B7.5–B7.6. Ở vòng 2 chỉ làm thẻ S8, phụ trách phần vận hành/pháp lý của Phiếu C và gom bài khi có đủ report/trace S8; các phần đó hiện chưa được đo hoặc điền kết quả.

### Đóng góp cụ thể

- Đã có câu trả lời 1.2 và 1.4 trong Phiếu A.
- Hoàn thiện B7.5–B7.6: phân công nhân viên mô phỏng, cảnh báo, dừng/bật lại và kế hoạch giờ cao điểm; đồng bộ operations/legal trong config.
- Rà soát HAZOP ngoài kỹ thuật và checklist B5: phân biệt kịch bản dự phòng với số đo, sửa tên trường cần lọc, ghi rõ bằng chứng còn chờ; không xác nhận Xong khi chưa có report.
- Điền tên nhóm/thành viên trong submission.json theo TEAM.md và ghi nhận thẻ S8 theo xác nhận của nhóm; quyết định và ba câu cuối còn chờ bằng chứng và quyết định chung.
- Có sử dụng trợ lý AI Codex để đọc hướng dẫn, soạn/rà nội dung trên và chỉnh file trên nhánh tuananh. Các con số vận hành là phương án cần bản thân và nhóm xem xét, giải thích, kiểm chứng trước khi chốt; chưa coi là kết quả pilot.

### Bằng chứng

Phiếu A câu 1.2/1.4; Phiếu B B4 phần ngoài kỹ thuật, B5, B7.5–B7.6; config/operating_gates.json phần operations/legal; submission/submission.json phần team/members. Các chỉnh sửa mới chưa commit, chưa có run ID; bổ sung mã commit/report thực tế sau khi nhóm tích hợp và chạy.

Đóng góp soạn Phiếu C cho S8: C3.4 (hiệu chỉnh lòng tin), một dòng hoàn trên hạn mức ở C3.1 Bước 2, C5 câu 3.3 (giả định môi trường), bản nháp HAZOP C4 và nhánh vận hành C6; Runbook 4–5 và danh sách bằng chứng cần nhận tại C11. Nội dung được soạn với Codex từ thẻ/dữ liệu S8 và phương án vận hành; phần giả thuyết, ngưỡng đề xuất và thông tin chờ trace/report được ghi rõ. Chưa nhận đã chạy S8, xác minh cổng hiện tại, diễn tập quy trình hoặc chứng minh kết quả after; các chỉnh sửa Phiếu C này chưa commit/push.

Tổng hợp bổ sung A/B theo yêu cầu cả nhóm: đã điền metric offline 1.3, giải thích 1.5 và sửa cách đo telemetry 1.4; tích hợp B1–B3 và B7.1–B7.4 từ các nhánh với nguồn rõ ràng, business từ QuangDung khớp config; tổng hợp đủ bốn lăng kính B6. Những nội dung thuộc vai khác ghi nhận là tổng hợp nguồn/tham khảo, không nhận thay đóng góp hay chữ ký của thành viên. B8 còn chờ quyết định hợp lệ và chữ ký thật, report bản cấu hình cuối chưa có.

Bổ sung sau khi đọc nhánh thành viên: góp ý ranh giới/soát A4 theo tiêu chí đã ký; rà HAZOP kỹ thuật B4 từ code và nguồn Khoa; ghi hai đề xuất cá nhân B6, nhật ký nguồn B0 và bằng chứng B8. Chưa ký quyết định chung hoặc xác nhận kết quả của cấu hình khác.

### Exit ticket

Chưa điền: Phạm Tuấn Anh tự ghi một điều học được và một điều còn chưa chắc sau khi trực tiếp rà nội dung, tham gia đánh giá/demo; không ghi thay trải nghiệm cá nhân.
# Team

## Thông tin nhóm

- Tên nhóm (`TenNhom`, không dấu, không khoảng trắng):KKK
- Lớp: `L3A` 
- Repo của bàn: `K5-L3A-DAY10-KKK-PoCtoPilotGate1`
- Thẻ sự cố đã bốc (S1–S8):

## Thành viên

Họ tên đầy đủ và MSSV của **mọi** thành viên; thêm dòng nếu cần. Vai: Kỹ sư cổng · Sản phẩm và kinh doanh · Vận hành và pháp lý (README mục 3, phút 0–15).

| STT | Họ và tên | MSSV | Vai | Trưởng nhóm |
| --: | --------- | ---- | --- | :---------: |
|   1 |Đỗ Tuấn Anh|2A202603465 |Kỹ sư cổng 1 |Trưởng nhóm|
|   2 |Nguyễn Tiến Khoa        |2A202603460     |Kỹ sư cổng 2     | |
|   3 |Vũ Quang Dũng           |2A202603486     |Sản phẩm và kinh doanh     ||
|   4 |Phạm Tuấn Anh           |2A202603503     |Vận hành và pháp lý     |             |

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
- Gộp xung đột Git trong `guards.py` và `templates/form-b-evaluation-gates.md` sau các lần merge của nhóm, để `guards.py` chạy lại được (trước đó còn dòng `<<<<<<<`).
- Ghi chú người ký ở Phiếu A mục A5 (người ký đại diện vai Sản phẩm và kinh doanh theo ủy quyền của bàn, vì file đã khoá hash không sửa được `signed_by`).

### Bằng chứng

- Commit: `4856d0b` (ký tiêu chí), `5ddc1f5` (Phiếu B mục B7.1–B7.3), `6f8f3f8` (gộp xung đột, `guards.py` sạch). Hash tiêu chí `446d401cddbe9d63a4956aea24832deb33d3af960b4e7d91cc4f7d2dc6199bb8`.
- Mã lần chạy: `R-base-after-20261118-164113-57e844` (mốc `after` với `guards.py` hiện tại): pass_rate 1,0, pass^k 1,0, hoàn sai 0đ, lỗi oan hãng 0, lộ PII 0, chuyển người 22,73%, chi phí 4.202đ/ticket, ROI 1,38, 0 ca ùn. Các lần chạy base, after, prepared khác ghi ở Phiếu B mục B0.
- Phiếu B: mục B7.1 (ba cổng), B7.2, B7.3; Phiếu A mục A5.
- Ticket hiểm (mốc `after`, seed 11): `O-1002/C-02` sổ cái `[]`, không ghi lỗi hãng (trước khi có cổng hoàn 30.000đ); `O-1001/C-01` hoàn 25.000đ do LOGIX trả (đề xuất ban đầu 345.000đ, payer MERCHANT), tin gửi hãng không còn `customer_note`.

### Exit ticket

- **Một điều học được:** đặt cổng ở tầng hệ thống, tính lại từ nguồn sự thật (tracking, chính sách, sổ cái) rồi mới cho ghi, hiệu quả hơn nhờ model "hiểu đúng". Lỗi chìm như hoàn theo số ngày khách khai không hiện ra với khách mà làm hãng chịu thiệt, và chỉ trace mới thấy.
- **Một điều còn chưa chắc:** các cổng tổng quát được với bài kiểm tra ẩn và gói sự cố hay chưa. Bộ nền đạt 100% nhưng chỉ có 22 ticket, nên chưa chứng minh được gì ngoài đó. Ngoài ra bản chốt vòng 1 (`guards_round1.py`) là bản của đồng đội còn `guards.py` hiện tại mạnh hơn, nên chưa rõ khoảng cách `prepared` so với `after` sẽ được đọc thế nào. Cổng chuyển người khi hãng đủ 2 lỗi trong ngày cũng chưa kiểm chứng đủ trên gói sự cố.

