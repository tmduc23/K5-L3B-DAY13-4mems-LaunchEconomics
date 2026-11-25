# Báo cáo cá nhân — Trần Minh Đức - 2A202603977

## 1. Thông tin thành viên

- Họ tên: Trần Minh Đức
- MSSV: 2A202603977
- Email:tranminhduc230204@gmail.com
- Vai trong nhóm: **Nhóm trưởng** · **Người viết code phiên 1** (CP1 nhiệm vụ A, CP2 nhiệm vụ B)

## 2. Phần việc phụ trách

- `src/lab13.py`: ba hàm A1, `mo_hinh()`, A3 (tách theo `loai`), A4 (chi phí cố định), và CP2 bảng độ nhạy B1–B4.
- `report/team/bang_chi_phi.md`: bảng A1, A2, A3, A4 và các câu trả lời của nhiệm vụ A.
- `report/team/pilot_plan.yaml`: các trường của file và bốn luật dừng (CP4).
- `report/team/group_report.md`, `TEAM.md`, `PHAN_CONG.md`.
- Vai trưởng nhóm: chủ repo, phân công, merge nhánh, soát 6 file hồ sơ, chốt push và nhắc cả nhóm nộp LMS.

## 3. Đóng góp cụ thể

- **A1:** viết `so_lan_chay_ky_vong`, `ti_le_thanh_cong`, `he_so_chi_phi_moi_viec_thanh_cong`. `python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT` với 1,20 · 1,25 · 1,25.
- **A2:** viết `mo_hinh()` — tử số cộng mọi lần chạy kể cả `status == 'loi'`, mẫu số chỉ đếm `ket_qua == 'thanh_cong'`. Kết quả: chi phí mỗi việc thành công **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ).
- **A3:** gọi lại `mo_hinh()` cho 4 giá trị `loai` và tính tỉ lệ `ok` theo từng `attempt`. Kết luận: `quoc_te` 1,88× và thành công 27,3%, chạy lại không giúp (30,0% → 11,4% → 2,2%).
- **A4:** cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang`: 1.185 đ/việc ở 45.000 yêu cầu/tháng → 4.599 đ = 0,38×; 2.370 đ/việc nếu còn một nửa khối lượng → 5.784 đ = 0,48× [simulated].
- **B1:** 9 kịch bản độ nhạy, gốc 4.472 đ. Số ca làm lại gấp đôi **+51,8%** (6.787 đ) · xem lại gấp đôi **+40,7%** (6.292 đ) · lương +25% **+23,1%** (5.506 đ) · giá token gấp đôi chỉ **+5,6%** (4.723 đ) [simulated]. Xếp hạng ba yếu tố nhạy nhất: làm lại → xem lại → lương.
- **B2:** đổi một cặp (giá token gấp đôi + xem lại gấp đôi) ra 6.543 đ = **+46,3%**, đúng bằng tổng hai tác động riêng vì mô hình cộng tuyến tính các khoản chi phí.
- **B3:** giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ cả hệ thống) nhưng **không** trùng giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần, 4.111 đ). Tối ưu riêng chi phí mỗi việc sẽ đẩy thêm 85 việc sang nhân viên và làm cả hệ thống đắt thêm 548.561 đ.
- **B4:** xem lại 100% trong phạm vi cho 11.743 đ = **0,98×**, lên 12.415 đ = **1,03×** nếu dùng số phút làm lại thực 15,3 phút [simulated]; mức hoà vốn là mỗi lần xem lại không quá **5,1 phút**.
- **D:** điền `owner` (Giám đốc vận hành), `assignment.unit: staff`, `rollout`, `identifiability` (chuyển năm câu D2 thành giá trị), `rollback`, `decision_date`, `simulated_inputs` 8 dòng, và **bốn luật dừng** đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ cho hoàn trùng, an toàn, chi phí, mức độ sử dụng (sau duyệt chéo, nhóm tách hoàn trùng thành luật thứ tư dừng ngay trong ngày). Ngưỡng an toàn đặt theo tỉ lệ nền 3,97% trong phạm vi: chênh ≥ 2 điểm so với đối chứng hoặc trần tuyệt đối 6%, thay vì ngưỡng tuyệt đối 3% sẽ làm pilot dừng ngay tuần đầu.
- **Vai trưởng nhóm:** điền `TEAM.md` và `PHAN_CONG.md`; merge nhánh của người gắn nhãn 1 vào `main` và xử lý 4 lần conflict; soát 6 file hồ sơ; viết `group_report.md`.

## 4. Bằng chứng

Commit, file, bảng hoặc con số do bạn làm.

- `src/lab13.py` — ba hàm A1 và `mo_hinh()`; chạy lại ra đúng các số trong `bang_chi_phi.md`.
- `report/team/bang_chi_phi.md` — bảng A1, A2, A3, A4 và 4 câu trả lời.
- Commit: `eed8a92` — *CP1+CP2: mo hinh chi phi, tach theo loai, chi phi co dinh, bang do nhay* (thêm ba hàm A1 và `mo_hinh()` vào `src/lab13.py`, điền bảng A1–A4 vào `bang_chi_phi.md`). Các commit sau của riêng phần này: `c121a7e` (CP4 các trường và luật dừng), `910069e` (sửa console cp1252), `0d1efa0` (đồng bộ nhãn ca 8 và mục 5 hồ sơ).
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

- **Làm được:** xong nhiệm vụ A và B đúng mốc, mọi số lệch 0% so với bảng đối chiếu trong `docs/`; nhận ra 4.472 đ / 12.000 đ = 0,37× là con số thiếu nên tính thêm chi phí cả hệ thống 0,49×, nhờ đó hồ sơ nêu được con số bất lợi thay vì chọn số đẹp; phát hiện `mde` 0,05 mâu thuẫn với cỡ mẫu 859 và sửa thành 0,06 trước khi nộp; phát hiện lệnh kiểm trong đề bài crash trên Windows và sửa ở mức file thay vì bắt từng người đặt biến môi trường.
- **Cần cải thiện:** để `TEAM.md` trống gần hết buổi dù đó là file của mình, chỉ điền lúc gần cuối; điều phối git chậm, có lúc local đi sau remote 3 commit nên cả nhóm làm trên bản cũ và sinh conflict; nhận bản phân công theo nhánh nhưng lại commit thẳng `main` nên mất chỗ để người khác duyệt trước khi merge.
- **Rút kinh nghiệm:** việc của trưởng nhóm (`TEAM.md`, `group_report.md`) nên làm sớm ngay trong CP1 vì nó không phụ thuộc số liệu, và nên `git pull` trước mỗi lần sửa file dùng chung thay vì sửa xong mới pull.
