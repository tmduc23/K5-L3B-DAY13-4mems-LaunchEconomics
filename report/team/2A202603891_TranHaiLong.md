# Báo cáo cá nhân — TranHaiLong-2A202603891

## 1. Thông tin thành viên

- Họ tên: Trần Hải Long
- MSSV: 2A202603891
- Email: ...
- Vai trong nhóm: Người gắn nhãn 2, kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Giữ và hoàn thiện hồ sơ launch v0 (`report/team/ho_so_launch_v0.md`) từ đầu buổi qua các mốc CP1–CP5, chốt đề xuất Gate 2a kèm số bất lợi và điều kiện.
- Gắn nhãn độc lập 20 ca lỗi theo 5 loại PAIR (CP3), cùng Hải đối chiếu đồng thuận, viết quy tắc phân biệt và bảng khắc phục 5 ca (`report/team/bang_loi.md`).
- Viết `scope` cho `report/team/pilot_plan.yaml` dựa trên số A3.
- Viết mục E2 rủi ro kinh tế trong `report/team/chi_so.md` dựa trên bảng độ nhạy B1 và B4.
- Chấm hồ sơ nhóm bạn ở phiên hội đồng (`report/team/phieu_cham.md`) và rà soát `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Điền mục 1, 2, 3 (chi phí A2, độ nhạy B1–B2, so với mốc thủ công 12.000 đ ở A4) và mục 4, 5, 6, 7 trong `report/team/ho_so_launch_v0.md`, kèm đề xuất **Go có điều kiện** và 2 số bất lợi (`power = 0,64` ở MDE 5 điểm; `12.516 đ = 1,04×` khi xem lại 100%).
- Gắn nhãn độc lập 20 ca lỗi (`Nhãn người 2`), đạt đồng thuận **19/20 = 95%** với Hải, lệch duy nhất ca 8 (tôi ghi Ngầm, Hải ghi Hệ thống) và nhóm chốt nhãn thống nhất là **Hệ thống** vì lỗi đã lộ ra trong câu trả lời gửi khách; hoàn thiện bảng khắc phục 5 ca có event, ngưỡng, tần suất và một vai trò phụ trách.
- Viết `scope` trong `report/team/pilot_plan.yaml` (`noi_dia` 0,22×, `hang_nang` 0,69×; loại `quoc_te` 1,88× và `doi_tac` 0,85×).
- Viết 2 dòng rủi ro kinh tế E2 trong `report/team/chi_so.md` (+51,8% lên 6.787 đ khi làm lại gấp đôi; 12.516 đ = 1,04× khi xem lại 100%).

## 4. Bằng chứng

- `report/team/ho_so_launch_v0.md` (7 mục hoàn chỉnh + đề xuất **Go có điều kiện**).
- `report/team/bang_loi.md` (20 nhãn độc lập `Nhãn người 2`, đồng thuận 19/20 = 95%, quy tắc Ca 8, bảng khắc phục 5 ca).
- `report/team/pilot_plan.yaml` (trường `scope`).
- `report/team/chi_so.md` (bảng E2 rủi ro kinh tế).

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI (Antigravity / Gemini 4 Hydrogen) để đọc đề bài 20 ca lỗi, đối chiếu định nghĩa 5 loại lỗi PAIR, kiểm tra các quy tắc hồ sơ (`simulated`, một vai trò phụ trách, không dùng từ bị cấm) và rà soát số liệu từ `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`.
- Cách tự kiểm tra: đối chiếu trực tiếp từng con số với `report/team/bang_chi_phi.md`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml`, và chạy `grep` kiểm tra từ khoá bắt buộc trong `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đúng mốc các phần việc gắn nhãn, phạm vi, rủi ro và hồ sơ launch v0; giữ nguyên hai bộ nhãn độc lập trước khi so sánh và đảm bảo mọi con số giả lập đều có nhãn `simulated`.
