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
| Token | 245.585 | `logix_runs.csv`: 5.771.712 token vào ÷ 1.000 × 26 + 734.774 token ra ÷ 1.000 × 130, mọi 1.624 lần chạy (kể cả `loi`) | đo từ trace |
| Tool | 84.000 | `logix_runs.csv`: 5.600 lần gọi × 15 | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804 | `logix_runs.csv`: 424 lần chạy có attempt lớn hơn 1 | đo từ trace |
| Xem lại | 1.780.000 | `phut_xem_lai_simulated`: 890 phút × 2.000 | simulated |
| Làm lại | 2.264.000 | `phut_lam_lai_simulated`: 1.132 phút × 2.000 | simulated |
| Tổng chi phí | 4.373.585 | Token + Tool + Xem lại + Làm lại | có phần simulated |
| Số việc thành công | 978 | `ket_qua` bằng `thanh_cong` | đo từ dữ liệu |
| Chi phí mỗi việc thành công | 4.472 | 4.373.585 ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 | (245.585 + 84.000) ÷ 1.200 | đo từ trace |

Kiểm số (người kiểm số): tính tay độc lập cả 9 dòng từ tổng cột CSV, khớp output `python lab13.py`, lệch 0%.

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

- Loại nào không đáng để trợ lý xử lý? Với loại đó, cho chạy lại tới 3 lần có giúp không? **`quoc_te`: 22.515 đ = 1,88×**, thành công 27,3% [simulated]. Chạy lại 3 lần **không giúp** — tỉ lệ đúng tụt 30,0% → 11,4% → 2,2% vì lỗi lặp lại trên cùng yêu cầu. `doi_tac` sát ngưỡng 0,85× nên cũng để ngoài phạm vi pilot.

## A4 · Chi phí cố định (phạm vi noi_dia + hang_nang)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định | So với 12.000 đ |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ [simulated] | 0,38× |
| Một nửa khối lượng | 16.875 | 2.370 đ | 5.784 đ [simulated] | 0,48× |

Trong phạm vi `noi_dia` + `hang_nang`: 982 yêu cầu, 900 việc thành công, tổng chi phí 3.072.513 đ → chi phí mỗi việc thành công **chưa** cộng cố định là 3.414 đ [simulated]. Số việc thành công mỗi tháng = 45.000 × 900 ÷ 1.200 = 33.750.

Ba con số của phạm vi, **đừng lẫn vào nhau** khi ghi mục 3 của hồ sơ: 3.414 đ = 0,28× (chưa cố định) · 4.599 đ = 0,38× (cộng cố định, chỉ chia cho 900 việc trợ lý làm xong) · **5.217 đ = 0,43×** (cộng cố định **và** 82 yêu cầu không thành công mà nhân viên làm thay — 34 ca `chuyen_nhan_vien`, 48 ca `lam_lai`): (3.072.513 + 82 × 12.000 + 1.185 × 900) ÷ 982 [simulated]. Con số công bằng nhất để so với 12.000 đ là 0,43×.

- Chi phí cố định có đổi kết luận không? Ở khối lượng nào? Ở quy mô đầy đủ thì **không đổi**: 4.599 đ = 0,38×, và kể cả tính đủ phần nhân viên làm thay vẫn là 0,43× — rẻ hơn 12.000 đ. Khối lượng giảm một nửa thì cố định tăng từ 1.185 đ lên **2.370 đ/việc**, đẩy chi phí lên 5.784 đ = **0,48×** [simulated]. Hồ sơ phải ghi rõ con số đã cộng cố định hay chưa và ở khối lượng nào.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công | Thay đổi (%) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ và 260 đ cho 1.000 token; giá tool giữ nguyên | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ và 65 đ | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ mỗi phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lần chạy có attempt > 2; yêu cầu có so_lan_chay > 2 coi là chuyen_nhan_vien | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Như trên với giới hạn 1 | 4.111 đ | −8,1% |

Gốc (A2): 4.472 đ. Mọi dòng là số [simulated] vì chi phí mỗi việc thành công có phần tính từ hai cột `_simulated`.
Kiểm đối xứng (người kiểm số): token +5,6% ↔ −2,8% · xem lại +40,7% ↔ −20,3% · làm lại +51,8% ↔ −25,9%; mỗi kịch bản "giảm một nửa" giảm đúng nửa mức tăng của "gấp đôi" (sai lệch ≤ 0,05 điểm do làm tròn) → code đúng.

## B2 · Đổi một cặp và xếp hạng

- Giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi: **6.543 đ (+46,3%)** [simulated], đúng bằng tổng hai tác động riêng (+5,6% + 40,7% = +46,3%) vì mô hình cộng tuyến tính các khoản chi phí.
- Xếp hạng ba yếu tố ảnh hưởng mạnh nhất: 1. **số ca làm lại** (±51,8%) · 2. **tỉ lệ xem lại** (±40,7%) · 3. **lương nhân viên** (+23,1% khi tăng 25%). Giá token chỉ ±5,6%, nên pilot phải theo dõi tỉ lệ làm lại và tỉ lệ xem lại, không phải hoá đơn token.

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý | Số yêu cầu không thành công | Chi phí cả hệ thống | Chi phí mỗi việc thành công |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | **4.111 đ** (thấp nhất) |
| 2 lần | 4.093.220 đ | 234 | **6.901.220 đ** (rẻ nhất) | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

Mọi số trong bảng là [simulated]. Chi phí cả hệ thống = tổng chi phí trợ lý + 12.000 đ × số yêu cầu không thành công, vì nhân viên phải làm thay những ca đó.

- Giới hạn nào rẻ nhất cho công ty? Có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? **Giới hạn 2 lần rẻ nhất cho công ty: 6.901.220 đ** [simulated]. **Không trùng**: chi phí mỗi việc thành công thấp nhất là ở giới hạn 1 lần (4.111 đ). Tối ưu riêng chi phí mỗi việc thành công sẽ đẩy thêm 85 việc (319 − 234) sang nhân viên và làm cả hệ thống đắt thêm 548.561 đ.

## B4 · Nếu phải xem lại tất cả

Phạm vi `noi_dia` + `hang_nang`: 982 yêu cầu, **948** yêu cầu có ít nhất một lần chạy `ok` (mỗi yêu cầu xem lại 5 phút), **48** ca `lam_lai`, token + tool của mọi lần chạy trong phạm vi là 224.513 đ, 900 việc thành công.

| Số phút làm lại mỗi ca | Tổng chi phí | Chi phí mỗi việc thành công | So với 12.000 đ | Mức hoà vốn của một lần xem lại |
| --- | ---: | ---: | ---: | ---: |
| 9 phút (đề cho) | 10.568.513 đ | 11.743 đ [simulated] | **0,98×** | ≤ 5,1 phút |
| 15,3 phút (trung bình thực của toàn bộ ca `lam_lai`) | 11.173.054 đ | 12.415 đ [simulated] | **1,03×** | ≤ 4,8 phút |
| 16,2 phút (trung bình thực trong phạm vi) | 11.264.513 đ | 12.516 đ [simulated] | 1,04× | ≤ 4,8 phút |

- Chi phí mỗi việc thành công khi xem lại 100% (`noi_dia` + `hang_nang`), so với 12.000 đ: **11.743 đ = 0,98×** với 9 phút làm lại mỗi ca; dùng số phút làm lại thực trong dữ liệu (15,3 phút) thì lên **12.415 đ = 1,03×** [simulated], tức **đắt hơn** nhân viên tự làm.
- Kết quả này nói gì về thứ pilot cần học được? Xem lại 100% thì trợ lý gần như không tiết kiệm được gì, vì tiền xem lại chiếm khoảng 90% chi phí kịch bản này. Pilot phải học hai điều: **tỉ lệ xem lại giảm an toàn được xuống mức nào**, và **một lần xem lại có ngắn hơn 5,1 phút được không** (ngưỡng hoà vốn).
