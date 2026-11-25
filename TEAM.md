# Team

## Thông tin nhóm

- Tên nhóm: 4mems
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-4mems-LaunchEconomics`
- URL repo, nhánh nộp, commit chốt: <https://github.com/tmduc23/K5-L3B-DAY13-4mems-LaunchEconomics> · nhánh `main` · commit chốt: _(điền hash commit cuối cùng lúc 17:45)_

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Trần Minh Đức (nhóm trưởng) | 2A202603977 | tranminhduc2324@gmail.com | `tmduc23` | Người viết code phiên 1 (nhiệm vụ A, B) · chủ repo, điều phối, chốt nộp |
|   2 | Trần Thị Nhài | 2A202603911 | nhainhinhanh6a@gmail.com | `chanhochust` | Người kiểm số (A, B) · người viết code phiên 2 (D1 cỡ mẫu, E1 chỉ số) |
|   3 | Ngô Ngọc Hải | 2A202603939 | ngongochai0804@gmail.com | `NgoHai0804` | Người gắn nhãn 1 · phụ trách đặc tả chỉ số và danh sách event |
|   4 | Trần Hải Long | 2A202603891 | longhtr028@gmail.com | `longhtr028` | Người gắn nhãn 2, kiêm giữ hồ sơ launch v0 |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Nhóm đã đổi người viết code sau giờ giải lao: Trần Minh Đức viết phần A và B (CP1, CP2), Trần Thị Nhài nhận code từ 15:35 và viết phần D1, E1 (CP4, CP5). Phân công chi tiết theo checkpoint: [PHAN_CONG.md](PHAN_CONG.md).

## Cá nhân

Mỗi thành viên đồng thời tạo một báo cáo riêng trong `report/` theo dạng:

```text
report/team/MSSV_HoTen.md
```

Ví dụ: `report/team/20241234_NguyenVanAn.md`.

Sao chép mục dưới đây cho từng thành viên.

## TranMinhDuc-2A202603977

### Phần việc phụ trách

- `src/lab13.py`: ba hàm A1, `mo_hinh()`, A3 tách theo `loai`, A4 chi phí cố định, B1–B4 bảng độ nhạy.
- `report/team/bang_chi_phi.md`: bảng A1, A2, A3, A4 và các câu trả lời B2, B3, B4.
- `report/team/pilot_plan.yaml`: các trường của kế hoạch và ba luật dừng.
- Vai nhóm trưởng: chủ repo, phân công, merge nhánh, soát 6 file hồ sơ, `TEAM.md`, `group_report.md`, chốt push và nhắc nộp LMS.

### Đóng góp cụ thể

- A1: ba phép thử đáp án biết trước ĐẠT (1,20 · 1,25 · 1,25).
- A2: chi phí mỗi việc thành công **4.472 đ** [simulated], gấp 16,3 lần hoá đơn token chia số yêu cầu (274,7 đ); khoản lớn nhất là làm lại 51,8%.
- A3: `quoc_te` 1,88× và thành công 27,3%, chạy lại 3 lần không giúp (30,0% → 11,4% → 2,2%) → đề nghị loại khỏi phạm vi.
- A4: chi phí cố định 1.185 đ/việc ở 45.000 yêu cầu/tháng → 4.599 đ = 0,38×; còn một nửa khối lượng thì 2.370 đ/việc → 5.784 đ = 0,48×.
- B1–B4: xếp hạng ba yếu tố nhạy nhất (làm lại 51,8% · xem lại 40,7% · lương 23,1%); giới hạn 2 lần rẻ nhất cho công ty (6.901.220 đ) nhưng không trùng giới hạn cho chi phí mỗi việc thấp nhất; xem lại 100% là 0,98× và lên 1,03× nếu dùng số phút làm lại thực.
- CP4: điền `owner`, `assignment`, `rollout`, `identifiability`, `interim_looks`, `rollback`, `decision_date`, `simulated_inputs` và ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- Merge nhánh `hai` vào `main`, giữ cả hai bên không mất nội dung của ai.
- Sửa lỗi console cp1252 làm `python lab13.py` crash trên Windows, để file chạy được trên mọi máy.

### Bằng chứng

- Commit: `eed8a92` (A1–A4, B1–B4), `c121a7e` (CP4), `32aea05` (merge nhánh `hai`), `a4e5589` (`PHAN_CONG.md`).
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`, `TEAM.md`, `PHAN_CONG.md`.

## TranThiNhai-2A202603911

### Phần việc phụ trách

- Kiểm số độc lập cho nhiệm vụ A và B; cột Nguồn và Nhãn của bảng A2; 9 dòng bảng độ nhạy B1.
- `src/lab13.py` từ sau giờ giải lao: `co_mau()` và năm câu D1, tỉ lệ `mo_lai_trong_7_ngay`, ba chỉ số E1.
- `report/team/pilot_plan.yaml`: chú thích D1, khối đánh đổi đã chấp nhận, và các trường `n_per_arm`, `design_effect`, `clusters_per_arm`.

### Đóng góp cụ thể

- Kiểm số A2: đối chiếu tay các khoản token, tool, xem lại, làm lại; điền cột Nguồn và Nhãn, đảm bảo hai dòng giả lập có nhãn `simulated`.
- Nhập đủ 9 dòng bảng B1 và kiểm tính đối xứng giữa các cặp "gấp đôi" và "giảm một nửa".
- D1: cỡ mẫu theo yêu cầu 1.251/nhóm; theo nhân viên m = 75 cần 3.103/nhóm nên không đủ người; 20 nhân viên mỗi nhóm chỉ đạt trần 1.000 < 1.251; 6 depot mỗi nhóm trần 300; mức chênh 6 điểm cần m ≥ 299 yêu cầu/người.
- Tính tỉ lệ `mo_lai_trong_7_ngay` hiện tại trước khi nhóm đặt ngưỡng an toàn, nhờ đó nhóm không đặt ngưỡng tuyệt đối thấp hơn tỉ lệ nền.
- E1: ba chỉ số tính thử — chỉ số chính 82,83% (994/1.200), bỏ qua gợi ý 27,12% (48/177), mở lại 7 ngày 4,25% (51/1.200).

### Bằng chứng

- Commit: `c17d643` (kiểm số A2 và B1), `81806e0` (D1 và tỉ lệ mở lại), `15b213c` (E1), `8f34de4` (cỡ mẫu và đánh đổi trong `pilot_plan.yaml`).
- File: `src/lab13.py`, `report/team/bang_chi_phi.md`, `report/team/pilot_plan.yaml`.

## NgoNgocHai-2A202603939

### Phần việc phụ trách

- Gắn nhãn độc lập 20 ca lỗi (bộ nhãn 1) và bảng khắc phục 5 ca trong `report/team/bang_loi.md`.
- `report/team/chi_so.md`: đặc tả chỉ số E1, hai chỉ số tự đề xuất, danh sách event, phần kiểm tra chéo chỉ số ↔ event.
- Năm câu D2 "tách được tác động" trong chú thích `report/team/pilot_plan.yaml`.

### Đóng góp cụ thể

- Gắn nhãn 20 ca độc lập trong 8 phút, không trao đổi với người gắn nhãn 2; đồng thuận 19/20 = 95%, vượt mốc 80%.
- Viết quy tắc phân biệt cho ca không trùng và bảng khắc phục 5 ca, mỗi loại lỗi một ca, mỗi dòng có cách phát hiện đo được (event, ngưỡng, tần suất) và một vai trò phụ trách.
- Đặc tả chỉ số E1 kèm công thức, thêm một chỉ số dùng và một chỉ số an toàn tự đề xuất.
- Liệt kê 10 event đều có `trace_id`, kèm kiểm tra chéo chỉ ra event nào dùng để tính chỉ số nào.
- Trả lời năm câu D2 làm căn cứ cho trường `identifiability` của kế hoạch pilot.

### Bằng chứng

- Commit: `f40107c` (bộ nhãn 1 và bảng khắc phục), `89075cf` (D2), `0ca730f` (E1, event, kiểm tra chéo), `dd7f8f8` (báo cáo cá nhân), `64c0ddc` (rà soát cách ghi người phụ trách).
- File: `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml`.

## TranHaiLong-2A202603891

### Phần việc phụ trách

- `report/team/ho_so_launch_v0.md`: giữ hồ sơ và điền dần từ đầu buổi, bảy mục và đề xuất cuối.
- Gắn nhãn độc lập 20 ca lỗi (bộ nhãn 2); chọn 5 ca cho bảng khắc phục.
- `report/team/chi_so.md` mục E2 rủi ro kinh tế; trường `scope` của `report/team/pilot_plan.yaml`.
- `report/team/phieu_cham.md` khi nhóm làm hội đồng Gate 2a.

### Đóng góp cụ thể

- Điền bảy mục của hồ sơ, mỗi mục có con số chính, trạng thái và một vai trò phụ trách; bốn mục dẫn từ cột `_simulated` ghi trạng thái Giả lập.
- Mục 3 dùng con số công bằng **5.217 đ/yêu cầu = 0,43×** của 12.000 đ (đã gồm chi phí cố định và 82/982 ca nhân viên làm thay) thay vì con số thuận lợi hơn.
- Viết `scope` thu hẹp về `noi_dia` và `hang_nang` kèm lý do bằng số cho cả bốn loại yêu cầu.
- E2: hai dòng rủi ro kinh tế lấy số từ bảng độ nhạy, mỗi dòng có ngưỡng theo dõi, hành động và một vai trò phụ trách.
- Chốt đề xuất **Go có điều kiện** với ba điều kiện có người phụ trách và ngày kiểm tra, nêu rõ hai con số bất lợi: xem lại 100% lên 1,03–1,04× và power còn 0,64 nếu tác động thật chỉ 5 điểm.

### Bằng chứng

- Commit: `d132d42` (hồ sơ mục 1–3 và 7, E2, `scope`), `09d7419` (hoàn thiện `bang_loi.md`, hồ sơ và báo cáo cá nhân).
- File: `report/team/ho_so_launch_v0.md`, `report/team/bang_loi.md`, `report/team/chi_so.md`, `report/team/pilot_plan.yaml`.
