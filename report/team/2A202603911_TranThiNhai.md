# Báo cáo cá nhân — Trần Thị Nhài - 2A202603911

## 1. Thông tin thành viên

- Họ tên: Trần Thị Nhài
- MSSV: 2A202603911
- Email: nhainhinhanh6a@gmail.com
- Vai trong nhóm: **Người kiểm số** (CP1, CP2) · **Người viết code phiên 2** (CP4 nhiệm vụ D1, CP5 nhiệm vụ E1)

## 2. Phần việc phụ trách

- Kiểm số cho nhiệm vụ A và B: đối chiếu số tính từ tổng cột CSV với output của `src/lab13.py`, lệch quá 2% thì truy chỗ sai trước khi nhóm đi tiếp.
- `report/team/bang_chi_phi.md`: cột Nguồn và Nhãn của bảng A2, 9 dòng bảng độ nhạy B1 và câu kiểm đối xứng.
- `src/lab13.py` sau giờ giải lao: `co_mau()`, `he_so_thiet_ke()`, `m_toi_thieu()`, năm câu D1, tỉ lệ `mo_lai_trong_7_ngay` hiện tại, ba chỉ số E1.
- `report/team/pilot_plan.yaml`: chú thích D1, đánh đổi đã chấp nhận, tỉ lệ mở lại hiện tại, các trường `mde`, `n_per_arm`, `design_effect`, `clusters_per_arm`.

## 3. Đóng góp cụ thể

- **Kiểm số A1, A2:** A1 ra 1,20 · 1,25 · 1,25. A2: token 5.771.712 ÷ 1.000 × 26 + 734.774 ÷ 1.000 × 130 = 245.585 đ; tool 5.600 × 15 = 84.000 đ; xem lại 890 × 2.000 = 1.780.000 đ [simulated]; làm lại 1.132 × 2.000 = 2.264.000 đ [simulated]; 4.373.585 ÷ 978 = **4.472 đ/việc thành công** [simulated], gấp 16,3× hoá đơn chia số yêu cầu (274,7 đ). Khớp output `mo_hinh()`, lệch 0%.
- **Soát ba lỗi hay gặp trong `mo_hinh()`:** token cộng trên mọi 1.624 lần chạy kể cả `loi`; mẫu số là 978 chứ không phải 1.200; có chia 1.000 trước khi nhân giá. Cả ba đều đúng. Nếu bỏ lần chạy lỗi sẽ ra 4.346 đ (−2,8%), chia 1.200 sẽ ra 3.645 đ.
- **Kiểm đối xứng B1:** token +5,6% ↔ −2,8% · xem lại +40,7% ↔ −20,3% · làm lại +51,8% ↔ −25,9%, đúng quy tắc "giảm một nửa = nửa mức tăng" nên code B đúng.
- **D1, năm câu cỡ mẫu:** (a) 1.251/nhóm · (b) DE 2,48, 3.103/nhóm = 42 người/nhóm, cần 84 > 40 người · (c) trần 20 ÷ 0,02 = 1.000 < 1.251 · (d) trần 6 ÷ 0,02 = 300 · (e) mức chênh 6 điểm cần 859/nhóm, m ≥ 299 yêu cầu/người, DE 6,96. Con số bất lợi: power còn 0,64 nếu tác động thật chỉ 5 điểm.
- **Tỉ lệ mở lại 7 ngày hiện tại:** 4,25% (51/1.200), trong phạm vi `noi_dia` + `hang_nang` 3,97% (39/982). Đã đưa cho nhóm trước khi viết luật an toàn, nên ngưỡng không đặt dưới tỉ lệ nền.
- **E1, ba chỉ số trong đợt chạy thử:** chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177; sửa 41 + bỏ 7 trên 177 ca được xem lại) · mở lại 7 ngày 4,25% (51/1.200).
- **Kiểm commit của thành viên khác:** chạy lại `lab13.py` sau mỗi lần pull, đối chiếu số A3, A4, B2–B4 và số trong `scope`, hồ sơ, E2. Phát hiện `mde` trong YAML còn 0,05, mâu thuẫn với mức chênh 6 điểm đã chốt, và đã sửa.

## 4. Bằng chứng

- Commit `c17d643`: Nguồn, Nhãn bảng A2 và 9 dòng B1 + kiểm đối xứng trong `bang_chi_phi.md`.
- Commit `81806e0`: `co_mau()` và năm câu D1, tỉ lệ mở lại 7 ngày trong `src/lab13.py`; chú thích D1 trong `pilot_plan.yaml`.
- Commit `15b213c`: ba chỉ số E1 trong `src/lab13.py`.
- Commit `8f34de4`: `mde`, `n_per_arm`, `design_effect`, `clusters_per_arm`, đánh đổi và tỉ lệ mở lại hiện tại trong `pilot_plan.yaml`.
- Output `python lab13.py`, phần D1 và E1:

```text
a) Chia theo yeu cau: co_mau(0.70, 0.75) = 1,251 yeu cau/nhom
b) Theo nhan vien, m = 75: DE = 1 + 74 x 0.02 = 2.48; n = 1,251 x 2.48 = 3,103/nhom = 42 nguoi/nhom, tong 84 > 40 -> KHONG du nguoi
c) 20 nhan vien/nhom: tran c/ICC = 20/0.02 = 1,000 < 1,251 -> KHONG dat muc chenh 5 diem
d) 6 depot/nhom: tran 6/0.02 = 300 -> loai (chi 6 cum, duoi 20)
e) Muc chenh 6 diem: co_mau(0.70, 0.76) = 859/nhom; 20m/(1 + (m-1) x 0.02) >= 859 -> m >= 299 yeu cau/nguoi (DE 6.96)
   Danh doi: neu tac dong that chi 5 diem, power voi n = 859 chi con 0.64
Ti le mo_lai_trong_7_ngay hien tai: toan bo 4.25% (51/1200) · noi_dia + hang_nang 3.97% (39/982)
Chinh: dong 24h & khong mo lai 7 ngay     82.83% (994/1200)
Dung: bo qua goi y (sua + bo)             27.12% (48/177)
An toan: mo lai trong 7 ngay               4.25% (51/1200)
```

- Lỗi kỹ thuật gặp trên Windows: `python lab13.py` báo `UnicodeEncodeError` khi in tiếng Việt, xử lý bằng `$env:PYTHONIOENCODING="utf-8"`. Lệnh kiểm `yaml.safe_load(open(...))` báo `UnicodeDecodeError` (kể cả với file mẫu gốc), xử lý bằng `python -X utf8`.

## 5. Công cụ AI đã dùng

- **Công cụ:** Claude Code (trong VS Code).
- **Dùng vào việc gì:** đọc đề và phân công để nắm phần việc; lấy tổng các cột trong hai file CSV và lập bảng tính A2; viết code D1, E1 và điền các bảng, trường YAML thuộc phần của mình; rà các commit của nhóm sau mỗi lần pull.
- **Tự kiểm tra ra sao:** tự bấm máy lại các dòng token, xem lại, làm lại và chi phí mỗi việc thành công của A2, câu D1 (e) (2,82m ≥ 841,82 → m ≥ 299), và tỉ lệ 48/177; chạy `python lab13.py` trên máy mình sau mỗi lần pull; đối chiếu mọi số với các mốc trong `docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md` (lệch ≤ 2%).
- **Không dùng AI để:** bịa số, bịa nhãn lỗi, hay bịa kết quả duyệt chéo.

## 6. Tự đánh giá

- **Làm được:** hoàn thành kiểm số A/B, code D1 và E1 trước lịch; mọi số chạy lại được từ `lab13.py` và khớp mốc hướng dẫn (A2 lệch 0%, D1 năm câu đúng); khi điền cỡ mẫu đã phát hiện `mde` 0,05 mâu thuẫn với mức chênh 6 điểm đã chốt và sửa thành 0,06.
- **Cần cải thiện:** phần kiểm A2 chưa hoàn toàn độc lập vì tổng cột lấy bằng pandas chứ không đếm tay; phụ thuộc AI ở bước viết code D1, E1.
- **Rút kinh nghiệm:** lần sau tự tính tay một phép trước (ví dụ 4.373.585 ÷ 978), rồi mới dùng code và AI để đối chiếu.
