# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Ngô Ngọc Hải · Người gắn nhãn 2: Trần Hải Long (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- **Không có ca không trùng:** hai bộ nhãn độc lập khớp cả 20/20 ca, trên mốc 80% nên nhóm không phải viết lại định nghĩa.
- Quy tắc hai người dùng cho cặp dễ lẫn nhất, **Hệ thống** và **Ngầm**: lỗi đã **lộ ra** cho người dùng hoặc nhân viên (ca 8 trích dẫn điều khoản bịa nhìn thấy được, ca 15 nhân viên bắt được) thì là **Hệ thống**, dù số tiền hoàn vẫn đúng; **Ngầm** chỉ dùng khi không ai nhận ra cho tới lúc kiểm tra mẫu (ca 12 chi phí gấp 3 suốt 3 tuần, ca 17 sai bảng giá trong bộ nhớ đệm). Tiêu chí là "có ai thấy được hay không", không phải "số tiền có đúng hay không".

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi tên tập thể.

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo khi quá **2%** số yêu cầu/**ngày** | Nhận diện mã sàn TMĐT và tra sang mã vận đơn; không tra được thì hướng dẫn kèm ảnh | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát **mỗi giờ**: tin nhắn "đã hoàn" không có `refund_ledger_write` ok cùng `trace_id`; ngưỡng **> 0 ca** | Chỉ báo "đã hoàn" khi sổ cái trả ok; lỗi 503 sau 3 lần thì báo "đang xử lý" và chuyển nhân viên | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Event `ticket_reopened` trên ca hoàn tiền đúng số tiền; ngưỡng **> 3% ca/tuần**, rà soát **hằng tuần** | Mẫu tin nhắn luôn ghi cách tính: `30.000 đ × 50% = 15.000 đ` | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Event `handoff_to_staff` với `reason = thieu_du_lieu` theo loại yêu cầu; ngưỡng **> 5%/tuần**, theo dõi **hằng tuần** | Giữ cách chuyển kèm tóm tắt; đưa `quoc_te` ra khỏi pilot | PM trợ lý hoàn phí |
| 17 | Ngầm | Event `audit_sample_checked`: kiểm tra mẫu **100 đơn/tuần** so với bảng giá hiện hành; ngưỡng **≥ 1%** đơn lệch | Xoá bộ nhớ đệm khi có bảng giá mới, ghi phiên bản bảng giá vào trace | Kế toán trưởng |
