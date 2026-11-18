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

Vai trong bàn; câu nào của đề, mục nào của phiếu A/B/C, file nào (`lab10/guards.py`, `config/operating_gates.json`, …).

### Đóng góp cụ thể

...

### Bằng chứng

Mã commit, mã lần chạy (`runs/<mã>`), dòng trong phiếu.

### Exit ticket

Một điều học được, một điều còn chưa chắc.

## VuQuangDung-2A202603486

### Phần việc phụ trách

Vai Sản phẩm và kinh doanh. Câu 1.1 và câu 1.6 trên Phiếu A; câu 2.3 (bản đồ dữ liệu) và câu 2.9 (cổng `business`) trên Phiếu B. Không sửa `lab10/guards.py`, không điền cổng `operations` / `legal`.

### Đóng góp cụ thể

- Câu 1.1: mục tiêu cấp hệ thống cho hai kho pilot, hoàn đúng chính sách, đối soát được, chuyển duyệt khi thiếu căn cứ.
- Câu 1.6: phiếu viết cho khớp tiêu chí đã ký, không sửa file sau khi khóa. Ngưỡng trong JSON: `pass_rate_min` 0,97, `pass_k_min` 0,92, ba chỉ số an toàn bằng 0, `escalation_rate_max` 0,25, chi phí tối đa 8.000 đồng/ticket, ROI tối thiểu 0,3, không ca ùn.
- Câu 2.3: nguồn sự thật là đơn, kiện, chính sách hiệu lực tại `as_of` 2026-11-16; ticket và câu trả lời của model chỉ là diễn giải. Ghi drift chính sách REFUND-v4 từ 2026-12-01.
- Câu 2.9: `daily_refund_cap_vnd` 2.000.000, `cost_budget_per_ticket_vnd` 1.500 (trần LLM, không phải tổng chi phí 8.000), `pilot_scope` kho HN và HCM, `roi_min` 0,3.
- Câu 2.5: hai lý do lăng kính kinh doanh trong pre-mortem (vượt trần hoàn ngày; pilot lỗ hoặc mở nhầm kho sỉ), nối vào đúng các cổng `business` ở trên. Ba lăng kính còn lại để vai khác.

### Bằng chứng

- Tiêu chí đã ký: commit `4856d0b`, `signed_at` `2026-11-18T14:52:52`, hash `446d401cddbe9d63a4956aea24832deb33d3af960b4e7d91cc4f7d2dc6199bb8`. Trường `signed_by` ghi trưởng nhóm ký đại diện vai Sản phẩm và kinh doanh; không sửa dòng đó sau khi khóa.
- Phiếu A câu 1.1 và 1.6: commit `f1127db`, sau đó sửa lại cho khớp ngưỡng đã ký (phiếu, không đụng JSON).
- Phiếu B câu 2.3 và bảng B7.4, cùng `config/operating_gates.json` mục `business`.

### Exit ticket

Học được: ký trước khi đo nghĩa là phiếu phải chạy theo file đã khóa, không được "sửa cho đẹp" rồi ký lại. Còn chưa chắc: hai kho HN và HCM có nằm trong công suất 48 lượt duyệt/ca hay không, vì chưa có số đo vòng 1.
