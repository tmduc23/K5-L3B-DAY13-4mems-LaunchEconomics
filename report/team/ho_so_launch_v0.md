# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi tên tập thể. Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: 4mems · Lớp: L3B

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | **4.472 đ/việc thành công** trên toàn mẫu A2 (4.373.585 đ ÷ 978 việc thành công, chưa cộng chi phí cố định) [simulated]. | Giả lập | PM trợ lý hoàn phí |
| 2 · Ba yếu tố nhạy nhất | Chi phí mỗi việc thành công tăng **51,8%** khi số ca làm lại gấp đôi, **40,7%** khi tỉ lệ xem lại gấp đôi và **23,1%** khi lương tăng 25% [simulated, B1–B2]. | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | Với `noi_dia` + `hang_nang` ở quy mô 45.000 yêu cầu/tháng toàn hệ thống, chi phí **5.217 đ/yêu cầu = 0,43×** mốc 12.000 đ, đã gồm chi phí cố định và nhân viên xử lý 82/982 ca không thành công [simulated, A4]. | Giả lập | Giám đốc vận hành |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Trong đợt chạy thử trên 1.200 yêu cầu: chỉ số chính đóng trong 24h không mở lại 7 ngày đạt **82,83% (994/1.200)**, tỉ lệ bỏ qua gợi ý **27,12% (48/177)**, tỉ lệ lỗi lọt đến khách **4,25% (51/1.200)** [E1]. | Xong, có bằng chứng | Trưởng nhóm CSKH |
| 5 · Bảng lỗi và cách khắc phục | Hai bộ nhãn độc lập đồng thuận **20/20 = 100%** (mốc 80%) trên 5 loại PAIR; 5 biện pháp khắc phục, mỗi loại lỗi một ca, đều có event, ngưỡng và tần suất đo [C]. | Xong, có bằng chứng | PM trợ lý hoàn phí |
| 6 · Pilot plan | Chia theo **nhân viên** (**20 người/nhóm**, phân tầng 12 depot) cho `noi_dia` + `hang_nang` (loại `quoc_te` 1,88×, `doi_tac` 0,85×); chấp nhận MDE **6 điểm** (`m ≥ 299`/người, **5.980/nhóm**, DE **6,96**; nếu thật 5 điểm thì power còn **0,64**) và 3 luật dừng đủ 4 vế [D1–D2]. | Xong, có bằng chứng | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Gấp đôi số ca làm lại làm chi phí tăng **51,8%**. Xem lại toàn bộ gợi ý đủ điều kiện với số phút làm lại trung bình trong phạm vi đẩy chi phí lên **12.516 đ/việc thành công = 1,04×** mốc thủ công. Giữ nguyên lưu lượng khi chạm ngưỡng E2 [simulated]. | Giả lập | PM trợ lý hoàn phí |

**Đề xuất:** **Go có điều kiện**

- **Số bất lợi & cách xử lý:** (1) Với 20 nhân viên/nhóm, trần cỡ mẫu hiệu dụng chỉ đạt **1.000 < 1.251** nên nếu tác động thật chỉ 5 điểm thì **power còn 0,64** — xử lý bằng cách chốt MDE **6 điểm** (`m ≥ 299` yêu cầu/người) và đo đủ 2 tuần ở bước `0.50`; (2) Nếu tuần đầu phải xem lại **100%** gợi ý với 16,2 phút làm lại trong phạm vi, chi phí lên **12.516 đ = 1,04×** mốc thủ công [simulated] — xử lý bằng 3 luật dừng và hạ tỉ lệ xem lại.
- **Điều kiện 1 (An toàn & chống hoàn trùng):** Khoá chống hoàn trùng và không báo thành công khi sổ cái lỗi (Ca 7, 20), giữ tỉ lệ mở lại 7 ngày trong phạm vi không vượt **+2 điểm** so với đối chứng hoặc trần **6%** — **Kỹ sư trưởng agent** · kiểm tra **2026-12-01**.
- **Điều kiện 2 (Chi phí & mức dùng):** Giữ chi phí trong phạm vi **≤ 8.000 đ/việc thành công**, làm lại **≤ 7%/tuần** và bỏ qua gợi ý **≤ 40%/tuần** qua các bước `10% → 25% → 50%` — **PM trợ lý hoàn phí** · kiểm tra hằng tuần từ **2026-12-08**.
- **Điều kiện 3 (Quyết định bước 0,50):** Người kiểm số hoàn tất `n_per_arm`, `design_effect`, `clusters_per_arm` trong `pilot_plan.yaml` và tổng hợp kết quả đo đủ mẫu — **Giám đốc vận hành LogiX-VN** · kiểm tra **2027-01-12**.
