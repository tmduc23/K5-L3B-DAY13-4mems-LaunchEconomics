# Báo cáo nhóm

Báo cáo ngắn, tối đa 2 trang. Số liệu chi tiết nằm trong các file hồ sơ; ở đây chỉ dẫn lại con số chính. Toàn bộ dữ liệu của lab là giả lập; mọi số tính từ hai cột `_simulated` đều ghi nhãn `simulated`.

## 1. Thông tin nhóm

- Tên nhóm: 4mems
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md)

## 2. Mục tiêu và cách tiếp cận

Dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để trả lời bốn câu: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot thiết kế thế nào để ra được quyết định.

Cách tiếp cận: đo chi phí thật từ trace thay vì từ hoá đơn token, rồi dùng chính các con số đó làm căn cứ cho phạm vi pilot, ngưỡng theo dõi và luật dừng. Nhóm chia bốn vai theo [PHAN_CONG.md](../../PHAN_CONG.md) và đổi người viết code sau giờ giải lao để hai người tự tay tính được chi phí.

## 3. Giải pháp

| Nhiệm vụ | Cách làm | File |
| --- | --- | --- |
| A · Mô hình chi phí | Viết ba hàm kinh tế chạy lại, rồi `mo_hinh()` cộng token và tool trên **mọi** lần chạy kể cả lần lỗi, chia cho số yêu cầu `thanh_cong`; tách theo `loai`; cộng chi phí cố định cho phạm vi pilot | [src/lab13.py](../../src/lab13.py), [bang_chi_phi.md](bang_chi_phi.md) |
| B · Độ nhạy | Gọi lại `mo_hinh()` cho 9 kịch bản một yếu tố, 1 kịch bản cặp, 3 mức giới hạn số lần chạy, và kịch bản xem lại 100% | [bang_chi_phi.md](bang_chi_phi.md) |
| C · Bảng lỗi | Hai người gắn nhãn 20 ca độc lập trong 8 phút, không trao đổi, rồi so nhãn và gán cách khắc phục cho từng loại | [bang_loi.md](bang_loi.md) |
| D · Pilot plan | Tính cỡ mẫu cho ba cách chia **trước khi** chọn, kiểm năm câu tách được tác động, tính tỉ lệ nền của chỉ số an toàn trước khi đặt ngưỡng | [pilot_plan.yaml](pilot_plan.yaml) |
| E · Chỉ số và rủi ro | Ba chỉ số tính thử, 10 event đều có `trace_id`, kiểm tra chéo chỉ số ↔ event, hai dòng rủi ro kinh tế lấy số từ bảng độ nhạy | [chi_so.md](chi_so.md), [ho_so_launch_v0.md](ho_so_launch_v0.md) |

## 4. Kết quả

**Chi phí.** Chi phí mỗi việc thành công là **4.472 đ** [simulated], **gấp 16,3 lần** hoá đơn token chia số yêu cầu (274,7 đ). Giờ nhân viên chiếm 92,5% tổng chi phí: làm lại 51,8%, xem lại 40,7%; token và tool chỉ 7,5%. So với nhân viên tự làm 12.000 đ, con số công bằng là chi phí cả hệ thống **5.865 đ/yêu cầu = 0,49×** vì phải tính cả 222 yêu cầu nhân viên làm thay.

**Phạm vi.** Tách theo loại: `noi_dia` 0,22× · `hang_nang` 0,69× · `doi_tac` 0,85× · `quoc_te` **1,88×** với tỉ lệ thành công chỉ 27,3%, và chạy lại không giúp (tỉ lệ đúng tụt 30,0% → 11,4% → 2,2%). Pilot vì vậy thu hẹp còn `noi_dia` + `hang_nang`, nơi chi phí cộng cả cố định và phần nhân viên làm thay là **5.217 đ = 0,43×** [simulated].

**Yếu tố nhạy nhất.** Số ca làm lại (±51,8%) → tỉ lệ xem lại (±40,7%) → lương nhân viên (+23,1%). Giá token chỉ ±5,6%, nên pilot theo dõi tỉ lệ làm lại và xem lại, không theo dõi hoá đơn token. Giới hạn 2 lần chạy rẻ nhất cho công ty (6.901.220 đ) nhưng **không** trùng giới hạn cho chi phí mỗi việc thành công thấp nhất (1 lần).

**Lỗi.** Hai bộ nhãn độc lập đồng thuận **20/20 = 100%**, khớp đáp án cả 20 ca; bảng khắc phục 5 ca đủ năm loại, mỗi dòng có event, ngưỡng, tần suất và một vai trò phụ trách.

**Chỉ số trong đợt chạy thử.** Chỉ số chính 82,83% (994/1.200) · bỏ qua gợi ý 27,12% (48/177) · mở lại trong 7 ngày 4,25% (51/1.200). Đợt chạy thử không có nhóm đối chứng nên nhóm chỉ kết luận "chỉ số trong đợt chạy thử là…", không kết luận trợ lý đã nâng chỉ số.

**Pilot.** Chia theo nhân viên, 20 người mỗi nhóm, phân tầng theo depot. Không cách chia nào đủ mẫu cho mức chênh 5 điểm (trần 1.000 < 1.251), nên nhóm chấp nhận mức chênh **6 điểm**: n = 859/nhóm, DE 6,96, 20 cụm mỗi nhóm. Con số bất lợi đã nêu rõ: nếu tác động thật chỉ 5 điểm thì **power còn 0,64**.

**Đề xuất cuối:** **Go có điều kiện** cho pilot `noi_dia` + `hang_nang`, với ba điều kiện có người phụ trách và ngày kiểm tra, kèm hai con số bất lợi: xem lại 100% đẩy chi phí lên **1,03–1,04×** mốc thủ công, và power 0,64 ở mức chênh 5 điểm.

**Kết quả duyệt chéo Gate 2a:** Hội đồng là nhóm **teamrandom** (L3B), chấm trên commit `18cc364`. Kết quả **30/30**, quyết định **Go có điều kiện**.

| Tiêu chí | Điểm | Nhận xét của hội đồng |
| --- | ---: | --- |
| C6 · Đề xuất khớp bằng chứng | 10/10 | Khớp với số của nhóm (4.472 đ/việc thành công; 5.217 đ = 0,43× trong phạm vi khi đã cộng cố định và 82 ca nhân viên làm thay), có nêu cả hai số bất lợi kèm cách xử lý. **Yêu cầu làm rõ:** điều kiện 3 ghi “đủ 859 yêu cầu mỗi nhóm” trong khi `pilot_plan.yaml` ghi cần ≥ 5.980 yêu cầu thực tế (859 là mẫu hiệu dụng). |
| C7 · Số giả lập và phạm vi | 10/10 | Phạm vi thu hẻp có số đỡ (`quoc_te` 1,88× và thành công 27,3%; `doi_tac` 0,85×), nhãn `simulated` đủ ở mục 1, 2, 3, 7, bảng chi phí, E2 và `simulated_inputs`. **Thiếu nhãn:** hai số 1,88× và 0,85× ở mục 6 của hồ sơ. |
| C8 · Pilot ra được quyết định | 10/10 | Đối chứng cùng thời gian cùng depot, bốc thăm bằng code có seed, đủ 20 cụm mỗi nhóm; đủ mẫu cho MDE 6 điểm. **Điểm yếu:** luật dừng 1 gộp ca hoàn trùng vào vế “TRONG 3 ngày liên tiếp” thay vì dừng ngay khi có 1 ca; `interim_looks` còn là câu mẫu. |

**Câu hỏi hội đồng đặt:** Điều kiện 3 ghi “chỉ ra quyết định khi bước 0,50 đo đủ 859 yêu cầu mỗi nhóm”, nhưng `pilot_plan.yaml` ghi cần ít nhất 5.980 yêu cầu mỗi nhóm (20 người × 299). Ngưỡng ra quyết định thật là bao nhiêu, và với 2 tuần ở bước 0,50 cộng 7 ngày theo dõi mở lại thì nhóm có đủ dữ liệu trước ngày quyết định 2027-01-12 không?

**Câu trả lời của nhóm tại buổi:** Ngưỡng ra quyết định thật là **5.980 yêu cầu thực tế mỗi nhóm** (`m ≥ 299` yêu cầu/người × 20 người). Con số **859** là **cỡ mẫu hiệu dụng**, tức 5.980 chia hệ số thiết kế **6,96**; hai số nói về cùng một điều kiện chứ không phải hai ngưỡng khác nhau. Hội đồng đúng ở chỗ điều kiện 3 của hồ sơ chỉ ghi 859 nên đọc ra thành số yêu cầu phải thu, mâu thuẫn với mục 6 của chính hồ sơ và với `pilot_plan.yaml` — **nhóm đã sửa**, điều kiện 3 nay ghi cả hai số và nói rõ quan hệ giữa chúng.

Về thời gian: nhóm **không khẳng định chắc chắn đủ dữ liệu** trước 2027-01-12. Pilot bắt đầu 2026-12-01, ba bước rollout mỗi bước một tuần, đo chỉ số chính từ bước 0,50, cộng 7 ngày theo dõi mở lại — phần còn lại đủ hay không phụ thuộc lưu lượng yêu cầu thực tế mỗi nhân viên mỗi ngày, mà đó là số nhóm **chưa đo được** từ dữ liệu đợt chạy thử. Vì vậy điều kiện 3 gắn quyết định vào **điều kiện đủ mẫu**, không gắn vào ngày: chỉ ra quyết định khi đã đo đủ 5.980 yêu cầu mỗi nhóm. Nếu đến 2027-01-12 chưa đủ thì gia hạn, chứ không kết luận trên mẫu thiếu. Đây là điểm yếu nhóm đã nêu trong hồ sơ chứ không che.

**Nhóm đã làm gì với ba ý trên:** xem mục 5.5 dưới đây.

**4mems làm hội đồng cho nhóm nào:** 4mems chấm **teamrandom**, kết quả 30/30 và quyết định Go có điều kiện, ghi đầy đủ trong `report/team/phieu_cham.md`. Câu hỏi 4mems đặt cho teamrandom: ngưỡng 8.000 đ của luật dừng 3 đặt trên số gộp cả phạm vi, trong khi `hang_nang` đứng riêng đã là 8.221 đ nên luật đó có thể không bao giờ kích hoạt.

## 5.5 Ba ý hội đồng nêu và nhóm đã làm gì

Nhóm teamrandom cho 30/30 nhưng nêu ba chỗ cần sửa. Nhóm kiểm lại và xác nhận **cả ba đều đúng**.

**1. Điều kiện 3 ghi sai ngưỡng ra quyết định — đã sửa.** Bản trước ghi “đo đủ 859 yêu cầu mỗi nhóm”, trong khi 859 là **mẫu hiệu dụng**, còn số yêu cầu thực tế cần thu là **5.980 mỗi nhóm** (`m ≥ 299` × 20 người) — đúng như mục 6 của chính hồ sơ và `pilot_plan.yaml` đã ghi. Đây là mâu thuẫn nội bộ trong cùng một file, lọt ra khi nhóm viết lại điều kiện 3 ở phút cuối. Điều kiện 3 nay ghi cả hai số và nói rõ quan hệ giữa chúng qua hệ số thiết kế 6,96.

**2. Mục 6 thiếu nhãn `simulated` ở hai số 1,88× và 0,85× — đã sửa.** Hai số này dẫn xuất từ chi phí tính trên các cột `_simulated` nên phải mang nhãn; cùng hai số ấy ở `pilot_plan.yaml` và `bang_chi_phi.md` đã có nhãn từ trước, riêng mục 6 bị sót. Theo rúbric, số giả lập thiếu nhãn bị trừ điểm, nên đây là ý đáng giá nhất trong ba ý.

**3. Luật dừng 1 gộp ca hoàn trùng vào vế “TRONG 3 ngày liên tiếp” — đã sửa.** Hội đồng đúng về mặt thiết kế: một ca hoàn tiền trùng đã đối soát là lỗi tiền bạc, phải tắt ngay khi có 1 ca chứ không chờ đủ 3 ngày như ngưỡng tỉ lệ mở lại. Nhóm đã **tách hoàn trùng thành luật dừng riêng**, vế TRONG là “bất kỳ ngày nào của pilot, xử lý ngay khi xác nhận”, vế KHÔNG THÌ là không được bật lại khi nguyên nhân chưa sửa và Giám đốc vận hành chưa phê duyệt; luật mở lại 7 ngày giữ vế “3 ngày liên tiếp” của riêng nó. `pilot_plan.yaml` nay có **bốn luật dừng**, và `interim_looks` được viết lại cụ thể: chỉ số nào xem, tần suất nào, ai báo ai, và vì sao không xem chỉ số chính giữa kỳ. Bốn chỗ khác trong `report/team/` ghi “3 luật dừng” cũng được sửa theo trong cùng một lần, để không tạo thêm mâu thuẫn giữa các file như hai ý trên.

Bài học chung từ ba ý: hai ý đầu đều là **mâu thuẫn giữa hai file của chính nhóm**, không phải sai phép tính. Khi bốn người sửa song song ở phút cuối, rủi ro lớn nhất không phải tính sai mà là hai chỗ ghi hai số khác nhau cho cùng một đại lượng.

## 5. Khó khăn và cách xử lý

**1. Console Windows cp1252 làm code crash dù code đúng.** `python lab13.py` báo `UnicodeEncodeError: 'charmap' codec can't encode character 'ử'` ngay tại dòng in "ĐẠT", dù ba phép thử đã đạt. Lệnh kiểm YAML trong đề bài, `python -c "import yaml; yaml.safe_load(open('../report/team/pilot_plan.yaml'))"`, báo `UnicodeDecodeError: 'charmap' codec can't decode byte 0x90`, kể cả với file mẫu chưa sửa — nguyên nhân là `open()` mặc định dùng codepage hệ thống chứ không phải UTF-8.

Xử lý tạm thời: đặt `$env:PYTHONIOENCODING="utf-8"` hoặc chạy `python -X utf8`. Xử lý chính thức: thêm vào `src/lab13.py` hai dòng

```python
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
```

nhờ đó `python lab13.py` chạy hết và exit 0 trên máy Windows mà không cần đặt biến môi trường. Người chấm trên Windows nên dùng `python -X utf8 -c "import yaml; …"` cho lệnh kiểm YAML.

**2. Bốn người sửa song song gây conflict.** Hai lần conflict trên `report/team/chi_so.md` và `report/team/pilot_plan.yaml` vì hai người điền hai mục khác nhau của cùng file, và một lần trên báo cáo cá nhân. Xử lý: giữ cả hai bên khi nội dung không chồng nhau, và với file thuộc một người thì giữ bản của chính người đó. Nhóm cũng thống nhất không sửa song song `pilot_plan.yaml`.

**3. Một ca nhãn bị nhập sai.** Khi nhập bộ nhãn 2 vào `bang_loi.md`, ca 8 bị ghi lệch so với bản gắn nhãn gốc, làm tỉ lệ đồng thuận hiện ra 19/20. Người gắn nhãn 2 tự phát hiện và sửa lại theo bản ghi của mình (commit `abc3ada`, "fix wrongly uploaded labels"), sau đó nhóm đồng bộ các file dẫn lại con số. Hai cột nhãn độc lập không bị sửa vì lý do khác ngoài việc chép lại cho đúng bản gốc.

**4. Không cách chia nhóm nào đủ mẫu.** Với 40 nhân viên CSKH, cả ba cách chia đều không đạt cỡ mẫu cho mức chênh 5 điểm. Xử lý: tính đủ năm câu cỡ mẫu trước khi chọn, rồi chọn cách chia theo nhân viên và ghi rõ đánh đổi cùng power còn lại trong hồ sơ, thay vì chọn cách dễ triển khai nhất.

## 6. Tổng hợp đóng góp

Chi tiết đóng góp của từng thành viên nằm trong [TEAM.md](../../TEAM.md).

- Trần Minh Đức (2A202603977) — nhóm trưởng, người viết code phiên 1: nhiệm vụ A và B, các trường và bốn luật dừng của pilot plan, điều phối và đóng gói bài nộp.
- Trần Thị Nhài (2A202603911) — người kiểm số, người viết code phiên 2: kiểm số A và B, năm câu cỡ mẫu D1, tỉ lệ nền của chỉ số an toàn, ba chỉ số E1.
- Ngô Ngọc Hải (2A202603939) — người gắn nhãn 1: bộ nhãn 1 và bảng khắc phục, đặc tả chỉ số và danh sách event, năm câu D2.
- Trần Hải Long (2A202603891) — người gắn nhãn 2, kiêm giữ hồ sơ: bộ nhãn 2, hồ sơ launch v0 bảy mục và đề xuất cuối, phạm vi pilot, rủi ro kinh tế E2.

## 7. Hạn chế và hướng cải thiện

- **Số giờ nhân viên là giả lập.** Hai cột `_simulated` quyết định 92,5% tổng chi phí, nên mọi kết luận về chi phí chỉ đúng nếu số phút thật gần số giả lập. Tuần 1 của pilot phải thay bằng phút đo thật từ event `staff_review_decision` và `staff_rework_completed`.
- **Pilot không phát hiện được mức chênh 5 điểm.** Chấp nhận mức 6 điểm là đánh đổi có ý thức, power còn 0,64 ở mức 5 điểm. Muốn phát hiện 5 điểm thì phải tăng số cụm, tức mở rộng ngoài 40 nhân viên hiện có.
- **Kịch bản xem lại 100% chưa có lời giải.** Ở mức đó chi phí là 1,03–1,04× mốc thủ công, tức trợ lý không tiết kiệm được gì. Cần học xem tỉ lệ xem lại giảm an toàn tới đâu và một lần xem lại có ngắn hơn 5,1 phút được không.
- **Kiểm số chưa hoàn toàn độc lập.** Phần kiểm A2 lấy tổng cột bằng pandas thay vì tính tay, nên chỉ phát hiện được lỗi công thức, không phát hiện được lỗi đọc dữ liệu chung cho cả hai bên.

## 8. Tài liệu tham khảo

- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*, <https://arxiv.org/abs/2504.13359>
- Google PAIR, *People + AI Guidebook*, chương "Errors + Graceful Failure", <https://pair.withgoogle.com>
- Tài liệu `statsmodels`, lớp `NormalIndPower` (mục `stats.power`)
- Tài liệu lab: [docs/du_lieu_va_cong_thuc.md](../../docs/du_lieu_va_cong_thuc.md), [docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- Trợ lý AI: Claude Code, dùng để gợi ý code và soát lỗi; cách từng thành viên tự kiểm tra ghi trong báo cáo cá nhân.
