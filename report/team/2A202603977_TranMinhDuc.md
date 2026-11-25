# Báo cáo cá nhân — Trần Minh Đức - 2A202603977

## 1. Thông tin thành viên

- Họ tên: Trần Minh Đức
- MSSV: 2A202603977
- Email:
- Vai trong nhóm: **Nhóm trưởng** · **Người viết code phiên 1** (CP1 nhiệm vụ A, CP2 nhiệm vụ B)

## 2. Phần việc phụ trách

- `src/lab13.py`: ba hàm A1, `mo_hinh()`, A3 (tách theo `loai`), A4 (chi phí cố định), và CP2 bảng độ nhạy B1–B4.
- `report/team/bang_chi_phi.md`: bảng A1, A2, A3, A4 và các câu trả lời của nhiệm vụ A.
- `report/team/pilot_plan.yaml`: các trường của file và ba luật dừng (CP4).
- `report/team/group_report.md`, `TEAM.md`, `PHAN_CONG.md`.
- Vai trưởng nhóm: chủ repo, phân công, merge nhánh, soát 6 file hồ sơ, chốt push và nhắc cả nhóm nộp LMS.

## 3. Đóng góp cụ thể

- **A1:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`. `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` với 1,20 · 1,25 · 1,25.
- **A2:** viết `mo_hinh()` — tử số cộng mọi lần chạy kể cả `status == 'loi'`, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Kết quả: chi phí mỗi việc thành công **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ).
- **A3:** gọi lại `mo_hinh()` cho 4 giá trị `loai` và tính tỉ lệ `ok` theo từng `attempt`. Kết luận: `quoc_te` 1,88× và thành công 27,3%, chạy lại không giúp (30,0% → 11,4% → 2,2%).
- **A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang`: 1.185 đ/việc ở 45.000 yêu cầu/tháng → 4.599 đ = 0,38×; 2.370 đ/việc nếu còn một nửa khối lượng → 5.784 đ = 0,48× [simulated].
- **B:** (điền sau CP2)
- **D:** (điền sau CP4 — các trường YAML và ba luật dừng)

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `src/lab13.py` — ba hàm A1 và `mo_hinh()`; chạy lại ra đúng các số trong `bang_chi_phi.md`.
- `report/team/bang_chi_phi.md` — bảng A1, A2, A3, A4 và 4 câu trả lời.
- Commit: (điền hash commit `CP1 A1-A4`)
- Con số tự kiểm được: token 245.585 đ · tool 84.000 đ (5.600 lần gọi) · xem lại 890 phút = 1.780.000 đ [sim] · làm lại 1.132 phút = 2.264.000 đ [sim] · tổng 4.373.585 đ · 978 việc thành công · 4.472 đ/việc · chi phí cả hệ thống 5.865 đ/yêu cầu = 0,49×.

## 5. Công cụ AI đã dùng

Công cụ nào, dùng vào việc gì, bạn tự kiểm tra kết quả ra sao.

- **Công cụ:** Claude Code (Claude Opus).
- **Dùng vào việc gì:** gợi ý code cho ba hàm A1 và `mo_hinh()`, phần in bảng A3 và A4 trong `__main__`, soạn bản phân công `PHAN_CONG.md`, và điền số vào các bảng của `bang_chi_phi.md` từ output của `lab13.py`.
- **Tự kiểm tra ra sao:**
  1. Tính tay phép thử A1: với `p = 0,8` và `k = 2` thì `(1 − (1 − 0,8)²) / 0,8 = 0,96 / 0,8 = 1,20`, khớp output. `kiem_tra_dap_an_biet_truoc()` qua cả ba `assert` ở ngưỡng `1e-9`.
  2. Đối chiếu từng dòng A2 với bảng số tự kiểm trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` — lệch 0%.
  3. Kiểm hai số do AI dẫn lại mà chưa tự tính (5.600 lần gọi tool, tổng chi phí phạm vi 3.072.513 đ) bằng cách chạy `runs.tool_calls.sum()` và `mo_hinh(runs, pham_vi)['tong']` trên máy mình.
  4. Người kiểm số (Trần Thị Nhài) tính tay độc lập các khoản của A2 và so với output; lệch không quá 2%.
- **Không dùng AI để:** bịa số, bịa nhãn lỗi, hay bịa kết quả duyệt chéo.

## 6. Tự đánh giá

...
