# Bảng chi phí · Nhiệm vụ A và B

Số tính bằng `src/lab13.py`. Mọi con số tính từ cột `_simulated` ghi nhãn `simulated`. Mỗi câu trả lời không quá ba dòng, có ít nhất một con số.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | --- |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

`python lab13.py` in `Ba phép thử đáp án biết trước: ĐẠT`. Hệ số ở phép thử 3 rút gọn thành `1/p`, nên không phụ thuộc số lần chạy tối đa `k`.

## A2 · Mô hình chi phí từ trace

| Khoản | Số tiền (đ) | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585 | `logix_runs.csv`, mọi lần chạy (1.624) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`, 5.600 lần gọi | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated` (890 phút × 2.000 đ) | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated` (1.132 phút × 2.000 đ) | simulated |
| Tổng chi phí | 4.373.585 | tổng bốn khoản trên | có phần simulated |
| Số việc thành công | 978 | `ket_qua` bằng `thanh_cong` | |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp bao nhiêu lần "hoá đơn chia số yêu cầu"? 4.472 đ so với 274,7 đ, tức **gấp 16,3 lần** [simulated]. Phần chênh là giờ nhân viên, khoản mà hoá đơn token không nhìn thấy.
- Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí, bao nhiêu phần trăm? **Làm lại: 2.264.000 đ = 51,8%** [simulated], tiếp theo là xem lại 1.780.000 đ = 40,7%. Giờ nhân viên chiếm 92,5% tổng chi phí; token và tool chỉ 7,5%.
- Lưu ý khi so với 12.000 đ: 4.472 đ = 0,37× nhưng chỉ chia cho 978 việc trợ lý làm xong, **chưa tính** 222 yêu cầu không thành công mà nhân viên phải làm thay (148 ca `chuyen_nhan_vien`, 74 ca `lam_lai`). So công bằng thì dùng chi phí cả hệ thống: (4.373.585 + 222 × 12.000) ÷ 1.200 = **5.865 đ/yêu cầu = 0,49×** [simulated].

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: | ---: |
| noi_dia | 824 | 95,0% | 1,11 | 2.696 đ [simulated] | 0,22× |
| hang_nang | 158 | 74,1% | 1,47 | 8.221 đ [simulated] | 0,69× |
| quoc_te | 150 | 27,3% | 2,32 | 22.515 đ [simulated] | 1,88× |
| doi_tac | 68 | 54,4% | 1,88 | 10.215 đ [simulated] | 0,85× |

Tỉ lệ `status` bằng `ok` theo từng lần thử (bằng chứng cho câu hỏi "chạy lại có giúp không"):

| Loại | Lần 1 | Lần 2 | Lần 3 |
| --- | ---: | ---: | ---: |
| noi_dia | 91,0% | 75,7% | 38,9% |
| hang_nang | 70,9% | 39,1% | 17,9% |
| doi_tac | 51,5% | 18,2% | 14,8% |
| quoc_te | 30,0% | 11,4% | 2,2% |

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`: 22.515 đ = 1,88×** của 12.000 đ, tỉ lệ thành công chỉ 27,3% [simulated]. Chạy lại tới 3 lần **không giúp**: tỉ lệ đúng tụt 30,0% → 11,4% → 2,2%, lỗi lặp lại trên cùng yêu cầu nên chỉ tốn thêm tiền. `doi_tac` sát ngưỡng (0,85×) và có điều khoản riêng nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

Trong phạm vi `noi_dia` + `hang_nang`: 982 yêu cầu, 900 việc thành công, tổng chi phí 3.072.513 đ → chi phí mỗi việc thành công **chưa** cộng cố định là 3.414 đ [simulated]. Số việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200 = 33.750.

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Ở quy mô đầy đủ thì **không đổi**: 4.599 đ = 0,38× vẫn rẻ hơn nhân viên tự làm. Khối lượng giảm một nửa thì cố định tăng từ 1.185 đ lên **2.370 đ/việc**, đẩy chi phí lên 5.784 đ = **0,48×** [simulated]. Hồ sơ phải ghi rõ con số đã cộng cố định hay chưa và ở khối lượng nào.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | ... | ... |
| Giá token giảm một nửa | 13 đ và 65 đ | ... | ... |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | ... | ... |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | ... | ... |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | ... | ... |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | ... | ... |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | ... | ... |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | ... | ... |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | ... | ... |

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: ...
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. ... · 2. ... · 3. ...

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | ... | ... | ... | ... |
| 2 lần | ... | ... | ... | ... |
| 3 lần | ... | ... | ... | ... |

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? ...

## B4 · Nếu phải xem lại tất cả

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: ...
- Kết quả này nói gì về thứ pilot cần học được? ...
