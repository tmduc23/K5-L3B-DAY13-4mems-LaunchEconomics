# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhóm can thiệp được mở bằng trợ lý | Số yêu cầu có `staff_id` thuộc nhóm dùng trợ lý / tổng yêu cầu của nhóm đó | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần (bắt lỗi ngầm như ca 5, 17) | Số đơn lệch tiền trong mẫu kiểm tra / số đơn kiểm tra | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Ít nhất sáu event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | request_id, loai, so_tien, arm, trace_id | Khi khách gửi |
| `agent_run_completed` | Agent | attempt, tokens_in/out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | giu/sua/bo, phut_xem_lai, trace_id | Khi bấm gửi/sửa/bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính (đóng 24h & không mở lại) → tính từ `refund_request_created` + `ticket_closed` + `ticket_reopened`.
- Tỉ lệ bỏ qua gợi ý → tính từ `agent_suggestion_shown` + `staff_review_decision`.
- Tỉ lệ mở lại 7 ngày → tính từ `ticket_reopened`.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1 trên toàn mẫu: **+51,8%**, lên **6.787 đ/việc thành công** [simulated]. | Tỉ lệ `lam_lai` trên các yêu cầu trong phạm vi đạt **9,8%** trong một tuần, khoảng gấp đôi mốc 48/982 ca trong đợt chạy thử. | Tạm hoãn tăng lưu lượng, rà trace ca làm lại theo loại yêu cầu và xử lý nguyên nhân trước khi tăng tiếp. | PM trợ lý hoàn phí |
| Phải xem lại toàn bộ gợi ý đủ điều kiện | B4: **11.743 đ/việc thành công** với 9 phút làm lại mỗi ca, lên **12.516 đ = 1,04×** mốc thủ công khi dùng số phút làm lại trung bình trong phạm vi [simulated]. | Trong một tuần, **100%** yêu cầu có ít nhất một lần chạy `ok` được xem lại và thời gian xem lại trung bình đạt **5 phút** hoặc hơn. | Giữ mức lưu lượng hiện tại, đo phút xem lại và làm lại thực tế, rồi rút ngắn bước xem lại và đo lại trước khi tăng tiếp. | Trưởng nhóm CSKH |
