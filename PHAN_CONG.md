# Phân công công việc — Lab 13 · LogiX-VN Gate 2a

Nhóm 4 người · Lớp **L3B** · Repo `K5-L3B-DAY13-4mems-LaunchEconomics` (chủ repo: `tmduc23`)
Buổi lab 14:00–18:00 · Deadline nộp LMS: **23h59 GMT+7 ngày lab**

File này chỉ để chia việc, **không phải file hồ sơ nộp** (nên các lệnh `grep` kiểm tra trong file này đều chỉ quét thư mục `report/team/`). Luật chấm điểm vẫn theo [RUBRIC.md](RUBRIC.md), mốc giờ theo [CHECKPOINTS.md](CHECKPOINTS.md), cách nộp theo [SUBMISSION.md](SUBMISSION.md).

---

## 1. Bảng phân vai

| Người | MSSV | Vai của lab | File chịu trách nhiệm chính | File báo cáo cá nhân phải tạo |
| --- | --- | --- | --- | --- |
| **Trần Minh Đức** (nhóm trưởng) | 2A202603977 | **Người viết code — phiên 1** (CP1 nhiệm vụ A, CP2 nhiệm vụ B) + chủ repo, điều phối, chốt nộp | `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/group_report.md`, `TEAM.md` | `report/team/2A202603977_TranMinhDuc.md` |
| **Trần Thị Nhài** | 2A202603911 | **Người kiểm số** (CP1, CP2) → **Người viết code — phiên 2** (CP4 nhiệm vụ D1 cỡ mẫu, CP5 ba chỉ số) | Cột "kiểm tay" của `bang_chi_phi.md`, phần chú thích D1 trong `report/team/pilot_plan.yaml`, số ở bảng E1 | `report/team/2A202603911_TranThiNhai.md` |
| **Ngô Ngọc Hải** | 2A202603939 | **Người gắn nhãn 1** (CP3) + chủ trì chỉ số và event (CP5) | `report/team/bang_loi.md` (bộ nhãn 1 + bảng khắc phục), `report/team/chi_so.md` | `report/team/2A202603939_NgoNgocHai.md` |
| **Trần Hải Long** | 2A202603891 | **Người gắn nhãn 2, kiêm giữ hồ sơ** (điền hồ sơ từ 14:10) | `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md` (bộ nhãn 2), mục E2 rủi ro trong `chi_so.md`, `report/team/phieu_cham.md` | `report/team/2A202603891_TranHaiLong.md` |

**Vì sao chia như vậy:** [TEAM.md](TEAM.md) yêu cầu đổi người viết code sau giờ giải lao để ít nhất hai người tự tay tính được chi phí → Đức code phiên 1, Nhài code phiên 2. CP3 cần hai người gắn nhãn **ngồi tách nhau trong 8 phút** → Hải và Long, trong lúc đó Đức và Nhài hoàn thiện nhiệm vụ B.

**Năm điều ai cũng phải nhớ** (quy tắc lab, mất điểm nếu sai):

1. Chưa qua ba phép thử A1 (**1,20 · 1,25 · 1,25**) thì không ai được làm tiếp.
2. Mọi con số lấy từ `phut_xem_lai_simulated` / `phut_lam_lai_simulated` phải ghi nhãn **`simulated`**.
3. Mỗi câu trả lời **≤ 3 dòng và có ít nhất một con số**.
4. Người phụ trách luôn là **một vai trò** ("PM trợ lý hoàn phí", "Trưởng nhóm CSKH"…), **không ghi "cả đội"**.
5. **Không dùng từ "production"** ở bất kỳ file hồ sơ nào. Kiểm tra: `grep -rni production report/team`.

---

## 2. Lịch buổi chiều — ai làm gì, từng mốc

| Giờ | Đức (code 1 / trưởng nhóm) | Nhài (kiểm số → code 2) | Hải (gắn nhãn 1) | Long (gắn nhãn 2 + giữ hồ sơ) |
| --- | --- | --- | --- | --- |
| 14:00–14:10 | Chia vai, điền `TEAM.md`, kiểm tra ai cũng clone được repo | Cài venv, chạy `python -c "import pandas…"` | Cài venv, mở 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` | Cài venv, mở `ho_so_launch_v0.md`, điền tên nhóm + lớp |
| 14:10–14:53 **CP1 · A** | Viết 3 hàm A1 + `mo_hinh()`, rồi A2, A3, A4 | Tính tay token/tool/xem lại/làm lại để đối chiếu A2 | Đọc `docs/du_lieu_va_cong_thuc.md`, nắm định nghĩa 5 loại lỗi PAIR | Điền mục 1 và 3 của hồ sơ ngay khi có số A2/A4 |
| 14:53–15:20 **CP2 · B** | Viết vòng lặp 9 kịch bản B1, rồi B2, B3, B4 | Kiểm quy tắc đối xứng (gấp đôi ↔ giảm một nửa), điền bảng B1 | Đọc kỹ 20 ca lỗi, **chưa gắn nhãn** | Điền mục 2 của hồ sơ (ba yếu tố nhạy nhất) |
| 15:20–15:35 | Giải lao — **bàn giao code cho Nhài** (giải thích `mo_hinh()` 3 phút) | Nhận bàn giao code | Giải lao | Giải lao |
| 15:35–15:43 **CP3 · C** | Cùng Nhài hoàn thiện B3, B4 | Cùng Đức hoàn thiện B3, B4 | **Gắn nhãn 20 ca độc lập, 8 phút, không nói chuyện** | **Gắn nhãn 20 ca độc lập, 8 phút, không nói chuyện** |
| 15:43–16:08 | Soát giúp nếu đồng thuận < 80% | Nhập hai bộ nhãn vào `bang_loi.md` | So nhãn, tính % đồng thuận, viết quy tắc cho ca lệch | Chọn 5 ca (mỗi loại 1 ca), điền bảng khắc phục |
| 16:08–16:36 **CP4 · D** | Viết các trường YAML + 3 luật dừng (NẾU–TRONG–THÌ–KHÔNG THÌ) | **Code D1:** 5 câu cỡ mẫu + tỉ lệ `mo_lai_trong_7_ngay` hiện tại | Trả lời 5 câu D2 "tách được tác động" | Viết `scope` lấy từ A3, điền mục 6 hồ sơ |
| 16:36–17:00 **CP5 · E** | Soát 6 file, chạy lại `lab13.py` từ đầu | **Code E1:** 3 chỉ số tính thử | Viết bảng chỉ số + ≥ 6 event có `trace_id` | Viết ≥ 2 dòng rủi ro E2, **chốt đề xuất Go / Go có điều kiện / No-go** |
| 17:00–17:10 | Gửi `ho_so_launch_v0.md` cho nhóm hội đồng | Rà nhãn `simulated` lần cuối | Rà "cả đội" và "production" | Khoá bản hồ sơ đã gửi đi |
| 17:10–17:25 | Đọc hồ sơ nhóm n+1 | Đối chiếu số của nhóm đó | Chấm tiêu chí 2 (nhãn, phạm vi) | **Điền `phieu_cham.md`**, viết 1 câu hỏi |
| 17:25–17:40 | **Trình 1 phút** | Trả lời câu hỏi về số | Trả lời câu hỏi về lỗi/chỉ số | Công bố điểm khi làm hội đồng |
| 17:45–18:00 | Merge các nhánh, commit, push, kiểm repo mở được | Nộp link LMS | Nộp link LMS | Nộp link LMS |

Nhóm trưởng nộp link LMS cuối cùng sau khi push xong. **Ai không nộp link thì không có điểm, dù nhóm đã nộp.**

---

## 3. Checklist riêng từng người

### 3.1 Trần Minh Đức — 2A202603977 — nhóm trưởng, người viết code phiên 1

**Trước buổi lab**

- [ ] Repo đúng tên `K5-L3B-DAY13-4mems-LaunchEconomics`, **public** hoặc đã mời giảng viên.
- [ ] Mời Nhài, Hải, Long làm collaborator; cả 3 đã `git clone` thành công.
- [ ] Điền `TEAM.md`: tên nhóm, lớp L3B, URL repo, 4 dòng thành viên (họ tên, MSSV, email, GitHub, vai).

**CP1 · Nhiệm vụ A (14:10–14:53)**

- [ ] `cd src` → tạo venv → `python -m pip install -r requirements.txt` → in ra `san sang`.
- [ ] Viết 3 hàm A1 trong [src/lab13.py](src/lab13.py) tại dòng `TODO CP1`; `python lab13.py` in **`Ba phép thử đáp án biết trước: ĐẠT`**.
- [ ] Viết `mo_hinh(runs, reqs, …)`: tử số cộng **mọi** lần chạy kể cả `status == 'loi'`; mẫu số chỉ đếm `ket_qua == 'thanh_cong'`.
- [ ] Đọc CSV đúng cách: `pd.read_csv('logix_requests.csv', keep_default_na=False)` — thiếu tham số này là sai hàng loạt về sau.
- [ ] Chia 1.000 trước khi nhân giá token (26 đ và 130 đ cho **1.000** token).
- [ ] A3: gọi `mo_hinh(runs, reqs[reqs.loai == loai])` cho cả 4 loại.
- [ ] A4: cộng chi phí cố định 40 triệu đ/tháng cho phạm vi `noi_dia + hang_nang`, ở 2 mức khối lượng.
- [ ] Đổ số vào `report/team/bang_chi_phi.md` (bảng A1, A2, A3, A4) + trả lời 2 câu A2 và 1 câu A3, mỗi câu ≤ 3 dòng có số.
- [ ] Tự kiểm: chi phí mỗi việc thành công phải **gấp hơn 10 lần** "hoá đơn token chia số yêu cầu". Chỉ gấp 1–2 lần = đã quên giờ nhân viên.

**CP2 · Nhiệm vụ B (14:53–15:20)**

- [ ] Viết dict 9 kịch bản tại `TODO CP2`, in ra chi phí và % thay đổi so với gốc.
- [ ] B2: gọi `mo_hinh(..., gia_vao=52, gia_ra=260, he_so_xem_lai=2)` — kết quả phải **đúng bằng tổng hai tác động riêng** (mô hình cộng tuyến tính).
- [ ] B3: chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu **không** thành công, cho giới hạn 1/2/3 lần.
- [ ] B4: chỉ lấy `noi_dia + hang_nang`, giả định xem lại 100%.
- [ ] Xếp hạng đúng 3 yếu tố nhạy nhất và ghi vào B2.

**Giải lao — bàn giao (15:20)**

- [ ] Commit và push phần A, B lên nhánh của mình, mở PR.
- [ ] Giải thích cho Nhài trong 3 phút: tham số của `mo_hinh()`, chỗ `max_lan_chay` ghi đè `ket_qua`.

**CP4–CP5 (16:08–17:00) — vai trưởng nhóm**

- [ ] Điền các trường `pilot_plan.yaml`: `owner` (một vai trò), `assignment`, `rollout`, `identifiability`, `interim_looks`, `rollback`, `decision_date`, `simulated_inputs`.
- [ ] Viết **3 luật dừng** đủ bốn vế: **NẾU** [chỉ số vượt ngưỡng] – **TRONG** [bao lâu] – **THÌ** [việc cụ thể, ai làm] – **KHÔNG THÌ** [việc bị cấm]. Ba nhóm: an toàn, chi phí, mức độ sử dụng.
- [ ] Chạy 2 lệnh kiểm tra YAML (mục 6), không còn dấu `?` ngoài dòng chú thích.
- [ ] Soát chéo cả 6 file hồ sơ theo bảng mục 4.
- [ ] Viết `report/team/group_report.md` (8 mục, ≤ 2 trang), mục 5 ghi mọi lỗi kỹ thuật đã gặp kèm bằng chứng.
- [ ] Tạo `report/team/2A202603977_TranMinhDuc.md` từ mẫu `MSSV_HoTen.md` (**giữ nguyên file mẫu**).

**17:45 — đóng gói**

- [ ] Merge 4 nhánh về `main`; `cd src && python lab13.py` chạy hết **trên máy của một bạn khác**.
- [ ] `git status` sạch; không có `.venv/`, không có `.env`, không có key.
- [ ] Push `main`, mở link repo ở chế độ ẩn danh để chắc người chấm xem được.
- [ ] Nhắc từng người đã nộp link LMS, rồi tự nộp.
- [ ] **Không force-push, không xoá commit, không sửa ngày commit** (vi phạm [RULES.md](RULES.md)).

---

### 3.2 Trần Thị Nhài — 2A202603911 — người kiểm số, người viết code phiên 2

**CP1 (14:10–14:53) — kiểm số bằng tay, không chờ code xong**

- [ ] Tính tay 4 khoản của A2 **độc lập** với code của Đức: tiền token, tiền tool, tiền xem lại, tiền làm lại.
- [ ] Tính tay `so_lan_chay_ky_vong(0.8, 2)` = 1,20 để chắc công thức `(1 − (1 − p)^k) / p` đúng.
- [ ] So số của mình với số code in ra. **Lệch > 2% là một trong hai bên sai — dừng, tìm ra chỗ sai trước khi đi tiếp.**
- [ ] Ba lỗi phải chủ động soát trong code: (a) chỉ cộng token của lần chạy thành công, (b) chia cho 1.200 thay vì số việc thành công, (c) quên chia 1.000 trước khi nhân giá token.
- [ ] Điền cột "Nguồn" và "Nhãn" trong bảng A2 — hai dòng xem lại / làm lại **phải** có nhãn `simulated`.

**CP2 (14:53–15:20)**

- [ ] Kiểm quy tắc đối xứng của bảng B1: mỗi kịch bản "giảm một nửa" phải làm chi phí giảm **đúng nửa** mức tăng của kịch bản "gấp đôi" tương ứng. Không đúng → code sai.
- [ ] Nhập đủ **9 dòng** B1 vào `bang_chi_phi.md`, kèm cột "Cách tính".

**Nhận bàn giao code (15:35) — từ đây bạn là người viết code**

- [ ] Chạy lại `python lab13.py` trên **máy của mình**, ra đúng số của Đức.
- [ ] Giúp Đức chốt B3, B4 trong lúc Hải và Long đang gắn nhãn.

**CP4 · D1 (16:08–16:36) — phần code quan trọng nhất của bạn**

- [ ] Viết hàm `co_mau(p1, p2, alpha=0.05, power=0.8)` theo công thức so hai tỉ lệ.
- [ ] Tính đủ **5 câu**, ghi vào phần chú thích đầu `pilot_plan.yaml`:
  - [ ] a) chia theo **yêu cầu**: `co_mau(0.70, 0.75)`
  - [ ] b) theo **nhân viên, m = 75**: hệ số thiết kế `DE = 1 + (m − 1) × 0,02` rồi nhân với kết quả (a)
  - [ ] c) **20 nhân viên mỗi nhóm**: trần `c / ICC = 20 / 0,02`
  - [ ] d) **6 depot mỗi nhóm**: trần `6 / 0,02`
  - [ ] e) **mức chênh 6 điểm, 20 người/nhóm**: giải `20m / (1 + (m − 1) × 0,02) ≥ n` để tìm `m`
- [ ] Tính `reqs.mo_lai_trong_7_ngay.mean()` **trước khi** nhóm đặt ngưỡng an toàn, và tính riêng cho phạm vi `noi_dia + hang_nang`. Đưa số này cho Đức và Long — đặt ngưỡng tuyệt đối thấp hơn tỉ lệ hiện tại là pilot bị dừng ngay tuần đầu.
- [ ] Ghi `n_per_arm`, `design_effect`, `clusters_per_arm` vào YAML cho **cách chia đã chọn**, không phải cho cách chia lý tưởng.

**CP5 · E1 (16:36–17:00)**

- [ ] Code 3 chỉ số: chỉ số chính (`dong_trong_24h == 1` **và** `mo_lai_trong_7_ngay == 0`), tỉ lệ bỏ qua gợi ý (`sua` + `bo` trên số ca được xem lại), tỉ lệ mở lại 7 ngày.
- [ ] Đưa 3 số + mẫu số (ví dụ "994/1.200") cho Hải điền `chi_so.md`.
- [ ] Rà cả `report/team/` lần cuối: mọi con số từ cột `_simulated` đã có nhãn.

**Trước khi nộp**

- [ ] Tạo `report/team/2A202603911_TranThiNhai.md`; mục 5 ghi rõ đã dùng AI vào việc gì và **tự kiểm tra lại bằng cách nào**.
- [ ] Nộp link repo nhóm trên LMS bằng tài khoản của mình.

---

### 3.3 Ngô Ngọc Hải — 2A202603939 — người gắn nhãn 1, phụ trách chỉ số và event

**Trước CP3 (14:10–15:35) — chuẩn bị**

- [ ] Nắm 5 loại lỗi PAIR và **câu hỏi để nhận ra** từng loại: Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm.
- [ ] Mở mục "Hai mươi ca lỗi" trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`, đọc hết 20 ca nhưng **chưa viết nhãn nào ra giấy**.
- [ ] Thống nhất với Long: chỉ đọc đề, **không bàn ca nào trước khi gắn nhãn** (vi phạm [RULES.md](RULES.md) nếu bàn trước).

**CP3 · gắn nhãn (15:35–15:43, đúng 8 phút)**

- [ ] Ngồi tách khỏi Long, gắn nhãn cả 20 ca, mỗi ca một loại duy nhất.
- [ ] Nguyên tắc: gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa. "Trợ lý không gợi ý" là việc khắc phục, không đổi được nguyên nhân gốc là khách nhập sai.
- [ ] Phân biệt **Hệ thống** (sai đã lộ ra, có người thấy) với **Ngầm** (không ai nhận ra cho tới khi kiểm tra mẫu). Sai về **chi phí** cũng là sai.
- [ ] Ngoài phạm vi / thiếu dữ liệu → **Giới hạn hệ thống**, kể cả khi trợ lý xử lý giới hạn đó kém.
- [ ] Kết quả đúng chính sách nhưng khách hiểu sai → **Ngữ cảnh**.

**CP3 · so nhãn (15:43–16:08)**

- [ ] Nhập 2 bộ nhãn vào `report/team/bang_loi.md`, điền cột "Trùng?" cho từng ca.
- [ ] Tính tỉ lệ đồng thuận = số ca trùng ÷ 20. **Phải ≥ 16/20.** Thấp hơn → viết lại định nghĩa loại lỗi rồi ghi bản định nghĩa đã sửa vào file, **không sửa hai bộ nhãn độc lập đã ghi**.
- [ ] Mỗi ca lệch: thống nhất một nhãn + viết **một câu quy tắc phân biệt**.
- [ ] Cùng Long chốt bảng khắc phục 5 ca — kiểm mỗi dòng có cách phát hiện **đo được** (tên event + ngưỡng + tần suất) và **một vai trò** phụ trách.

**CP4 · D2 (16:08–16:36)**

- [ ] Trả lời 5 câu "tách được tác động", mỗi câu một dòng, ghi vào chú thích `pilot_plan.yaml`: đối chứng chạy cùng thời gian? ngẫu nhiên hay người chọn? ảnh hưởng gián tiếp và cách giảm? chỉ số/ngưỡng/ngày quyết định đã viết trước chưa? ≥ 20 cụm mỗi nhóm?

**CP5 · chỉ số và event (16:36–17:00)**

- [ ] Điền bảng E1 trong `report/team/chi_so.md` với 3 số của Nhài, kèm công thức.
- [ ] Đề xuất thêm **1 chỉ số dùng** và **1 chỉ số an toàn** (không cần tính số).
- [ ] Liệt kê **≥ 6 event**, mỗi event có Ai tạo · Thuộc tính chính (bắt buộc có `trace_id`) · Thời điểm. Nên có: tạo yêu cầu, agent chạy xong (mọi lần kể cả lỗi), gợi ý hiện ra, nhân viên quyết định xem lại, ghi sổ cái, chuyển nhân viên, đóng ticket, mở lại ticket, kiểm tra mẫu.
- [ ] **Kiểm tra chéo:** với từng chỉ số ở E1, ghi rõ dùng event nào để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được — phải thêm event hoặc bỏ chỉ số.
- [ ] Soát ngôn từ: chỉ viết "chỉ số **trong đợt chạy thử** là …", **không** viết "trợ lý đã nâng chỉ số từ 0,70" (đợt chạy thử không có nhóm đối chứng).

**Trước khi nộp**

- [ ] `grep -rni "cả đội" report/team` và `grep -rni production report/team` — cả hai không in gì.
- [ ] Tạo `report/team/2A202603939_NgoNgocHai.md`.
- [ ] Nộp link repo nhóm trên LMS.

---

### 3.4 Trần Hải Long — 2A202603891 — người gắn nhãn 2, kiêm giữ hồ sơ

Bạn giữ file quyết định phần lớn 30 điểm hội đồng. **Điền dần từ 14:10, không đợi 16:36.**

**14:10 — mở hồ sơ ngay**

- [ ] Mở `report/team/ho_so_launch_v0.md`, điền tên nhóm và lớp L3B.
- [ ] Mỗi mục trong 7 mục có 3 ô phải điền: **con số chính · trạng thái · người phụ trách (một vai trò)**.
- [ ] Trạng thái chỉ nhận đúng 3 giá trị: **Xong, có bằng chứng** · **Chưa** · **Giả lập**. Mục 1, 2, 3, 7 dựa trên cột `_simulated` → ghi **Giả lập**.

**Điền theo tiến độ**

- [ ] Mục 1 (chi phí mỗi việc thành công) + mục 3 (so với nhân viên tự làm) — ngay khi Đức có số A2 và A4. Ghi rõ con số **đã cộng chi phí cố định hay chưa, và ở khối lượng nào**.
- [ ] Mục 2 (ba yếu tố nhạy nhất) — sau CP2.
- [ ] Mục 5 (bảng lỗi) — sau CP3, ghi tỉ lệ đồng thuận.
- [ ] Mục 6 (pilot plan) — sau CP4, ghi cỡ mẫu và cách chia nhóm đã chọn.
- [ ] Mục 4 (ba chỉ số) và mục 7 (rủi ro) — sau CP5.

**CP3 · gắn nhãn (15:35–15:43)**

- [ ] Gắn nhãn 20 ca độc lập trong 8 phút, **không trao đổi với Hải**, không nhìn bài nhau.
- [ ] Sau khi so nhãn, chọn **5 ca, mỗi loại lỗi đúng 1 ca**, điền bảng khắc phục: cách phát hiện phải có **tên event + ngưỡng + tần suất**; người phụ trách là **một vai trò có quyền quyết định**.

**CP4–CP5 · phạm vi và rủi ro**

- [ ] Viết `scope` cho `pilot_plan.yaml`: chỉ `noi_dia` và `hang_nang`, **kèm số bội so với 12.000 đ của từng loại và lý do loại `quoc_te`, `doi_tac`** (tiêu chí C7 chỉ cho 10 điểm khi phạm vi thu hẹp **có lý do bằng số**).
- [ ] Viết **≥ 2 dòng rủi ro kinh tế** trong `chi_so.md`, số lấy trực tiếp từ bảng độ nhạy, mỗi dòng đủ 5 cột: rủi ro · tác động đã tính · dấu hiệu theo dõi (có ngưỡng) · hành động · người phụ trách.
- [ ] **Chốt đề xuất** ở dòng cuối hồ sơ: đúng một trong **Go · Go có điều kiện · No-go**.
  - Chọn "Go có điều kiện" → mỗi điều kiện phải có **người phụ trách và ngày kiểm tra**.
  - Chọn "No-go" → ghi **việc phải làm để quay lại cổng**.
  - Bắt buộc nêu **con số bất lợi** của nhóm và cách xử lý: nêu được thì 10 điểm C6, bỏ qua chỉ 5 điểm. **No-go có lý do bằng số được điểm cao hơn Go bỏ qua số bất lợi.**

**17:00–17:25 · làm hội đồng**

- [ ] Nhận hồ sơ nhóm n + 1, điền `report/team/phieu_cham.md`: 3 tiêu chí × (0/5/10), mỗi ô **Lý do phải có số**.
- [ ] Viết 1 câu hỏi cho đội trình. Ba câu dùng được: "Chi phí mỗi việc thành công bao nhiêu nếu tuần đầu phải xem lại 100%?" · "Cách chia của nhóm có ≥ 20 cụm mỗi nhóm không?" · "Với tỉ lệ mở lại hiện tại, ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?"
- [ ] Ghi lại câu trả lời của đội trình vào phiếu, điền tổng `… / 30`.

**Trước khi nộp**

- [ ] Hồ sơ đúng **một trang**, đủ **7 mục**, không mục nào còn để `...`.
- [ ] Tạo `report/team/2A202603891_TranHaiLong.md`.
- [ ] Nộp link repo nhóm trên LMS.

---

## 4. Duyệt chéo trong nhóm — ai kiểm bài của ai

Không ai tự duyệt file của chính mình. Làm trong 10 phút lúc 16:50.

| File | Người viết | Người duyệt | Duyệt cái gì |
| --- | --- | --- | --- |
| `src/lab13.py` | Đức | Nhài | Chạy được trên máy khác, 3 phép thử ĐẠT |
| `bang_chi_phi.md` | Đức | Nhài | A2 đủ 9 dòng, 2 dòng giả lập có nhãn; B1 đủ 9 dòng, đối xứng gấp đôi ↔ giảm nửa |
| `bang_loi.md` | Hải | Long | Hai bộ nhãn độc lập còn nguyên, đồng thuận ≥ 80%, bảng khắc phục đủ 5 loại |
| `pilot_plan.yaml` | Đức + Nhài | Hải | `yaml.safe_load` chạy được, hết dấu `?`, 3 luật dừng đủ 4 vế |
| `chi_so.md` | Hải + Long | Đức | 3 chỉ số có số, ≥ 6 event đều có `trace_id`, ≥ 2 dòng rủi ro |
| `ho_so_launch_v0.md` | Long | Đức | 7 mục đủ 3 ô, đề xuất là 1 trong 3, có nêu số bất lợi |
| `phieu_cham.md` | Long | Hải | Mỗi lý do có số |
| `group_report.md` | Đức | Long | 8 mục, dẫn lại con số chính |

---

## 5. Quy trình git (repo đã có sẵn, chủ repo là `tmduc23`)

Mỗi người làm trên nhánh riêng, **không ai push trực tiếp vào `main`** trừ nhóm trưởng khi merge.

```bash
git pull origin main
git checkout -b duc/cp1-chi-phi        # nhai/cp4-co-mau · hai/cp3-nhan-loi · long/cp5-ho-so
# ... làm việc ...
git add -A
git commit -m "CP1: mo hinh chi phi moi viec thanh cong"
git push -u origin duc/cp1-chi-phi
```

- [ ] Commit **sau mỗi checkpoint**, không dồn một commit cuối buổi — commit là bằng chứng đóng góp cho `TEAM.md` và báo cáo cá nhân.
- [ ] Hai người cùng sửa `pilot_plan.yaml` → sửa lần lượt, không song song (YAML conflict rất khó gỡ).
- [ ] Không commit `.venv/`, `.env`, API key. Không sửa `logix_runs.csv`, `logix_requests.csv`, `lab13_starter.py`.
- [ ] Nhóm trưởng merge các PR về `main` lúc 17:45, rồi chạy lại `lab13.py` một lần nữa trên `main`.

---

## 6. Hai checklist mốc cứng

### 17:00 — trước khi gửi hồ sơ cho nhóm hội đồng (Long gửi, Đức duyệt)

- [ ] `ho_so_launch_v0.md` đủ 7 mục, mỗi mục có con số + trạng thái + một vai trò.
- [ ] Dòng cuối là đề xuất Go / Go có điều kiện / No-go.
- [ ] `grep -rni production report/team` → không in gì.
- [ ] `grep -rni "cả đội" report/team` → không in gì.

### 17:45 — trước khi nộp (nhóm trưởng chạy, 3 người còn lại xác nhận)

```bash
cd src && python lab13.py                    # 3 phép thử in ĐẠT, bảng A2 in ra
python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"
grep -v '^ *#' ../report/team/pilot_plan.yaml | grep -n '?'   # không in gì
cd .. && grep -rni production report/team    # không in gì
```

- [ ] Đủ **6 file hồ sơ** trong `report/team/`, giữ **nguyên tên**: `bang_chi_phi.md`, `bang_loi.md`, `pilot_plan.yaml`, `chi_so.md`, `ho_so_launch_v0.md`, `phieu_cham.md`.
- [ ] `group_report.md` đã điền; `TEAM.md` đủ 4 dòng thành viên + vai + đóng góp.
- [ ] **4 file báo cáo cá nhân** đã tạo đúng tên và `MSSV_HoTen.md` mẫu vẫn còn:
  - [ ] `report/team/2A202603977_TranMinhDuc.md`
  - [ ] `report/team/2A202603911_TranThiNhai.md`
  - [ ] `report/team/2A202603939_NgoNgocHai.md`
  - [ ] `report/team/2A202603891_TranHaiLong.md`
- [ ] ≥ 3 luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- [ ] Mọi con số từ cột `_simulated` có nhãn `simulated`.
- [ ] Đã push `main`; repo mở được cho người chấm.
- [ ] **Cả 4 người đã nộp cùng link repo trên LMS trước 23h59 GMT+7.**

---

## 7. Phân vai 3 phút bảo vệ trước hội đồng

| Thứ tự | Ai | Nói gì (tối đa) |
| --- | --- | --- |
| 1 | **Đức** | 1 phút trình: chi phí mỗi việc thành công (có nhãn `simulated`), bội số so với 12.000 đ, phạm vi đã thu hẹp và lý do bằng số, đề xuất cuối. |
| 2 | **Nhài** | Trả lời mọi câu về số: cỡ mẫu, hệ số thiết kế, vì sao mẫu số chỉ đếm việc thành công. |
| 3 | **Hải** | Trả lời về bảng lỗi, chỉ số, và event nào dùng để tính chỉ số nào. |
| 4 | **Long** | Trả lời về luật dừng, ngưỡng an toàn so với tỉ lệ mở lại hiện tại, và điều kiện kèm đề xuất. |

Ba câu hỏi gần như chắc chắn bị hỏi — mỗi người chuẩn bị sẵn **một con số** cho câu của mình:

1. "Vì sao tử số cộng cả lần chạy lỗi mà mẫu số chỉ đếm việc thành công?" → **Nhài**.
2. "Cách chia nhóm của các bạn có ≥ 20 cụm mỗi nhóm không? Nếu không thì đánh đổi là gì?" → **Long** (dẫn số của Nhài).
3. "Ngưỡng an toàn của nhóm có làm pilot dừng ngay tuần đầu không?" → **Long**.

---

## 8. Dự phòng

| Tình huống | Xử lý |
| --- | --- |
| Máy ai đó không cài được Python / pandas | Người đó chuyển sang việc không cần code (gắn nhãn, giữ hồ sơ, soát chữ); **ghi lỗi + lệnh đã chạy + output vào mục 5 `group_report.md`** để không mất điểm. |
| Ba phép thử A1 chưa ĐẠT sau 15 phút | Dừng mọi việc khác, Đức + Nhài cùng soát công thức `(1 − (1 − p)^k) / p`. Sai ở A1 làm sai toàn bộ A–E. |
| Đồng thuận gắn nhãn < 80% | Không sửa hai bộ nhãn cũ. Viết lại định nghĩa 5 loại, ghi bản định nghĩa mới vào `bang_loi.md`, nêu rõ trong báo cáo. |
| Cách chia nhóm nào cũng không đủ mẫu | Đó là kết quả đúng của bài. Chọn một cách, **ghi rõ đánh đổi đã chấp nhận** (ví dụ nâng mức chênh cần phát hiện) và nêu con số power bất lợi trong hồ sơ. |
| Thiếu thời gian lúc 16:50 | Ưu tiên theo điểm: `pilot_plan.yaml` (15đ + 10đ hội đồng) → `ho_so_launch_v0.md` (10đ + 20đ hội đồng) → `chi_so.md` → `phieu_cham.md`. Mục nào chưa làm thì ghi trạng thái **Chưa**, không bỏ trống. |

---

## 9. Số để tự đối chiếu (chỉ dùng để kiểm, không được chép)

[RULES.md](RULES.md) yêu cầu mọi con số phải do `src/lab13.py` của nhóm tính ra. Các mốc dưới đây có trong [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md); dùng để biết mình có sai không, và **cả nhóm phải giải thích được vì sao ra số đó**.

| Mốc | Giá trị | Ai dùng |
| --- | --- | --- |
| Ba phép thử A1 | 1,20 · 1,25 · 1,25 | Đức, Nhài |
| Chi phí mỗi việc thành công (A2) | ~4.472 đ, gấp ~16,3× hoá đơn chia số yêu cầu | Đức, Nhài, Long |
| Khoản lớn nhất | làm lại ~51,8%, rồi xem lại ~40,7%; giờ nhân viên ~92,5% tổng chi phí | Long (mục 1 hồ sơ) |
| Loại không đáng xử lý (A3) | `quoc_te` ~1,88× và thành công ~27,3%; chạy lại 3 lần không giúp | Long (`scope`) |
| Ba yếu tố nhạy nhất (B) | 1. số ca làm lại · 2. tỉ lệ xem lại · 3. lương nhân viên | Long (mục 2 hồ sơ) |
| Giới hạn rẻ nhất cho công ty (B3) | 2 lần — **không** trùng với giới hạn cho chi phí mỗi việc thấp nhất (1 lần) | Đức |
| Xem lại 100% (B4) | ~0,98× của 12.000 đ, lên ~1,03× nếu dùng số phút làm lại thực trong dữ liệu | Long (rủi ro E2) |
| Cỡ mẫu chia theo yêu cầu (D1a) | ~1.251 mỗi nhóm | Nhài |
| 20 nhân viên mỗi nhóm (D1c) | trần 1.000 < 1.251 → **không đạt** mức chênh 5 điểm | Nhài, Long |
| 6 depot mỗi nhóm (D1d) | trần 300 → loại cách chia theo depot | Nhài |
| Ba chỉ số (E1) | chính ~82,83% · bỏ qua gợi ý ~27,12% · mở lại 7 ngày ~4,25% | Nhài, Hải |

Số của nhóm lệch không quá 2% so với slide chữa thì được nhận. Lệch nhiều hơn → sửa ngay tại checkpoint đó, **đừng để dồn sang nhiệm vụ sau** vì nhiệm vụ sau dùng lại số của nhiệm vụ trước.
