# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | ... |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | ... |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | ... |
| Dùng | Nhóm tự đề xuất: ... | ... | Không cần tính |
| An toàn | Nhóm tự đề xuất: ... | ... | Không cần tính |

Viết "chỉ số trong đợt chạy thử là …", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |
| ... | ... | ..., trace_id | ... |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- ...

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1 trên toàn mẫu: **+51,8%**, lên **6.787 đ/việc thành công** [simulated]. | Tỉ lệ `lam_lai` trên các yêu cầu trong phạm vi đạt **9,8%** trong một tuần, khoảng gấp đôi mốc 48/982 ca trong đợt chạy thử. | Tạm hoãn tăng lưu lượng, rà trace ca làm lại theo loại yêu cầu và xử lý nguyên nhân trước khi tăng tiếp. | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ gợi ý đủ điều kiện | B4: **11.743 đ/việc thành công** với 9 phút làm lại mỗi ca, lên **12.516 đ = 1,04×** mốc thủ công khi dùng số phút làm lại trung bình trong phạm vi [simulated]. | Trong một tuần, **100%** yêu cầu có ít nhất một lần chạy `ok` được xem lại và thời gian xem lại trung bình đạt **5 phút** hoặc hơn. | Giữ mức lưu lượng hiện tại, đo phút xem lại và làm lại thực tế, rồi rút ngắn bước xem lại và đo lại trước khi tăng tiếp. | Trưởng nhóm CSKH |
