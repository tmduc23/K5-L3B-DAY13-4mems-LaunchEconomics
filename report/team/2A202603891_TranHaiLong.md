# Báo cáo cá nhân — TranHaiLong-2A202603891

## 1. Thông tin thành viên

- Họ tên: Trần Hải Long
- MSSV: 2A202603891
- Email: longhtr028@gmail.com
- Vai trong nhóm: Người gắn nhãn 2 (CP3) · giữ hồ sơ launch v0.

## 2. Phần việc phụ trách

- `report/team/ho_so_launch_v0.md` (giữ hồ sơ, điền mục 1–7 và đề xuất Gate 2a).
- `report/team/bang_loi.md` (bộ nhãn 2 + đối chiếu đồng thuận + bảng khắc phục).
- `report/team/pilot_plan.yaml` (trường `scope`).
- `report/team/chi_so.md` (E2 rủi ro kinh tế).
- `report/team/phieu_cham.md` và rà soát `report/team/group_report.md`.

## 3. Đóng góp cụ thể

- Điền đủ 7 mục trong `report/team/ho_so_launch_v0.md`, chốt **Go có điều kiện** kèm 2 số bất lợi (`power = 0,64` ở MDE 5 điểm; `12.516 đ = 1,04×` khi xem lại 100%).
- Gắn nhãn 20 ca độc lập (`Nhãn người 2`), đồng thuận **20/20 (100%)** với Hải; thống nhất Ca 8 là `Hệ thống` (lỗi hệ thống).
- Viết `scope` trong `report/team/pilot_plan.yaml` (`noi_dia` 0,22×, `hang_nang` 0,69×; loại `quoc_te` 1,88×, `doi_tac` 0,85×).
- Viết 2 rủi ro kinh tế E2 trong `report/team/chi_so.md` (`+51,8%` lên `6.787 đ`; `12.516 đ = 1,04×` khi xem lại 100%).

## 4. Bằng chứng

- `report/team/ho_so_launch_v0.md`.
- `report/team/bang_loi.md`.
- Phần `scope` trong `report/team/pilot_plan.yaml`.
- Bảng E2 trong `report/team/chi_so.md`.

## 5. Công cụ AI đã dùng

- Dùng trợ lý AI để đối chiếu định nghĩa 5 loại lỗi PAIR, rà soát số liệu từ `bang_chi_phi.md`, `chi_so.md`, `pilot_plan.yaml`, và kiểm tra quy tắc hồ sơ (`simulated`, một vai trò phụ trách, không dùng từ bị cấm).
- Tự kiểm tra lại bằng cách đối chiếu trực tiếp từng con số với các file của nhóm và chạy `grep` kiểm tra từ khóa trong `report/team/`.

## 6. Tự đánh giá

- Hoàn thành đúng mốc phần gắn nhãn 2, `scope`, rủi ro E2 và hồ sơ launch v0; giữ nguyên hai bộ nhãn độc lập trước khi đối chiếu và gắn nhãn `simulated` cho các con số giả lập.
