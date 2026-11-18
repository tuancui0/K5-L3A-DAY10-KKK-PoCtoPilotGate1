# Phiếu B · Đo, rủi ro, cổng vòng 1 và quyết định v1 · Khối 2A + 2B + chốt (phút 65–115)

**Bàn:** ______

Tiêu chí đã ký ở Phiếu A. Từ phút 65 bàn mới được chạy trợ lý. Khối 2A (65–85) chưa sửa code hay config. Khối 2B (85–105) sửa
`lab10/guards.py` và `config/operating_gates.json`. Phút 105–115 chốt cổng vòng 1 rồi viết quyết định v1. Sau phút 115 không sửa phiếu này
(trừ khi Phiếu C bảo "mở lại" một ô và ghi bằng bút khác màu).

**Mục lục**
- [B0 · Nhật ký lần chạy vòng 1 (suốt khối)](#b0)
- [B1 · Câu 2.1 · Lần chạy đầu tiên, cổng tự chặn hay người duyệt · phút 65–71](#b1)
- [B2 · Câu 2.2 · Bảng soát lỗi `T-002@55` · phút 71–75](#b2)
- [B3 · Câu 2.3 · Bản đồ dữ liệu và ví dụ drift · phút 65–75](#b3)
- [B4 · Câu 2.4 · HAZOP vòng 1 · phút 65–75](#b4)
- [B5 · Câu 2.4 · Checklist 9 nhóm việc, lần 1 · phút 70–75](#b5)
- [B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa · phút 75–85](#b6)
- [B7 · Câu 2.6–2.10 · Cổng phòng ngừa, runbook phần 1–3, giờ cao điểm · phút 85–105](#b7)
- [B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 · phút 105–115](#b8)

---

<a id="b0"></a>

## B0 · Nhật ký lần chạy vòng 1

*Yêu cầu: ít nhất 3 lần chạy, mỗi lần đổi một thứ, có mã lần chạy và khoảng tin cậy.* Mỗi lệnh `lab10.eval` và `lab10.grade` tự ghi
một dòng vào `runs/journal.jsonl`. Việc của bàn là điền cột "Đổi MỘT thứ gì" (tham số `--note`) và cột "Kết luận".
Mọi con số trong quyết định Gate 1 phải trỏ về một dòng ở đây hoặc ở Phiếu C mục C0.

| # | Mã lần chạy | Bộ ticket · mốc | Đổi MỘT thứ gì so với lần trước | pass_rate (khoảng tin cậy 95%) | pass_k | Hoàn sai (đ) · lỗi hãng oan · lộ dữ liệu | Tỉ lệ chuyển người | Kết luận (một câu) |
|---|---|---|---|---|---|---|---|---|
| 1 | | base · base | (baseline, chưa có cổng) | | | | | |
| 2 | | base · after | (cổng vòng 1, thử trước khi chốt) | | | | | |
| 3 | | base · prepared | (cổng vòng 1 đã chốt) | | | | | |
| 4 | | | | | | | | |

---

<a id="b1"></a>

## B1 · Câu 2.1 · Lần chạy đánh giá đầu tiên

```bash
python3 -m lab10.eval --suite base --stage base --note "baseline"
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

- Mã lần chạy: `__________` (ghi cả vào B0 dòng 1)
- Ngưỡng đã ký nào `[CHƯA]` đạt: …
- Khối "kinh doanh và vận hành" ở cuối output: dòng nào đáng lo? …
- Khối "theo kho và hãng": kho hoặc hãng nào có số xấu nhất? …

**Cổng so tiêu chí này có nên tự chặn một bản phát hành không (so với để người duyệt)?**

| Lý lẽ ủng hộ tự chặn | Lý lẽ phản đối |
|---|---|
| | |

Khuyến nghị (khoanh một): **tự chặn · người duyệt · kết hợp**. Vì: …

---

<a id="b2"></a>

## B2 · Câu 2.2 · Bảng soát lỗi cho `T-002@55`

```bash
python3 -m lab10.trace --suite base --ticket T-002 --seed 55
```

**Cách làm, giữ nguyên ba phần:** (1) ghi lại từng lỗi bằng **cái người ta thực sự thấy**, ai gặp, mức hệ trọng,
và xếp vào một trong ba **loại lỗi**; (2) đưa lỗi qua bộ câu hỏi để tìm **nguồn**; (3) viết **hướng xử lý**: vì sao người ta coi
đó là lỗi, người ta đi tiếp bằng đường nào, hệ thống học được gì.

Ba loại lỗi:
- **Giới hạn của hệ thống**: hệ thống không thể trả lời đúng, hoặc không trả lời được, vì giới hạn vốn có.
- **Lỗi ngữ cảnh**: hệ thống "chạy đúng thiết kế" nhưng người dùng thấy sai, vì hành động không được giải thích, trái với hình dung của họ, hoặc dựa trên giả định kém.
- **Lỗi chìm**: hệ thống chạy sai mà **cả người dùng lẫn hệ thống đều không nhận ra**. Với một trợ lý có quyền ghi sổ, đây là loại nguy hiểm nhất: người chịu hại thường là bên thứ ba.

### Phần 1 · Ghi lỗi (bằng chứng là mã ticket@seed và dòng trace, không tả chung chung)

| # | Lỗi: người ta thấy gì (dán dòng trace / sổ cái) | Ai gặp, ai chịu | Hệ trọng (thấp / cao) | Loại lỗi (giới hạn hệ thống / ngữ cảnh / chìm) |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

### Phần 2 · Tìm nguồn (đánh dấu câu nào đúng với từng lỗi)

| Câu hỏi | Lỗi 1 | Lỗi 2 |
|---|---|---|
| **Đầu vào:** hệ thống có tự diễn giải / sửa đầu vào của người dùng theo cách họ không lường? Có đặt sai trọng số cho một lời nói hay tín hiệu của người dùng? | | |
| **Độ liên quan:** hệ thống có thiếu dữ liệu cần để quyết đúng? Dữ liệu vào có nhiễu, thiếu ổn định? | | |
| **Thứ bậc hệ thống:** có hai hệ thống cùng ghi / cùng theo dõi một thứ mà không rõ bên nào là chủ (ví dụ CSKH hoàn tay và trợ lý cùng ghi sổ)? | | |
| **Trạng thái hỏng:** nhiều lỗi cộng lại có làm tính năng không dùng được (ví dụ LLM lỗi liên tiếp)? | | |

### Phần 3 · Hướng xử lý (mỗi lỗi một ô)

| | Lỗi 1 | Lỗi 2 |
|---|---|---|
| Vì sao người gặp coi đây là lỗi | | |
| Kiểu giải pháp: phản hồi cho người dùng / trao quyền kiểm soát cho người / khác | | |
| Đường đi của người sau khi có giải pháp (ví dụ: ticket chuyển sang người duyệt → duyệt → khách được trả lời) | | |
| Hệ thống học được gì (tín hiệu ghi lại để theo dõi: tên metric trong `monitors.py`) | | |

**Ví dụ (bộ nền, đừng chép):** `T-002@55` · sổ cái có dòng hoàn 20.000đ, hãng VNX nhận một lỗi, trong khi tracking ghi trễ 2 ngày ·
khách không thấy gì sai, hãng chịu · cao · **lỗi chìm**. Nguồn: đầu vào (đặt sai trọng số cho con số khách tự khai). Xử lý:
hãng coi là lỗi vì sổ giao của họ ghi 2 ngày; kiểu giải pháp: trao quyền cho người (số khai khác tracking thì chuyển người duyệt);
tín hiệu: đếm sự kiện `model_override` mỗi ngày.

---

<a id="b3"></a>

## B3 · Câu 2.3 · Bản đồ dữ liệu của trợ lý và ví dụ drift

**Cách làm:** đi từ người dùng và việc họ cần làm, tới đầu ra của hệ thống, rồi mới hỏi hệ thống cần dữ liệu
gì, định dạng ra sao, và **thế giới thật làm dữ liệu đó lệch đi thế nào**; cuối cùng tóm lại trong vài câu.
Trợ lý LogiX không huấn luyện gì trong lab này, nên ta hỏi về "dữ liệu trợ lý đọc lúc chạy / trường then chốt / nguồn sự thật".
Gợi ý: mở `data/world.json` phần `policies`, `orders[].parcels`, `ops_limits`, `ops_facts`.

| Mục | Điền cho trợ lý hoàn tiền |
|---|---|
| Người dùng | Khách gửi yêu cầu hoàn tiền vì giao trễ; nhân viên CSKH và trưởng ca tiếp nhận những trường hợp cần người duyệt. Kế toán đối soát, shop và hãng vận chuyển là các bên chịu tác động của tiền hoàn và lỗi hãng được ghi. |
| Việc người dùng cần làm xong | Khách được giải quyết yêu cầu đúng đơn, đúng khách, đúng kiện và chính sách đang hiệu lực; CSKH có đủ căn cứ để duyệt ngoại lệ, không phải xử lý hàng chờ vượt công suất. Kế toán có thể đối soát khoản hoàn và hãng chỉ bị ghi lỗi khi có căn cứ. |
| Đầu ra của hệ thống (kể cả các lệnh ghi) | Quyết định hoàn, không hoàn hoặc chuyển người duyệt; số tiền và căn cứ. Các lệnh ghi gồm `issue_refund` (ghi khoản hoàn), `file_carrier_fault` (ghi lỗi hãng), `notify_carrier` (gửi thông báo cho hãng), `send_reply` (trả lời khách). Thông tin trả lời phải khớp khoản tiền thực sự được ghi sổ; dữ liệu gửi hãng phải nằm trong danh sách trường được phép. |
| Dữ liệu trợ lý đọc lúc chạy (bảng nào trong `data/world.json`) | Ticket nằm ở `data/tickets.jsonl`, không nằm trong `world.json`. Trong `world.json`: `as_of`, `orders` và `orders[].parcels`, `customers`, `policies`; `ops_limits` và `ops_facts` là căn cứ dựng cổng và tính khả năng vận hành. Phân biệt dữ liệu nghiệp vụ với các ngưỡng nhóm chọn trong `config/operating_gates.json`. |
| Trường then chốt quyết định tiền và lỗi hãng | Định danh: `order_id`, `customer_id`, `parcel_id`, `carrier_id`. Tiền: `shipping_fee_vnd`, `goods_value_vnd`; tracking: `promised_date`, `delivered_date`, `status`, `delay_cause`, cùng `as_of`. Chính sách: `effective_from`, `effective_to`, `late.min_days_fee`, `late.min_days_bonus`, `late.bonus_pct`, `late.bonus_cap_vnd`, `auto_limit_vnd`, `fault_causes`, `no_refund_causes`. `refund_status` cần được đối chiếu với sổ hoàn để tránh hoàn trùng. |
| Với mỗi trường then chốt: **nguồn sự thật** hay **bản sao** (ai cập nhật, khi nào)? | Trong lab, DB đơn/tracking và bảng `policies` là nguồn chuẩn để đối chiếu, không lấy số ngày hoặc số tiền khách tự khai làm sự thật. `order_id`, `customer_id`, giá trị hàng và phí vận chuyển thuộc hồ sơ đơn; các ngày giao, trạng thái, nguyên nhân và hãng thuộc bản ghi tracking từng kiện. `policies` là bản chính sách có khoảng hiệu lực; `index_active` là cờ phục vụ tra cứu, không thay thế kiểm tra ngày hiệu lực. Ticket, đề xuất model và nội dung trả lời là lời khai/bản diễn giải, không phải nguồn chuẩn cho tiền và lỗi hãng. `world.json` là ảnh chụp mock tại `as_of = 2026-11-16`, không có nhật ký chứng minh ai cập nhật từng trường. Khi pilot thật, nhóm yêu cầu hệ thống đơn hàng cập nhật hồ sơ khi tạo/đổi đơn, vận hành/hãng cập nhật tracking khi có sự kiện, chủ chính sách công bố phiên bản trước ngày hiệu lực; bộ phận sở hữu từng nguồn và SLA đồng bộ phải được xác nhận, không coi đây là dữ kiện đã được lab bảo đảm. |
| Định dạng cần để ý (ngày, trường được phép trống, đơn nhiều kiện) | Ngày dùng `YYYY-MM-DD`; chọn chính sách theo `as_of` trong khoảng hiệu lực, không lấy ngày máy. `effective_to = null` nghĩa là chưa có ngày kết thúc. `delivered_date` có thể trống: helper dùng `as_of` làm mốc cuối để tính độ trễ, nhưng riêng helper này không xét `status`, nên vẫn phải kiểm tra trạng thái. `parcels` là danh sách: ticket có `parcel_id` thì phải xác định đúng kiện; nếu không có, helper chọn kiện trễ nhất, cần xem đây có phải giả định phù hợp ngoài thực tế. Tiền dùng số nguyên VND; nguyên nhân dùng mã như `CARRIER`, `FORCE_MAJEURE`, `CUSTOMER_ABSENT`. Thiếu dữ liệu trọng yếu thì chuyển người kiểm tra, không tự bịa giá trị. |
| Thế giới thật làm dữ liệu lệch ở đâu (theo mùa, đổi chính sách, giờ cao điểm, người nhập tay)? | Ngày 01/12/2026 chính sách đổi từ v3 sang v4 nhưng chỉ mục hoặc cache có thể còn v3; mưa bão làm tăng ca `FORCE_MAJEURE`; quét giao hàng muộn hoặc nhập bù làm ngày giao/nguyên nhân không còn phản ánh đúng thực tế; một đơn tách nhiều kiện khiến giả định một đơn–một hãng sai. Cao điểm làm lượng ticket tăng trong khi công suất mock chỉ 6 ca/giờ/người, khiến chi phí, ROI và hàng chờ không còn giống `ops_facts`. Đây là các rủi ro dự kiến, chưa phải kết quả đo của nhóm. |
| Câu người ngoài sẽ hỏi về nguồn dữ liệu ("sao hệ thống biết đơn trễ mấy ngày?") | “Hệ thống lấy ngày hẹn và ngày giao từ kiện nào, có bị cập nhật muộn không? Vì sao ghi lỗi cho hãng này, nguyên nhân tracking là gì? Chính sách nào đang hiệu lực và tiền hoàn được tính ra sao?” Cần truy được `order_id`, `parcel_id`, ngày tracking, `delay_cause`, phiên bản chính sách và bút toán thực tế để giải thích; không trả lời chỉ bằng việc model đã nói như vậy. |

**Tóm lại:**
Trợ lý dùng **hồ sơ đơn và tracking từng kiện**, **chính sách có ngày hiệu lực**, **giới hạn và dữ kiện vận hành** để giúp **khách hàng và CSKH** giải quyết **yêu cầu hoàn tiền giao trễ đúng tiền, đúng trách nhiệm và có thể đối soát**.
Hai nhóm trường mà nếu sai thì tiền hoặc lỗi hãng sai theo là **ngày giao/ngày hẹn và nguyên nhân trễ của đúng kiện**, **các điều khoản của phiên bản chính sách đang hiệu lực**.
Thế giới thật có thể làm lệch **tracking khi đồng bộ chậm, chính sách khi chỉ mục chưa cập nhật và công suất duyệt khi cao điểm**. Dấu hiệu sớm cần theo dõi là **phiên bản chính sách được dùng không khớp khoảng hiệu lực**, **tracking thiếu/mâu thuẫn** và **hàng chờ tăng**; đây là các tín hiệu đề xuất, không khẳng định đã có monitor tương ứng.

**Ví dụ drift trong 3 tháng tới — chính sách đổi ngày 01/12/2026:**

- **Cái gì đổi:** REFUND-v3 hết hiệu lực ngày 30/11/2026; REFUND-v4 bắt đầu ngày 01/12/2026. Ngưỡng hoàn phí giảm từ trễ 3 xuống 2 ngày, ngưỡng thưởng giảm từ 7 xuống 5 ngày, trần thưởng tăng từ 200.000 lên 300.000 đồng, giới hạn tự động giảm từ 200.000 xuống 100.000 đồng. V4 bỏ `FORCE_MAJEURE` khỏi `fault_causes`: trễ do bất khả kháng vẫn có thể được hoàn theo chính sách nhưng không được ghi lỗi hãng.
- **Trường cho thấy:** `policies[].effective_from`, `effective_to`, `late.*`, `auto_limit_vnd`, `fault_causes`, đối chiếu với `as_of` và phiên bản hệ thống thực sự dùng. Trong ảnh chụp hiện tại, v3 có `index_active = true`, v4 có `index_active = false`; điều này phù hợp tại 16/11/2026, nhưng nếu giữ nguyên chỉ mục sau 01/12 thì có nguy cơ tra nhầm bản cũ. Không coi đó là sự cố đã xảy ra.
- **Ví dụ hậu quả:** Với ca trễ do `FORCE_MAJEURE` từ 3 ngày trở lên sau ngày 01/12, dùng v3 thay vì v4 có thể làm hệ thống ghi lỗi oan cho hãng. Với ca trễ 2 ngày do hãng, dùng v3 có thể không hoàn phí dù v4 đã cho phép. Đây là tình huống phân tích, không phải kết quả chạy ticket mới.
- **Con số trong Bản tiêu chí bị ảnh hưởng:** `wrongful_carrier_faults_max = 0` có thể bị vượt; `pass_rate_min = 0,97` và `pass_k_min = 0,92` có thể không đạt. Thay đổi mức hoàn và chuyển duyệt còn có thể tác động `cost_per_ticket_vnd_max = 8.000`, `roi_min = 0,3` và `queue_stuck_max = 0`; phải đo mới biết mức ảnh hưởng, không tự suy ra số kết quả.
- **Loại drift:** Chủ yếu là **quan hệ đầu vào–đầu ra đổi (concept drift do chính sách)**: cùng số ngày trễ và nguyên nhân nhưng sau ngày hiệu lực phải ra quyết định khác. Tra cứu nhầm chỉ mục là vấn đề dữ liệu/đồng bộ đi kèm. Không chỉ là thay đổi tần suất ticket đầu vào.
- **Chỉ số phát hiện:** Offline, tạo bộ thử theo ngày hiệu lực và kiểm `pass_rate`, `pass^k`, số lỗi hãng oan so với chính sách đúng ngày. Trong production không có nhãn, đề xuất theo dõi tỉ lệ quyết định dùng phiên bản khác với chính sách có khoảng hiệu lực chứa ngày xử lý, trên cửa sổ 1 giờ, báo động nếu lớn hơn 0; nếu không tìm được chính sách hiệu lực thì đếm riêng và báo động ngay. Đây là phép kiểm nhất quán với bảng chính sách đã duyệt, không phải nhãn thiệt hại thực tế; vẫn cần kiểm mẫu để phát hiện trường hợp chính bảng nguồn sai. Chỉ số đề xuất này chưa được cài vào `monitors.py`.

**Ví dụ một dòng (đừng chép):** trường then chốt `parcels[].delivered_date` · bản ghi do máy quét ở điểm phát tạo ra, là nguồn
sự thật về ngày giao · lệch khi điểm phát quét sót hoặc nhập bù bằng tay.

---

<a id="b4"></a>

## B4 · Câu 2.4 · HAZOP vòng 1 trên tool của agent

*Chỉ làm MỘT vòng, trên MỘT tool. Đây là HAZOP vòng 1; HAZOP của thẻ sự cố viết riêng ở Phiếu C mục C4, không ghi đè bảng này.*

**Khung tư duy.** HAZOP không hỏi "cái gì có thể hỏng" một cách chung chung. Nó cầm từng **từ gợi ý** áp vào từng **dòng dữ
liệu đi vào một hành động** và hỏi: nếu dòng này lệch theo kiểu đó thì hậu quả là gì, ai chịu. Mục tiêu là tìm ra những nhánh
mà cả bàn chưa nghĩ tới, không phải tả lại nhánh đã biết.

| Guideword | Nghĩa khi áp vào một tool của agent |
|---|---|
| **WRONG** | Giá trị đưa vào có đủ, hợp lệ về hình thức, nhưng sai sự thật |
| **INVALID** | Giá trị không còn hiệu lực: hết hạn, sai phiên bản, sai đối tượng |
| **INCOMPLETE** | Thiếu một phần thông tin cần có để quyết định |
| **PERTURBED** | Đầu vào bị ai đó cố ý hoặc vô tình làm lệch (cài câu lệnh, gửi lặp) |
| **INCAPABLE** | Thành phần không trả lời được: quá tải, lỗi, hết quota |

**Câu hỏi dẫn dắt:** tool nào tạo ra hậu quả không đảo ngược? Mỗi tham số của tool đó lấy từ đâu (ticket, DB, model tự suy)?
Với mỗi guideword: hậu quả cho ai, hiện có gì ngăn, cần thêm gate ở tầng nào (phát hiện / chặn / giới hạn thiệt hại)?

Tool chọn phân tích: `________________` (gợi ý: `issue_refund`, `file_carrier_fault`, `notify_carrier`)

| Tham số / dòng dữ liệu | Guideword | Lệch cụ thể (viết bằng dữ kiện của lab) | Hậu quả, cho ai | Hiện có gì ngăn? | Gate đề xuất + tầng |
|---|---|---|---|---|---|
| | WRONG | | | | |
| | INVALID | | | | |
| | INCOMPLETE | | | | |
| | PERTURBED | | | | |
| | INCAPABLE | | | | |

Không bắt buộc điền đủ năm dòng. Bắt buộc: **ít nhất ba dòng, trong đó một dòng là nhánh bàn chưa thấy trên trace**.

**Mở rộng ra ngoài kỹ thuật (thêm ít nhất hai dòng):** "thành phần" không chỉ là model và tool. Áp cùng năm từ gợi ý vào:

| Thành phần ngoài code | Ví dụ câu hỏi |
|---|---|
| **Người duyệt** (vận hành) | INCAPABLE: chỉ một người trực mà 14 ca tới trong một giờ thì ca cuối chờ bao lâu? |
| **Ngân sách** (kinh doanh) | WRONG: tổng hoàn tự động trong ngày vượt mức Finance cho phép mà không ai được báo thì sao? |
| **Phạm vi pilot** (kinh doanh) | INVALID: có nhóm ticket nào trợ lý luôn phải chuyển người, tức là tự động hoá vô nghĩa? |
| **Dữ liệu gửi bên thứ ba** (pháp lý) | PERTURBED: chữ khách tự gõ có tên, số điện thoại người khác bị chép sang hãng thì ai chịu? |

| Thành phần | Guideword | Lệch cụ thể | Hậu quả, cho ai | Cổng đề xuất: code hay con số nào trong `config/operating_gates.json` |
|---|---|---|---|---|
| | | | | |
| | | | | |

**Ví dụ mẫu (`issue_refund`, đừng chép):** tham số `amount_vnd` · WRONG · số tiền tính từ số ngày khách tự khai · LogiX mất
tiền, hãng bị kéo theo một lỗi · hiện chỉ có trần "không vượt tổng tiền đơn" · cổng ghi so với quyền lợi tính từ DB (chặn).

---

<a id="b5"></a>

## B5 · Câu 2.4 · Checklist go-live 9 nhóm việc, lần 1

Checklist chín nhóm việc phải xong trước khi chạy thử thật. Bàn điền lần đầu ở đây, rồi cập nhật sau sự cố ở Phiếu C mục C11.
Cột "Bằng chứng lấy từ đâu" trỏ tới mục bàn đã điền ở bước khác; không điền thêm phiếu nào chỉ để lấp cột này.

Trạng thái: **Xong** (có bằng chứng) · **Chưa** · **Không áp dụng** (ghi lý do). Bằng chứng là **mã lần chạy**, tên file / mục phiếu, hoặc số trong report.
**Cột PIC bắt buộc:** mỗi dòng một người có tên (không ghi "cả bàn"). Dòng nào chưa có PIC thì coi như Chưa.

| # | Nhóm việc | Bằng chứng lấy từ đâu (đã có sẵn trong lab) | Mục cần kiểm tra | Trạng thái | Bằng chứng | PIC |
|---|---|---|---|---|---|---|
| 1 | Chất lượng | Report `lab10.eval` (mã lần chạy) + bảng soát lỗi (Phiếu B mục B2) | | | | |
| 2 | Dữ liệu | Bản đồ dữ liệu (Phiếu B mục B3, câu 2.3): trường nào là nguồn sự thật, trường nào là bản sao | | | | |
| 3 | Bảo mật | Một vòng HAZOP với guideword PERTURBED (Phiếu B mục B4): chữ nào đi vào model mà không do LogiX viết | | | | |
| 4 | Quyền hạn | `config/switches.json` + guard trước lệnh ghi; thẻ S2, S8 có thêm mục mức kiểm soát (Phiếu C mục C3) | | | | |
| 5 | Hiệu năng, hạ tầng | Đội tự ước tính; HAZOP guideword INCAPABLE: LLM không trả lời thì sao; số người duyệt và số ca mỗi giờ | | | | |
| 6 | Chi phí | Khối "kinh doanh và vận hành" của report: chi phí mỗi ticket so với làm tay, ROI, tiền LLM ticket đắt nhất; `config/operating_gates.json` mục `business` | | | | |
| 7 | Vận hành | Runbook (Phiếu B mục B7.5–B7.6) + `config/operating_gates.json` mục `operations` (PIC, người duyệt, số người trực, điều kiện dừng, kênh báo tin) + metric trong `monitors.py` | | | | |
| 8 | Con người, pháp lý | Bên thứ ba (hãng, tài xế, shop, người nhận quà, người đứng tên duyệt); `config/operating_gates.json` mục `legal`; thẻ S6, S7, S8 có mục riêng ở Phiếu C mục C3 | | | | |
| 9 | Quyết định | Câu tiêu chí (Phiếu A mục A4) + hash Bản tiêu chí đã ký + quyết định Gate 1 (Phiếu B mục B8, Phiếu C mục C12) | | | | |

Ô "Chưa" có rủi ro cao → chuyển thành một dòng Risk register (Phiếu C mục C10).

---

<a id="b6"></a>

## B6 · Câu 2.5 · Pre-mortem bốn lăng kính → cổng phòng ngừa (khoảng 8–10 phút, cả bàn)

*Mọi bàn làm pre-mortem ở vòng 1, TRƯỚC khi biết sự cố, để chọn 2–3 cổng phòng ngừa sẽ dựng. Ở vòng 2 bàn mở lại phần này ở
Phiếu C mục C1 (bút khác màu).*

**Khung tư duy.** Hỏi "có rủi ro gì không" thì ai cũng dè dặt. Nói "nó đã hỏng rồi, vì sao" thì mọi người được phép nói ra
điều mình vẫn lo. Làm im lặng trước, đọc sau, để ý kiến của người nói to không lấn át.

**Đề bài (đọc to):** *"Ba tháng sau pilot, LogiX phải tắt trợ lý hoàn tiền ở cả hai depot. Chuyện gì đã xảy ra?"*

1. **2 phút, im lặng:** mỗi người viết 2 lý do, mỗi lý do một dòng.
2. **2 phút:** đọc vòng tròn, mỗi lượt một lý do, không bình luận. Gộp lý do trùng.
3. **2 phút:** xếp từng lý do vào một **lăng kính**. Lăng kính nào còn trống thì cả bàn viết thêm ít nhất một lý do cho nó.
4. **2 phút:** chọn 2–3 lý do sẽ biến thành **cổng phòng ngừa** ngay hôm nay (code trong `guards.py` hoặc con số trong
   `config/operating_gates.json`). Lý do còn lại → Risk register.

Bốn lăng kính (bắt buộc đủ cả bốn; dự án AI hay chết ở ba lăng kính sau hơn là ở lăng kính đầu):

| Lăng kính | Câu hỏi gợi ý trên LogiX |
|---|---|
| **Kỹ thuật** | Model tin nhầm cái gì? Dữ liệu nào thiếu, cũ, lệch? Lệnh ghi nào không đảo ngược được? |
| **Kinh doanh** | Mỗi ticket tốn bao nhiêu so với làm tay? Một ngày hoàn tối đa bao nhiêu? Nhóm ticket nào không thể có lời? |
| **Con người và vận hành** | Ai duyệt, mấy người, mỗi giờ được mấy ca? Lượng việc tăng gấp ba thì sao? Nhân viên có tin trợ lý không? |
| **Pháp lý** | Dữ liệu cá nhân của ai rời hệ thống? Bên thứ ba nào bị ghi lỗi, bị trừ tiền mà không được hỏi? |

| Lý do thất bại (viết ở thì quá khứ) | Lăng kính | Kiểm được hôm nay? (trace / data / config nào) | Thành cổng phòng ngừa nào (code hay config) / hay vào risk register |
|---|---|---|---|
| | Kỹ thuật | | |
| Trợ lý đã tự hoàn quá 2.000.000 đồng trong một ngày, vượt ngân sách Finance, mà không chuyển người duyệt. | Kinh doanh (Vũ Quang Dũng) | `ops_limits.daily_auto_refund_budget_vnd` = 2.000.000; khối "kinh doanh và vận hành" của report so tổng hoàn tự động với trần. | Cổng config: `business.daily_refund_cap_vnd` = 2.000.000. Khoản làm vượt trần thì chuyển duyệt, không ghi tự động. |
| Pilot đã mở cả kho sỉ và nhóm ticket không có lời: chi phí mỗi ticket vẫn trên mức làm tay 10.000 đồng, hoặc ROI dưới 0,3. | Kinh doanh (Vũ Quang Dũng) | `ops_facts.manual_cost_per_ticket_vnd` = 10.000; `business_ops` đã ký (8.000 đồng/ticket, ROI 0,3); report theo kho. | Cổng config: `pilot_scope` chỉ HN và HCM; `cost_budget_per_ticket_vnd` = 1.500 (trần LLM); `roi_min` = 0,3. Kho sỉ để ngoài phạm vi cho tới khi có số đo. |
| | Con người và vận hành | | |
| | Pháp lý | | |

---

<a id="b7"></a>

## B7 · Khối 2B · Cổng phòng ngừa (phút 85–105)

### B7.1 · Câu 2.6 · 2–3 cổng phòng ngừa trong `lab10/guards.py`

Mỗi cổng ứng với một dòng pre-mortem (B6) hoặc một dòng HAZOP (B4). Viết trong `pre_guard(ctx)` (trước khi trợ lý đọc ticket)
hoặc `write_gate(ctx, action)` (trước mỗi lệnh ghi). Thử bằng:

```bash
python3 -m lab10.eval --suite base --stage after --note "cổng vòng 1: ..."
python3 -m unittest discover -s tests
```

| # | Cổng (hàm và nhánh, ví dụ `write_gate` khi `tool == "issue_refund"`) | Ứng với dòng nào ở B6 / B4 | Chặn điều gì, dựa vào nguồn sự thật nào | Mã lần chạy `base · after` | Ca đang đúng nào bị hỏng? (phải là "không") |
|---|---|---|---|---|---|
| 1 | | | | | |
| 2 | | | | | |
| 3 | | | | | |

### B7.2 · Câu 2.7 · Hai bước tránh rò rỉ dữ liệu

Bàn đang chỉnh cổng tới khi 22 ticket bộ nền xanh hết. Nêu 2 bước cụ thể để không "chỉnh trên chính bộ dùng để chấm"
(gắn với bộ nền, gói sự cố, bài kiểm tra ẩn):

1. …
2. …

### B7.3 · Câu 2.8 · Một behavioral test

- Tính chất (một câu): …

```bash
python3 -m lab10.trace --suite base --stage after --adhoc "..." --order O-10xx --customer C-xx
```

| Ticket hiểm | Nội dung ticket (`--adhoc`) | `--order` · `--customer` | Kết quả (dán dòng `SỔ CÁI` / `LỖI HÃNG` / `GỬI HÃNG`) | Tính chất giữ được? |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |

Giữ hai ticket này cho phần demo.

### B7.4 · Câu 2.9 · Cổng kinh doanh (`config/operating_gates.json` mục `business`)

Mỗi con số kèm một câu lý do, lấy từ `data/world.json` → `ops_limits`, `ops_facts`.

| Khoá | Giá trị bàn đặt | Lý do (một câu, có số) |
|---|---|---|
| `business.daily_refund_cap_vnd` | 2.000.000 đồng | `ops_limits.daily_auto_refund_budget_vnd` là 2.000.000 đồng: tổng hoàn tự động cả ngày không vượt ngân sách Finance. Khoản làm vượt trần thì chuyển người duyệt, không ghi tự động. |
| `business.cost_budget_per_ticket_vnd` | 1.500 đồng | Đây là trần tiền LLM mỗi ticket, lấy đúng `ops_limits.max_llm_cost_per_ticket_vnd` = 1.500 đồng. Không nhầm với `cost_per_ticket_vnd_max` = 8.000 đồng trong tiêu chí đã ký, vốn là tổng chi phí xử lý so với làm tay 10.000 đồng. |
| `business.pilot_scope` (all / warehouse / percent) | `warehouse`: HN, HCM | Đề bài đặt pilot tại 2 depot; chọn HN và HCM vì `warehouses` mô tả cả hai phục vụ đơn lẻ, khách cá nhân, chưa đưa kho sỉ HCM-B2B vào. Với 1 người duyệt mặc định, 6 ca/giờ và ca 480 phút trong `ops_facts`, công suất danh nghĩa là 48 lượt duyệt/ca; chưa có bằng chứng tải tại hai kho nằm trong mức này. Ticket ngoài phạm vi tiếp tục làm tay. Phải đo độ phủ, chi phí và hàng chờ trước khi chốt v1; không tự coi hai kho là phạm vi đã đạt. |
| `business.roi_min` | 0,3 | Khớp `business_ops.roi_min` đã ký. Làm tay tốn 10.000 đồng/ticket (`ops_facts.manual_cost_per_ticket_vnd`); ROI dưới 0,3 thì report báo vượt trần và chưa chọn Tiếp tục. |

### B7.5 · Câu 2.10 · Cổng con người, vận hành, pháp lý + Runbook phần 1–3

Điền `config/operating_gates.json` mục `operations` và `legal` (PIC, người duyệt, số người trực mỗi ca, công suất duyệt mỗi giờ,
thời gian chờ tối đa, điều kiện dừng, kênh báo tin; trường dữ liệu cá nhân không gửi cho bên thứ ba; ghi lỗi cho hãng phải có
nguyên nhân trong tracking). Rồi viết runbook dưới đây **khớp với các con số đó**.

*Runbook là tờ giấy người trực ca cầm lúc 23h khi có chuyện. Nó trả lời: nhìn con số nào, ngưỡng nào thì làm gì, ai được quyết.
Phần 1–3 và mục Giờ cao điểm viết ở vòng 1. Phần 4–5 viết ở vòng 2 (Phiếu C mục C11). Mọi con số phải khớp `config/operating_gates.json` và report.*
*Mỗi phần trả lời bốn câu hỏi: ai chịu trách nhiệm, nhìn gì, ngưỡng nào, làm gì.* **Người viết (vai Vận hành và pháp lý):** ______

#### Runbook 1 · Ai chịu trách nhiệm

| Vai | Tên / mã nhân viên (lấy từ `data/world.json` → `staff`) | Được quyền làm gì | Liên lạc qua kênh nào |
|---|---|---|---|
| PIC của trợ lý (một người) | | | |
| Người duyệt đứng tên các khoản vượt hạn mức | | | |
| Người giữ công tắc tắt từng thao tác ghi | | | |
| Người nhận khiếu nại của bên thứ ba (hãng, shop, người nhận quà) | | | |

Số người trực duyệt mỗi ca: ___ · Mỗi giờ duyệt được: ___ ca · Phạm vi pilot: ______ (tất cả / kho nào / bao nhiêu phần trăm)

#### Runbook 2 · Nhìn con số nào, ngưỡng nào thì làm gì

Mỗi dòng một tín hiệu. Cột "Lấy ở đâu" phải là một dòng trong report của `lab10.eval` / `lab10.grade` hoặc một chỉ số trong `lab10/monitors.py`.

| Tín hiệu | Lấy ở đâu | Bình thường | Ngưỡng VÀNG → việc làm | Ngưỡng ĐỎ → việc làm | Ai quyết |
|---|---|---|---|---|---|
| Thời gian chờ người duyệt lâu nhất | | | | | |
| Số ca bị ùn | | | | | |
| Chi phí mỗi ticket so với làm tay | | | | | |
| Tổng tiền hoàn tự động trong ngày so với trần | | | | | |
| Tiền hoàn sai | | | | | |
| Lỗi ghi oan cho hãng / lộ dữ liệu cá nhân (pháp lý) | | | | | |
| (tín hiệu riêng của bàn) | | | | | |

#### Runbook 3 · Điều kiện dừng và cách dừng

- Dừng một phần (tắt một thao tác ghi, thu hẹp phạm vi) khi: …
- Dừng hẳn khi: …
- Cách dừng, từng bước (công tắc nào trong `config/switches.json`, dòng nào trong `config/operating_gates.json`): …
- Từ tín hiệu đỏ đến lúc dừng xong tối đa ____ phút; người bấm: ____
- Khi đã dừng, ticket đang chờ đi đâu, ai xử lý: …
- Điều kiện để bật lại, ai ký: …

### B7.6 · Giờ cao điểm (bắt buộc với thẻ S4; các thẻ khác nên có)

Lượng ticket có thể dồn gấp ba trong một giờ (ngày sale, sau bão). Viết trước, khi chưa biết sự cố.

| Câu hỏi | Trả lời (có số, có tên) |
|---|---|
| Giờ cao điểm là khi nào, bao nhiêu ticket mỗi giờ (dựa vào `ops_facts`)? | |
| Ai trực giờ cao điểm, mấy người (khớp `operations.reviewers_on_shift`)? | |
| Ngưỡng nào thì **gọi thêm người** (hàng chờ bao nhiêu ca, chờ lâu nhất bao nhiêu phút)? Ai gọi? | |
| Ngưỡng nào thì **thu hẹp** phạm vi (khoá `business.pilot_scope`) hoặc **tắt** một thao tác ghi (`config/switches.json`)? Ai quyết? | |
| Thêm người thì chi phí mỗi ticket và ROI thay đổi thế nào (đọc report)? | |

---

<a id="b8"></a>

## B8 · Chốt cổng vòng 1 và quyết định Gate 1 · v1 (phút 105–115)

Làm đúng thứ tự:

```bash
python3 -m lab10.checkpoint
python3 -m lab10.eval --suite base --stage prepared
python3 -m lab10.gate --run runs/<mã lần chạy>/report.json
```

**Khung tư duy.** Gate 1 "đạt" khi **quyết định khớp bằng chứng và khớp tiêu chí đã ký trước**. Tiếp tục, Thu hẹp, Cải tiến
thêm, Dừng đều có thể là quyết định đạt. Quyết định không đạt là quyết định mà con số trong report không đỡ được.
Chỉ chọn Tiếp tục khi mọi chỉ số bắt buộc đều đạt.

Ba câu tự vấn trước khi viết: (1) Rủi ro còn lại có chấp nhận được như hiện trạng không? (2) Cần thêm biện pháp nào, tốn
bao nhiêu thời gian? (3) Có phần nào của dự án không nên làm tiếp?

| | **v1** (phút 105–115, TRƯỚC khi nhận thẻ sự cố) |
|---|---|
| Commit ký tiêu chí (message `Sign acceptance criteria`; hash commit, tuỳ chọn) | |
| Hash chốt cổng vòng 1 (8 ký tự lệnh `lab10.checkpoint` in ra, tuỳ chọn) | |
| Mã lần chạy dùng làm bằng chứng | bộ nền, mốc base: ________ · bộ nền với cổng vòng 1 (prepared): ________ |
| Còn dòng "vượt trần" nào trong report? (hàng chờ, chi phí, ROI, trần tiền, pháp lý) | |
| Kho hoặc hãng có số xấu nhất: ____. Nếu chỉ nhìn phân khúc này, quyết định có đổi không? *(Đọc khối "theo kho và hãng" ở cuối output `lab10.eval` / `lab10.grade`, hoặc mục `by_segment` trong `report.json`.)* | |
| Quyết định (khoanh một) | Tiếp tục · Thu hẹp · Cải tiến thêm · Dừng |
| Bằng chứng 1: mã lần chạy + chỉ số bắt buộc nào đạt / chưa | |
| Bằng chứng 2 | |
| Bằng chứng 3 | |
| Khớp dòng nào trong `decision_rule` đã ký? | |
| Nếu Thu hẹp: cắt phần nào, vì sao | |
| Nếu Cải tiến thêm: giả thuyết cụ thể + hạn | |
| Nếu Dừng: bài học ghi lại | |
| Một bằng chứng còn thiếu (thứ bộ nền chưa đo được) | |
| Ngày quyết định lại (trừ khi Dừng) | |
| PIC ký | |

Xong v1 thì lưu và đẩy một bản (sau mốc này không sửa cột v1):

```bash
git add lab10/guards.py lab10/guards_round1.py config/operating_gates.json config/operating_gates.round1.json config/round1.lock templates/form-b-evaluation-gates.md
git commit -m "LAB 10: chốt cổng vòng 1, quyết định v1"
git push -u origin main
```
