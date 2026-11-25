# Kế hoạch phản biện Gate 2a — nhóm 4mems

Dùng khi tranh luận kiến thức với nhóm khác. Khác với [gate2a_slides.html](gate2a_slides.html): slide là để **trình**, file này là để **đánh và đỡ**.

**Luật chơi cần nhớ trước khi mở miệng.** Hội đồng chấm theo bằng chứng, không theo cách trình bày. Một đề xuất **No-go có lý do bằng số** được điểm cao hơn một **Go bỏ qua con số bất lợi**. Nghĩa là: tấn công vào *chỗ nhóm kia thiếu số*, không tấn công vào *kết luận họ chọn*. Một nhóm chọn No-go không sai; một nhóm chọn Go mà không biết con số bất lợi của chính mình thì sai.

**Nguyên tắc tự ràng buộc.** Không bịa số để thắng. Nếu nhóm kia chứng minh chúng ta sai, nhận ngay bằng một câu: *"Đúng, số đó chúng tôi tính thiếu phần X. Con số đúng là Y."* Nhận sai nhanh mất ít điểm hơn là bảo vệ một con số sai, vì giảng viên sẽ hỏi lại cách tính.

---

## 1. Năm trụ kiến thức

Mỗi trụ gồm: luận điểm cốt lõi → cơ chế đằng sau → câu hỏi tấn công → cách đỡ khi bị hỏi lại.

### Trụ 1 · Chi phí mỗi việc thành công (cost-of-pass)

**Luận điểm.** Hoá đơn token không phải chi phí. Chi phí là `(token + tool + xem lại + làm lại) ÷ số việc thành công`, trong đó **tử số cộng mọi lần chạy kể cả lần lỗi**, **mẫu số chỉ đếm việc thực sự xong**.

**Cơ chế.** Hai bất đối xứng. (a) Tiền tiêu cho lần chạy lỗi vẫn là tiền thật nhưng không tạo ra kết quả dùng được, nên nó phải ở tử số mà không được ở mẫu số. (b) Mẫu số chọn sai sẽ pha loãng phần hỏng: chia 4.373.585 đ cho 1.200 ra 3.645 đ, chia cho 978 ra 4.472 đ. Cùng một dữ liệu, chênh 23%.

**Hệ quả toán học quan trọng.** Với xác suất đúng `p` mỗi lần và tối đa `k` lần:

```
E[số lần chạy] = (1 − (1 − p)^k) / p      P(thành công) = 1 − (1 − p)^k
hệ số chi phí mỗi việc thành công = E[số lần chạy] / P(thành công) = 1/p
```

Cụm `1 − (1 − p)^k` triệt tiêu, nên **hệ số luôn bằng `1/p` bất kể `k`**. Trong mô hình, giới hạn số lần chạy **không** làm chi phí mỗi việc thành công thay đổi: nó cắt số lần chạy nhưng cắt tỉ lệ thành công đúng theo cùng tỉ lệ.

**Câu hỏi tấn công nhóm khác:**
- "Mẫu số của các bạn là bao nhiêu — 1.200 hay số việc thành công?" → nếu họ dùng 1.200, con số của họ thấp giả tạo.
- "Các bạn có cộng token của lần chạy lỗi không?" → nếu không, chi phí thiếu khoảng 93.804 đ phần lần chạy thứ 2 và 3.
- "Hệ số chi phí mỗi việc thành công phụ thuộc `k` thế nào?" → đáp án đúng: **không phụ thuộc**, bằng `1/p`. Ai trả lời "giảm khi giới hạn `k`" là chưa rút gọn công thức.

**Bị hỏi lại thì đỡ thế nào.** Nếu họ hỏi "vậy giới hạn số lần chạy vô ích?" → không: mô hình giả định `p` **không đổi** giữa các lần, còn dữ liệu thật phá giả định đó. Với `quoc_te`, lần 1 đúng 30,0%, lần 2 chỉ 11,4%, lần 3 chỉ 2,2% — lỗi lặp lại trên cùng yêu cầu. Đó là lý do phải đo theo `attempt`, không tin công thức.

---

### Trụ 2 · So sánh công bằng và chi phí cả hệ thống

**Luận điểm.** Không được so chi phí của trợ lý với nhân viên bằng cách chỉ chia cho phần việc trợ lý làm xong. Phải tính cả phần việc nó **không** làm được, vì phần đó nhân viên vẫn phải làm.

**Cơ chế.** `4.472 ÷ 12.000 = 0,37×` là so sánh lệch: nó bỏ qua 222 yêu cầu không thành công (148 `chuyen_nhan_vien` + 74 `lam_lai`). Con số công bằng là chi phí cả hệ thống:

```
(4.373.585 + 222 × 12.000) ÷ 1.200 = 5.865 đ/yêu cầu = 0,49×
```

Hai mẫu số khác nhau cho hai câu hỏi khác nhau: **chi phí mỗi việc thành công** trả lời "trợ lý làm một việc tốn bao nhiêu", **chi phí cả hệ thống trên mỗi yêu cầu** trả lời "công ty tốn bao nhiêu cho một yêu cầu". Lẫn hai cái là lỗi lập luận, không phải lỗi tính.

**Chi phí cố định.** 40 triệu đ/tháng chia cho số việc thành công, nên nó phụ thuộc khối lượng: 1.185 đ/việc ở 45.000 yêu cầu/tháng, nhưng 2.370 đ/việc nếu khối lượng còn một nửa. Kết luận "rẻ hơn" chỉ đúng **ở một mức khối lượng cụ thể**.

**Câu hỏi tấn công:**
- "Con số so với 12.000 đ của các bạn đã tính phần nhân viên làm thay chưa?" → câu hỏi đáng giá nhất của cả phiên, vì rất nhiều nhóm dùng 0,37×.
- "Con số đó đã cộng chi phí cố định chưa, và ở khối lượng nào?" → nếu họ không trả lời được "ở khối lượng nào", kết luận của họ không có điều kiện áp dụng.
- "Nếu khối lượng pilot chỉ bằng một nửa dự kiến, con số của các bạn thành bao nhiêu?"

**Bị hỏi lại.** Nếu họ nói "0,49× và 0,43× của các bạn mâu thuẫn" → không mâu thuẫn, **khác phạm vi**: 0,49× là toàn mẫu 1.200 yêu cầu, 0,43× là trong phạm vi pilot 982 yêu cầu và đã cộng chi phí cố định. Mỗi con số có mẫu số và phạm vi ghi kèm trong hồ sơ.

---

### Trụ 3 · Độ nhạy, cộng tuyến tính và cái bẫy tối ưu cục bộ

**Luận điểm.** Yếu tố cần theo dõi là yếu tố làm chi phí thay đổi nhiều nhất, không phải yếu tố dễ nhìn nhất. Ở đây là **số ca làm lại** (±51,8%), không phải giá token (±5,6%).

**Cơ chế cộng tuyến tính.** Mô hình cộng bốn khoản độc lập, không có số hạng nhân chéo, nên tác động của một cặp bằng tổng hai tác động riêng: giá token gấp đôi (+5,6%) cùng xem lại gấp đôi (+40,7%) cho đúng **+46,3%**. Đây là một **phép kiểm tra tính đúng đắn**: nếu cặp không bằng tổng, hoặc code sai, hoặc mô hình có tương tác mà nhóm chưa khai.

**Phép kiểm đối xứng.** Mỗi kịch bản "giảm một nửa" phải làm chi phí giảm **đúng bằng nửa** mức tăng của kịch bản "gấp đôi": 5,6 ↔ 2,8 · 40,7 ↔ 20,3 · 51,8 ↔ 25,9. Lệch là code sai.

**Bẫy tối ưu cục bộ (Goodhart).** Siết còn 1 lần chạy cho chi phí mỗi việc thành công **thấp nhất** (4.111 đ) nhưng làm cả hệ thống **đắt hơn**: 7.449.781 đ so với 6.901.220 đ ở giới hạn 2 lần, vì đẩy thêm 85 việc sang nhân viên. Tối ưu chỉ số của trợ lý không đồng nghĩa tối ưu chi phí của công ty.

**Câu hỏi tấn công:**
- "Yếu tố nhạy nhất của các bạn là gì, và các bạn kiểm bằng cách nào?" → nếu họ trả lời "giá token", họ chưa tính giờ nhân viên.
- "Kịch bản gấp đôi và giảm một nửa của các bạn có đối xứng không?" → câu hỏi phát hiện lỗi code mà không cần đọc code.
- "Giới hạn số lần chạy rẻ nhất cho **công ty** có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không?" → đáp án đúng: **không trùng**. Ai trả lời "trùng" là chưa tính chi phí cả hệ thống.

---

### Trụ 4 · Phân loại lỗi và tính đo được

**Luận điểm.** Gắn nhãn theo **nguyên nhân gốc**, không theo **chỗ cần sửa**. Và mỗi cách khắc phục phải có cách phát hiện **đo được**: tên event + ngưỡng + tần suất.

**Cơ chế phân biệt.** Năm loại PAIR, và ranh giới hay bị nhầm nhất là **Hệ thống** vs **Ngầm**: tiêu chí là *"có ai thấy được hay không"*, không phải *"số tiền có đúng hay không"*.

| Tình huống | Nhãn đúng | Vì sao |
| --- | --- | --- |
| Khách nhập sai mã, trợ lý không gợi ý sửa | Do người dùng | Nguyên nhân gốc là đầu vào sai. Việc trợ lý không gợi ý nằm ở **cột khắc phục** |
| Trợ lý trích dẫn điều khoản bịa, nhân viên bắt được | Hệ thống | Sai **đã lộ ra** |
| Chi phí gấp 3 suốt 3 tuần, không ai thấy | Ngầm | Chỉ phát hiện qua kiểm tra mẫu. "Sai" có thể là sai **chi phí**, không chỉ sai câu trả lời |
| Ngoài phạm vi, trợ lý xử lý kém | Giới hạn hệ thống | Ngoài phạm vi thì là giới hạn, kể cả khi xử lý giới hạn đó tệ |
| Số tiền đúng chính sách, khách hiểu sai cách tính | Ngữ cảnh | Kết quả đúng, chỉ giả định về hoàn cảnh là sai |

**Điểm lập luận tinh tế — đồng thuận cao chứng minh gì?** Nó chứng minh **định nghĩa đủ rõ để hai người áp dụng giống nhau**, chứ không chứng minh nhãn đúng. Đồng thuận 100% với định nghĩa sai vẫn là 100%. Vì vậy phải có **cả hai**: tỉ lệ đồng thuận ≥ 80% **và** khớp đáp án ≥ 16/20.

**Câu hỏi tấn công:**
- "Ca trích dẫn điều khoản bịa mà nhân viên bắt được, các bạn xếp Hệ thống hay Ngầm?" → đáp án: **Hệ thống**. Ai trả lời Ngầm là dùng tiêu chí "số tiền có đúng không" thay vì "có ai thấy không".
- "Hai bộ nhãn của các bạn gắn trước hay sau khi bàn với nhau?" → nếu có dấu hiệu bàn trước, toàn bộ bằng chứng mất giá trị.
- "Dòng khắc phục này phát hiện bằng event nào, ngưỡng bao nhiêu, kiểm bao lâu một lần?" → nếu họ trả lời chung chung kiểu "theo dõi thường xuyên" thì chưa đo được.
- "Ai phụ trách dòng này?" → nếu là "cả đội" hoặc tên một người cụ thể thay vì **vai trò có quyền quyết định**, đó là lỗi theo rubric.

---

### Trụ 5 · Nhân quả, cụm và cỡ mẫu — trụ nhiều điểm nhất

**Luận điểm.** Đợt chạy thử **không** cho kết luận nhân quả, vì không có nhóm đối chứng. Chỉ được nói *"chỉ số trong đợt chạy thử là 82,83%"*, không được nói *"trợ lý đã nâng chỉ số từ 0,70"*.

**Cơ chế cụm.** Khi chia theo cụm (nhân viên, depot), các yêu cầu trong cùng cụm tương quan với nhau, nên mỗi quan sát thêm mang ít thông tin mới hơn:

```
Hệ số thiết kế  DE = 1 + (m − 1) × ICC
Cỡ mẫu hiệu dụng = c × m / DE  <  c / ICC
```

với `c` là số cụm, `m` là số yêu cầu mỗi cụm. **Bất đẳng thức bên phải là chìa khoá của cả nhiệm vụ D**: dù `m` lớn bao nhiêu, cỡ mẫu hiệu dụng cũng không vượt `c / ICC`. **Số cụm quyết định, không phải tổng số yêu cầu.**

Với ICC = 0,02: 20 nhân viên mỗi nhóm → trần **1.000**; 6 depot mỗi nhóm → trần **300**. Trong khi mức chênh 5 điểm cần **1.251** mỗi nhóm. Vậy *không cách chia theo cụm nào đủ mẫu* — thêm yêu cầu cho cùng một người gần như vô dụng.

**Đánh đổi chỉ có ba hướng, không có hướng thứ tư:** tăng số cụm (không có, chỉ 40 nhân viên) · nâng mức chênh cần phát hiện (nhóm chọn 6 điểm, n = 859, DE 6,96) · hoặc chấp nhận power thấp. Nhóm chọn hướng hai và khai power còn **0,64** ở mức 5 điểm.

**Vì sao không chia theo yêu cầu dù đủ mẫu (1.251, DE = 1).** Cùng một nhân viên vừa dùng vừa không dùng trợ lý → học được từ gợi ý rồi áp dụng cả cho ca đối chứng → **tràn tác động**. Đủ mẫu nhưng đo sai thứ.

**Vì sao `interim_looks` chỉ kiểm chỉ số an toàn.** Nhìn chỉ số chính nhiều lần giữa đường rồi dừng khi thấy đẹp sẽ **đẩy alpha thật lên trên 0,05** — tự tạo kết quả dương tính giả. Chỉ số an toàn thì buộc phải nhìn liên tục, vì nó bảo vệ khách, không dùng để kết luận.

**Câu hỏi tấn công (mạnh nhất của cả phiên):**
- "Các bạn có **bao nhiêu cụm** mỗi nhóm?" → dưới 20 là thiết kế yếu, dù họ báo tổng số yêu cầu rất lớn.
- "Trần cỡ mẫu hiệu dụng của cách chia các bạn chọn là bao nhiêu?" → nếu họ không biết khái niệm `c / ICC`, họ chưa tính trần, chỉ nhân `n × DE`.
- "Các bạn chia theo depot vì nó dễ triển khai hay vì nó đủ mẫu?" → chia theo depot cho trần 300, chỉ 6 cụm. Đây là lỗi hay gặp nhất.
- "Mức chênh các bạn khai là 5 điểm nhưng `n` các bạn ghi là bao nhiêu?" → nếu `n = 859` mà `mde = 0,05` thì file tự mâu thuẫn; 859 là cỡ mẫu cho 6 điểm.
- "Nếu tác động thật nhỏ hơn mức các bạn thiết kế, power còn bao nhiêu?" → nhóm nào không trả lời được là chưa hiểu đánh đổi mình vừa chọn.
- "Ngưỡng an toàn của các bạn so với **tỉ lệ nền hiện tại** thì thế nào?" → nếu ngưỡng tuyệt đối thấp hơn nền (ví dụ 3% khi nền là 3,97%), pilot của họ dừng ngay tuần đầu dù trợ lý không làm gì sai.

---

## 2. Sáu lỗi lập luận — cần bắt ở nhóm khác và tránh ở nhóm mình

| Lỗi | Dấu hiệu nhận ra | Câu hỏi vạch ra |
| --- | --- | --- |
| **Lẫn mẫu số** | Dùng một con số cho cả hai câu "mỗi việc xong" và "mỗi yêu cầu" | "Con số này chia cho bao nhiêu, và bao nhiêu đó là gì?" |
| **Tối ưu cục bộ (Goodhart)** | Siết tham số để chỉ số đẹp, không tính phần đẩy sang người | "Cả hệ thống tốn bao nhiêu ở cấu hình đó?" |
| **Nhân quả từ dữ liệu không đối chứng** | Dùng chữ "đã nâng", "đã cải thiện" cho đợt chạy thử | "Nhóm đối chứng của đợt chạy thử là ai?" |
| **Ngưỡng không có nền** | Luật dừng có số tròn (3%, 5%) mà không nhắc tỉ lệ hiện tại | "Tỉ lệ hiện tại của chỉ số đó là bao nhiêu?" |
| **Nhiều yêu cầu, ít cụm** | Tự hào vì tổng số yêu cầu lớn | "Bao nhiêu cụm mỗi nhóm? Trần `c / ICC` là bao nhiêu?" |
| **Chỉ số không đo được** | Chỉ số hay nhưng không có event nào tính ra nó | "Chỉ số này tính từ event nào trong danh sách của các bạn?" |

---

## 3. Phân vai khi tranh luận

| Người | Đánh vào trụ | Mang theo con số |
| --- | --- | --- |
**Đức** | Trụ 1 và 3 · mẫu số, cộng tuyến tính, tối ưu cục bộ | 4.472 · 274,7 · 16,3× · 548.561 đ chênh ở B3 |
**Nhài** | Trụ 5 · cụm, DE, trần `c / ICC`, power | 1.251 · 1.000 · 300 · 859 · DE 6,96 · power 0,64 |
**Hải** | Trụ 4 · PAIR, lộ ra vs ngầm, tính đo được | 20/20 · 5 loại · ngưỡng 2%/ngày, 1%/tuần |
**Long** | Trụ 2 · so sánh công bằng, phạm vi, ngưỡng có nền | 0,49× · 0,43× · nền 3,97% và 4,89% · trần 6% |

**Thứ tự phát biểu khi phản biện:** Nhài hỏi trước (câu về cụm mạnh nhất và khó đỡ nhất) → Long hỏi tiếp về con số so sánh → Hải hỏi về tính đo được → Đức chốt. Mỗi người **một câu**, không ai hỏi chen.

---

## 4. Bốn mẫu câu khi bị tấn công

1. **Khi họ nêu một con số bất lợi của ta.** *"Đúng, con số đó là X. Chúng tôi đã ghi nó trong hồ sơ ở mục Y, và cách xử lý là Z."* — nếu con số đó đã nằm trong hồ sơ thì đòn tấn công trở thành điểm cộng cho ta ở tiêu chí C6.
2. **Khi họ nói thiết kế của ta chưa đủ mẫu.** *"Đúng, và chúng tôi nói rõ điều đó: trần là 1.000 so với 1.251 cần thiết. Đây là đánh đổi có ý thức, không phải thiếu sót — chúng tôi nâng mức chênh lên 6 điểm và khai power còn 0,64."*
3. **Khi họ hỏi một con số ta chưa tính.** *"Số đó chúng tôi chưa tính. Chúng tôi có X, và sẽ tính Y trước ngày quyết định."* — không đoán.
4. **Khi họ đúng và ta sai.** *"Đúng, chúng tôi tính thiếu phần đó. Con số đúng là Y."* — rồi dừng, không giải thích dài.

**Ba câu không được nói:** "cả đội chịu trách nhiệm" · "trợ lý đã nâng chỉ số" · bất kỳ câu nào có từ "production", vì Gate 2a chỉ duyệt kế hoạch pilot.

---

## 5. Bảng tra nhanh

| Khái niệm | Công thức | Số của nhóm |
| --- | --- | --- |
Chi phí mỗi việc thành công | (token + tool + xem lại + làm lại) ÷ số việc thành công | 4.472 đ · mẫu số 978 |
Hệ số chi phí theo `p` | `E[N] / P(thành công) = 1/p` | p = 0,8 → 1,25 |
Số lần chạy trung bình | `(1 − (1 − p)^k) / p` | p = 0,8; k = 2 → 1,20 |
Chi phí cả hệ thống | chi phí trợ lý + 12.000 × số yêu cầu không thành công | 7.037.585 đ · 0,49× mỗi yêu cầu |
Chi phí cố định mỗi việc | cố định tháng ÷ số việc thành công tháng | 40 tr ÷ 33.750 = 1.185 đ |
Cỡ mẫu so hai tỉ lệ | `(z₁₋α/₂√(2p̄(1−p̄)) + z₁₋β√(p₁(1−p₁)+p₂(1−p₂)))² / (p₂−p₁)²` | 5 điểm → 1.251 · 6 điểm → 859 |
Hệ số thiết kế | `DE = 1 + (m − 1) × ICC` | m = 299; ICC 0,02 → 6,96 |
Trần cỡ mẫu hiệu dụng | `c × m / DE < c / ICC` | 20 cụm → 1.000 · 6 cụm → 300 |

Tất cả con số dẫn từ hai cột `_simulated` đều phải đọc kèm nhãn **simulated**.
