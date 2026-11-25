# Báo cáo cá nhân — Trần Hải Long - 2A202603891

## 1. Thông tin thành viên

- Họ tên: Trần Hải Long
- MSSV: 2A202603891
- Email:
- Vai trong nhóm: **Người gắn nhãn 2, kiêm giữ hồ sơ** (điền `ho_so_launch_v0.md` từ đầu buổi)

## 2. Phần việc phụ trách

- `report/team/ho_so_launch_v0.md`: giữ và điền dần từ 14:10 — bảy mục, mỗi mục có con số chính, trạng thái (Xong có bằng chứng · Chưa · Giả lập) và một vai trò phụ trách; dòng cuối là đề xuất Go / Go có điều kiện / No-go.
- Gắn nhãn độc lập cả 20 ca lỗi (bộ nhãn 2) và chọn 5 ca cho bảng khắc phục trong `report/team/bang_loi.md`.
- `report/team/chi_so.md`: mục E2 rủi ro kinh tế, ít nhất hai dòng, số lấy từ bảng độ nhạy.
- Trường `scope` của `report/team/pilot_plan.yaml`: phạm vi thu hẹp kèm lý do bằng số từ A3.
- `report/team/phieu_cham.md`: chấm nhóm n + 1 khi làm hội đồng Gate 2a.

## 3. Đóng góp cụ thể

- **Hồ sơ launch v0:** đã điền thông tin nhóm `4mems · L3B` và hoàn thành các mục 1, 2, 3, 7 trong `report/team/ho_so_launch_v0.md` (đều ghi trạng thái `Giả lập` vì tính từ hai cột `_simulated`); các mục 4, 5, 6 và đề xuất cuối sẽ điền tiếp sau CP3–CP5.
- **Mục 1, 2 và 3 của hồ sơ:** mục 1 là **4.472 đ/việc thành công** [simulated, A2]; mục 2 nêu 3 yếu tố nhạy nhất (+51,8% làm lại ×2, +40,7% xem lại ×2, +23,1% lương +25%) [simulated, B1–B2]; mục 3 dùng phạm vi `noi_dia` + `hang_nang` ở quy mô 45.000 yêu cầu/tháng là **5.217 đ/yêu cầu = 0,43×** mốc 12.000 đ (đã gồm chi phí cố định và 82/982 ca nhân viên làm thay) [simulated, A4].
- **Phạm vi pilot (`scope` trong `pilot_plan.yaml`):** thu hẹp vào `noi_dia` (0,22×) và `hang_nang` (0,69×); loại `quoc_te` (1,88×, thành công 27,3%) và `doi_tac` (0,85×, sát ngưỡng và có điều khoản riêng) [simulated, A3].
- **Gắn nhãn 20 ca (bộ nhãn 2):** (chờ gắn nhãn độc lập lúc 15:35–15:43)
- **Bảng khắc phục 5 ca:** (chờ hoàn thiện cùng Hải lúc 15:43–16:08)
- **E2 rủi ro kinh tế:** đã điền 2 dòng trong `report/team/chi_so.md` lấy số từ B1 (+51,8% lên 6.787 đ/việc thành công, ngưỡng `lam_lai` 9,8%/tuần, PM trợ lý hoàn phí) và B4 (xem lại 100% lên 11.743–12.516 đ = 1,04×, ngưỡng 100% xem lại và ≥ 5 phút/lần, Trưởng nhóm CSKH).
- **Đề xuất cuối:** (chờ tổng hợp sau CP4–CP5)
- **Phiếu chấm hội đồng:** (chờ duyệt chéo lúc 17:00–17:45)

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- (điền hash commit của nhánh `long/cp5-ho-so`)
- (điền ảnh chụp bộ nhãn độc lập ghi trước khi so với người gắn nhãn 1)
- `report/team/ho_so_launch_v0.md`, `report/team/phieu_cham.md`

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Công cụ:** (điền; nếu không dùng thì ghi rõ "không dùng")
- **Dùng vào việc gì:** (điền — lưu ý: **không được** dùng AI để gắn nhãn 20 ca hay để bịa kết quả duyệt chéo)
- **Tự kiểm tra ra sao:** (điền — mọi con số trong hồ sơ phải truy được về `bang_chi_phi.md` hoặc output của `src/lab13.py`)
- **Không dùng AI để:** bịa số, bịa nhãn lỗi, hay bịa kết quả duyệt chéo.

## 6. Tự đánh giá

...
