# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): **4mems** · Lớp L3B · repo `K5-L3B-DAY13-4mems-LaunchEconomics`
- Nhóm được chấm: **teamrandom** · Lớp L3B · repo `K5-L3B-DAY13-teamrandom-LaunchEconomics`
- Buổi duyệt chéo Gate 2a: **2026-11-25**, khung **17:00 – 17:45** theo lịch trong `README.md`

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất Go có điều kiện khớp với số của chính nhóm: trong phạm vi `noi_dia` + `hang_nang` là 3.414 đ/việc thành công, cộng chi phí cố định 4.599 đ = 0,38× mốc 12.000 đ. Nhóm **tự nêu hai con số bất lợi kèm cách xử lý**: (1) xem lại 100% trong phạm vi đẩy chi phí lên 11.743 đ = 0,98× hoặc 12.415 đ = 1,03× tuỳ số phút làm lại, xử lý bằng giảm xem lại theo bậc với mục tiêu ≤ 4,8 phút/lần; (2) power chỉ 0,64 nếu tác động thật là 5 điểm, xử lý bằng việc Giám đốc vận hành ký chấp nhận mức chênh 6 điểm, kiểm tra 2026-12-04. Hồ sơ cũng ghi rõ đợt chạy thử **không có đối chứng nên chưa nói được tác động**, và ghi "phương án đề xuất, chưa có phê duyệt của doanh nghiệp" — không viết như thể trợ lý đã được duyệt chạy. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Nhãn `[simulated]` có ở mọi con số tính từ cột `_simulated` (mục 1, 2, 3, 7 của hồ sơ, bảng A2–A4 và B1–B4 trong `bang_chi_phi.md`); `pilot_plan.yaml` còn liệt kê 5 dòng `simulated_inputs` nêu đúng tên cột `phut_xem_lai_simulated` (890 phút) và `phut_lam_lai_simulated` (1.132 phút). Ba chỉ số E1 không mang nhãn là **đúng**, vì tính từ `dong_trong_24h` và `mo_lai_trong_7_ngay`, không phải cột `_simulated`. Phạm vi **không** ghi "mọi yêu cầu": giới hạn `noi_dia` + `hang_nang`, mỗi nhóm bị loại đều có số làm lý do — `quoc_te` 1,88× và thành công chỉ 27,3% (chạy lại không giúp: ok lần 1 là 30,0%, lần 3 chỉ 2,2%), `doi_tac` 0,85× dù rẻ hơn mốc vẫn loại vì có điều khoản riêng. Hồ sơ không dùng từ bị cấm ở quy tắc 5 của README (lệnh grep của đề bài không in gì). |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | **Tách được tác động:** có đối chứng song song 20 nhân viên cùng tuần cùng depot, chia ngẫu nhiên phân tầng theo depot bằng code có seed ghi trước; rủi ro lan được nêu và giảm bằng quyền truy cập theo tài khoản + log theo `staff_id`; đăng ký trước chỉ số chính, MDE, luật dừng, điều kiện kết thúc và ngày quyết định. **Đủ mẫu:** chia theo nhân viên, 20 cụm mỗi nhóm, m ≥ 299, DE 6,96, `n_per_arm` 859 hiệu dụng = 5.980 yêu cầu thực tế mỗi nhóm — hội đồng tính lại ra 855,5 cho nền 0,70 và MDE 0,06, lệch dưới 2% nên nhận. Nhóm nói thẳng trần mẫu hiệu dụng không đủ cho 5 điểm thay vì hứa suông. **Luật dừng:** 4 luật, luật nào cũng đủ 4 vế và có cả ba thứ — ngưỡng (1 ca hoàn trùng · ≥ 2 điểm hoặc 6% · 8.000 đ · 40%), thời hạn (bất kỳ ngày nào · 3 ngày liên tiếp · 2 tuần liên tiếp · 1 tuần) và người có quyền dừng là một vai trò cụ thể (Giám đốc vận hành · PM trợ lý hoàn phí · Trưởng nhóm CSKH), không dùng cách ghi tập thể mà rúbric cấm. `interim_looks` chỉ xem chỉ số an toàn hằng ngày, không xem chênh lệch chỉ số chính trước ngày quyết định; `rollback` có hiệu lực trong 30 phút về luồng nhân viên tự làm. |
| **Tổng** | | | | **30 / 30** | Ba tiêu chí đều đạt mô tả của mức 10 điểm. |

**Quyết định của hội đồng:** ~~Go~~ · **Go có điều kiện** · ~~No-go~~

**Lý do:** Hồ sơ đủ bằng chứng để ra quyết định và không có chỗ nào mâu thuẫn với số của chính nhóm. Chi phí rẻ hơn mốc thủ công ở mọi cách khoanh phạm vi mà nhóm công bố (3.414 đ trong phạm vi; 4.599 đ = 0,38× khi cộng chi phí cố định; 5.865 đ = 0,49× khi tính cả 222 ca × 12.000 đ nhân viên làm thay), và kế hoạch pilot có đối chứng, có cỡ mẫu tính được, có 4 luật dừng dừng được thật. Hội đồng giữ mức **có điều kiện** chứ không Go thẳng vì hai lý do lấy từ chính hồ sơ: (1) kịch bản xem lại 100% đưa chi phí lên 0,98×–1,03×, tức sát hoặc vượt mốc thủ công, nên điều kiện giảm xem lại theo bậc phải được kiểm trước khi sang bước 0,50; (2) ngưỡng chi phí 8.000 đ của luật dừng 3 đặt trên số **gộp** cả phạm vi, trong khi `hang_nang` đứng riêng đã là 8.221 đ — xem câu hỏi bên dưới. Ngoài ra Gate 2a chỉ duyệt kế hoạch pilot, và nhóm đã viết đúng như vậy.

**Một câu hỏi cho đội trình:** Luật dừng 3 đặt ngưỡng **8.000 đ/việc thành công tính trên cả phạm vi**, nhưng bảng A3 của nhóm cho thấy `noi_dia` là 2.696 đ (0,22×) còn `hang_nang` đã là **8.221 đ (0,69×)** — tự nó đã vượt ngưỡng, chỉ vì `noi_dia` chiếm 824 trong 982 yêu cầu nên số gộp mới xuống 3.414 đ. Nghĩa là nếu `hang_nang` xấu đi trong pilot, trung bình gộp vẫn đứng dưới 8.000 đ và luật dừng 3 sẽ không kích hoạt — trong khi biện pháp của chính luật dừng 3 lại là "thu hẹp về `noi_dia`". Nhóm có theo dõi chi phí **tách riêng theo `loai`**, hay đặt thêm ngưỡng riêng cho `hang_nang` không? Nếu không, luật dừng 3 phát hiện được tình huống nào trong thực tế?

**Câu trả lời của đội trình (ghi lại tại buổi):**

> *Ô này ghi nguyên văn lời đội trình trả lời tại buổi duyệt chéo, không viết trước. Ghi đủ ba thứ: (a) họ có theo dõi chi phí tách riêng theo `loai` hay không; (b) con số hoặc tên trường họ dẫn ra làm căn cứ; (c) họ có nhận đây là chỗ cần sửa hay không. Nếu họ không trả lời được thì ghi đúng như vậy — điểm ở ba dòng trên không đổi, vì rúbric chấm hồ sơ chứ không chấm câu trả lời.*

- Người trả lời (tên, vai trong nhóm teamrandom): 
- Nội dung trả lời: 
- Hội đồng đánh giá câu trả lời (thỏa đáng / chưa thỏa đáng, một câu lý do): 

---

## Ghi chú của hội đồng (không tính điểm, gửi kèm cho nhóm được chấm)

Một điểm hội đồng ghi lại để nhóm tham khảo, không trừ điểm:

1. **Đồng thuận nhãn 17/20 = 85%.** Đạt mốc 80% và trên mốc tự kiểm 16/20. Hồ sơ nên ghi thêm **một câu quy tắc phân biệt** cho ba ca lệch nhãn, vì CP3 yêu cầu "với ca không trùng, thống nhất nhãn và ghi một câu quy tắc phân biệt" — `bang_loi.md` đã có nhãn thống nhất, chỉ thiếu câu quy tắc.

**Điểm mạnh hội đồng muốn ghi nhận:** luật dừng 1 (một ca hoàn trùng đã đối soát là tắt trợ lý trong 30 phút) là luật dừng chặt nhất hội đồng thấy, và việc phân biệt rõ "4,8 phút là mục tiêu thiết kế, 5 phút là mức phải hành động" trong mục rollout cho thấy nhóm hiểu khác nhau giữa ngưỡng cảnh báo và mục tiêu vận hành.

---

---

## Phụ lục · Phiếu 4mems NHẬN ĐƯỢC từ hội đồng teamrandom

> Phần này **không phải** phiếu 4mems chấm — phần 4mems chấm teamrandom nằm ở trên. Đây là bản ghi nhận điểm mà **teamrandom chấm 4mems**, sao lại từ `report/team/phieu_cham.md` trong repo `K5-L3B-DAY13-teamrandom-LaunchEconomics`, để hai chiều duyệt chéo nằm cạnh nhau cho dễ đối chiếu. Bản gốc do teamrandom giữ.

- Hội đồng: **teamrandom** · L3B
- Nhóm được chấm: **4mems** · commit được chấm `18cc364`
- Kết quả: **30 / 30** · Quyết định: **Go có điều kiện**

| Tiêu chí | Điểm | Điểm họ yêu cầu sửa |
| --- | ---: | --- |
| Đề xuất khớp bằng chứng | 10 | Điều kiện 3 ghi “859 yêu cầu mỗi nhóm” trong khi `pilot_plan.yaml` ghi ≥ 5.980 yêu cầu thực tế; 859 là mẫu hiệu dụng. |
| Số giả lập và phạm vi | 10 | Mục 6 của hồ sơ thiếu nhãn `simulated` ở hai số 1,88× và 0,85×. |
| Pilot ra được quyết định | 10 | Luật dừng 1 gộp ca hoàn trùng vào vế “TRONG 3 ngày liên tiếp” thay vì dừng ngay khi có 1 ca; `interim_looks` còn là câu mẫu. |

**Câu hỏi teamrandom đặt cho 4mems:** Ngưỡng ra quyết định thật là 859 hay 5.980 yêu cầu mỗi nhóm, và với 2 tuần ở bước 0,50 cộng 7 ngày theo dõi mở lại thì có đủ dữ liệu trước 2027-01-12 không?

**4mems trả lời (ghi tại buổi):**

---

*Hội đồng: nhóm 4mems. Người điền: Trần Hải Long (2A202603891), đối chiếu số với Trần Minh Đức (2A202603977). Mọi con số dẫn trong phiếu lấy từ `report/team/` của nhóm teamrandom; hội đồng tính lại cỡ mẫu bằng công thức hai tỉ lệ với alpha 0,05 và power 0,80 để đối chiếu.*
