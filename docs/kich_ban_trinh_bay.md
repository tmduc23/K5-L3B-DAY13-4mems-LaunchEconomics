# Kịch bản trình bày cho các nhóm — giải thích vấn đề dễ hiểu nhất

Bản này để **đọc thành tiếng**, không phải để nộp. Văn nói, câu ngắn. Toàn bài **6 phút**; nếu bị cắt còn 3 phút thì bỏ các đoạn có dấu ✂.

Ba quy tắc khi nói: **một ý một hình ảnh** · **mỗi ý một con số duy nhất** · **không dùng biệt ngữ mà chưa giải thích**.

---

## Mở đầu · 30 giây

> "Nhóm mình được giao một câu hỏi nghe rất đơn giản: **con trợ lý này có đáng chạy không?**
>
> Chỗ khó không phải là tính toán. Chỗ khó là **đừng tính sai chỗ**. Và mình đã tính sai ở lần đầu, nên mình muốn kể lại cả chỗ sai đó."

**Tại sao mở như vậy:** thừa nhận mình từng sai làm người nghe bỏ phòng vệ. Họ sẽ nghe để học, không nghe để bắt lỗi.

---

## Ý 1 · Hoá đơn token không phải chi phí · 60 giây

> "Lần đầu mình làm thế này: lấy hoá đơn token cộng tiền gọi tool, chia cho số yêu cầu. Ra **275 đồng** một yêu cầu. Rẻ kinh khủng. Mình tưởng xong rồi.
>
> Nhưng hãy nghĩ thế này. Bạn mua một cái máy pha cà phê tự động. Tiền điện của nó mỗi tháng là 50 nghìn. Vậy một ly cà phê của bạn tốn 50 nghìn chia số ly, đúng không?
>
> Không. Vì vẫn có người phải đứng cạnh **kiểm lại** từng ly, và **làm lại** những ly máy pha sai. Tiền lương của người đó mới là khoản lớn.
>
> Với trợ lý hoàn phí, con số thật là **4.472 đồng** một việc — gấp **16 lần** cái hoá đơn token. Và trong 4.472 đồng đó, **92%** là giờ của nhân viên: thời gian họ xem lại gợi ý, và thời gian họ làm lại khi gợi ý sai.
>
> Nên bài học thứ nhất: **cái hoá đơn bạn nhận được không phải chi phí của bạn.** Chi phí của bạn gồm cả thời gian người thật phải bỏ ra vì con agent."

---

## Ý 2 · Chia cho cái gì mới là chỗ dễ sai nhất · 60 giây

> "Giờ đến chỗ mình sai thật.
>
> Tưởng tượng một người thợ nhận 10 cái áo để sửa. Anh ta sửa xong 8 cái, 2 cái làm hỏng phải trả lại khách.
>
> Vải và chỉ thì anh ta dùng cho cả **10** cái — kể cả 2 cái hỏng cũng tốn vật liệu rồi. Nhưng kết quả dùng được chỉ có **8** cái.
>
> Vậy giá thành một cái áo tốt là: vật liệu của 10 cái, chia cho 8 cái. **Không phải chia cho 10.**
>
> Dữ liệu của mình y như vậy. 1.200 yêu cầu, agent chạy 1.624 lần — kể cả những lần chạy lỗi vẫn tốn tiền. Nhưng chỉ **978** yêu cầu thực sự xong.
>
> Chia cho 1.200 thì ra 3.645 đồng. Chia cho 978 thì ra 4.472 đồng. Chênh nhau 23%, chỉ vì chọn mẫu số khác.
>
> Bài học thứ hai: **tiền tính hết, nhưng chỉ đếm cái chạy được.** Chia cho tổng số yêu cầu là tự che mất phần hỏng của mình."

✂ Nếu phải cắt, bỏ đoạn 1.624 lần chạy, giữ ví dụ người thợ và hai con số 3.645 / 4.472.

---

## Ý 3 · Chạy lại không miễn phí, và không phải lúc nào cũng cứu được · 50 giây

> "Agent chạy sai thì cho chạy lại — nghe hợp lý. Nhưng chạy lại có hai cái giá.
>
> Giá thứ nhất là tiền: mỗi lần chạy lại vẫn đốt token.
>
> Giá thứ hai lạ hơn. Bạn gọi tổng đài, bị trả lời sai. Bạn gọi lại lần hai. Nếu nguyên nhân là **nhân viên đó không biết**, thì gọi lại 10 lần vẫn sai như thế — vì vẫn là người đó, vẫn là câu hỏi đó.
>
> Dữ liệu của mình đúng y vậy. Với loại yêu cầu quốc tế, lần chạy đầu đúng **30%**. Lần thứ hai chỉ còn **11%**. Lần thứ ba: **2%**.
>
> Lỗi không phải ngẫu nhiên. Lỗi là **lặp lại trên cùng một yêu cầu**. Nên cho chạy tới 3 lần chỉ tốn thêm tiền mà không cứu được việc nào.
>
> Bài học thứ ba: **trước khi tăng số lần thử, hãy xem tỉ lệ đúng theo từng lần thử.** Nếu nó tụt dốc như vậy, chạy lại là vô ích."

---

## Ý 4 · Không phải việc nào cũng nên giao cho nó · 40 giây

> "Nhóm mình tách chi phí theo từng loại yêu cầu, và bức tranh đổi hẳn.
>
> Loại nội địa thường: **2.696 đồng**, bằng 0,22 lần so với để nhân viên tự làm. Rất đáng.
>
> Loại quốc tế: **22.515 đồng**, bằng **1,88 lần**. Tức là giao cho agent **đắt gần gấp đôi** so với để nhân viên làm thẳng.
>
> Cùng một con agent, cùng một tuần. Chỉ khác loại việc.
>
> Bài học thứ tư: câu hỏi đúng không phải *'agent này có tốt không'*, mà là **'agent này đáng dùng cho việc nào'**. Nên pilot của mình chỉ chạy hai loại rẻ nhất, và nói rõ bằng số vì sao loại hai loại kia."

---

## Ý 5 · Vì sao phải có nhóm đối chứng · 50 giây

> "Đợt chạy thử cho chỉ số **82,83%**. Nghe rất đẹp. Mục tiêu ban đầu là 70%.
>
> Nhưng mình **không** được nói 'agent đã nâng chỉ số từ 70 lên 83'. Vì sao?
>
> Bạn bị cảm. Bạn uống một viên thuốc. Ba ngày sau khỏi. Thuốc chữa khỏi bạn, hay bạn tự khỏi?
>
> Bạn không biết. Để biết, phải có một người khác cũng bị cảm, cũng ba ngày, mà **không** uống thuốc.
>
> Đợt chạy thử của mình không có 'người không uống thuốc'. Không có ai làm cùng tuần đó mà không dùng agent. Nên con số 82,83% chỉ nói *chuyện gì đã xảy ra*, không nói *vì sao nó xảy ra*.
>
> Bài học thứ năm: **không có đối chứng thì chỉ được mô tả, không được kết luận.** Mình chỉ viết 'chỉ số trong đợt chạy thử là 82,83%'. Đó cũng chính là lý do phải làm pilot."

---

## Ý 6 · Hỏi 20 người 300 câu không bằng hỏi 300 người 20 câu · 60 giây

> "Đây là phần mình mất nhiều thời gian nhất, và cũng là phần thú vị nhất.
>
> Giả sử bạn muốn biết dân thành phố thích món gì. Bạn có hai cách, cùng 6.000 câu trả lời:
>
> Cách A: hỏi **20 người**, mỗi người 300 câu.
> Cách B: hỏi **300 người**, mỗi người 20 câu.
>
> Cách nào đáng tin hơn? Cách B. Vì 300 câu trả lời của cùng một người thì **na ná nhau** — người thích ăn cay sẽ trả lời giống nhau 300 lần. Hỏi thêm người đó gần như không biết thêm gì mới.
>
> Thống kê gọi hiện tượng đó là **tương quan trong cụm**. Và nó dẫn tới một điều rất phũ: khi bạn chia nhóm theo người, **số người quyết định, không phải số yêu cầu.**
>
> Công ty này có 40 nhân viên. Chia đôi thành 20 và 20. Dù mỗi người xử lý bao nhiêu yêu cầu đi nữa, lượng thông tin hữu ích cũng **không vượt quá 1.000**. Mà để thấy được mức cải thiện 5 điểm, mình cần **1.251**.
>
> Tức là: **không có cách chia nào đủ mẫu**. Mình không thể làm phép tính này ra kết quả đẹp hơn.
>
> Nên mình làm điều duy nhất trung thực được: hạ mục tiêu xuống **phát hiện mức chênh 6 điểm** thay vì 5, và ghi thẳng vào hồ sơ rằng nếu tác động thật chỉ là 5 điểm thì **36% khả năng mình sẽ không phát hiện ra**.
>
> Bài học thứ sáu: **tính cỡ mẫu TRƯỚC khi chọn cách chia nhóm.** Nhiều người chọn chia theo chi nhánh vì dễ triển khai, rồi mới phát hiện chỉ có 6 cụm — quá ít để kết luận bất cứ điều gì."

---

## Ý 7 · Luật dừng phải viết trước, và ngưỡng phải so với nền · 40 giây

> "Ý cuối, ngắn thôi, nhưng là ý mình thích nhất.
>
> Mình viết sẵn ba điều kiện dừng pilot **trước khi** bắt đầu. Vì nếu đợi đến lúc số liệu xấu mới ngồi bàn 'thế này có đáng dừng không' thì sẽ luôn có người tìm ra lý do để chạy tiếp.
>
> Và đây là cái bẫy mình gần như mắc. Mình định đặt ngưỡng an toàn là: *tỉ lệ khách mở lại khiếu nại vượt 3% thì dừng.*
>
> Nghe rất chặt chẽ. Nhưng rồi mình đi đo tỉ lệ **hiện tại**: đã là **3,97%** rồi. Tức là pilot sẽ bị dừng ngay tuần đầu, dù agent không làm gì sai cả.
>
> Giống như đặt báo cháy ở mức 25 độ trong một căn phòng đang 28 độ.
>
> Nên ngưỡng của mình thành: **cao hơn nhóm đối chứng 2 điểm, kèm trần tuyệt đối 6%**.
>
> Bài học cuối: **đo nền trước khi đặt ngưỡng.** Một ngưỡng nghe nghiêm khắc mà thấp hơn mức nền thì không nghiêm khắc, nó chỉ vô dụng."

---

## Chốt · 25 giây

> "Tóm lại sáu chữ: **tính hết, đếm đúng, so công bằng.**
>
> Tính hết mọi lần chạy kể cả lần lỗi. Chỉ đếm việc thật sự xong. So với chi phí của con người một cách công bằng, kể cả phần việc agent không làm được.
>
> Làm được ba điều đó thì con số 275 đồng thành 5.865 đồng. Vẫn rẻ hơn 12.000 đồng của nhân viên — nhưng là **rẻ một nửa**, không phải rẻ 40 lần. Và sự khác biệt đó đủ để đổi hẳn quyết định đầu tư.
>
> Cảm ơn mọi người."

---

## Nếu chỉ còn 30 giây

> "Một ý duy nhất: **hoá đơn token không phải chi phí.** Chi phí thật của một việc làm xong là 4.472 đồng, gấp 16 lần hoá đơn, vì 92% nằm ở giờ nhân viên xem lại và làm lại. Ai chỉ nhìn hoá đơn token sẽ tưởng agent rẻ gấp 40 lần con người, trong khi thực tế chỉ rẻ khoảng một nửa."

---

## Giải thích biệt ngữ — dùng cột phải khi nói

| Đừng nói | Hãy nói |
| --- | --- |
Chi phí mỗi việc thành công | Chi phí cho một việc **làm xong được** |
Cỡ mẫu hiệu dụng | Lượng thông tin **hữu ích** thật sự có |
Hệ số thiết kế, ICC | Các câu trả lời của **cùng một người thì na ná nhau** |
Power 0,64 | **36% khả năng không phát hiện ra** dù có tác động thật |
MDE 6 điểm | Mức cải thiện **nhỏ nhất mà pilot còn thấy được** |
Spillover / tràn tác động | Người dùng agent **kể lại** cho người không dùng |
Nhóm đối chứng | Nhóm **không dùng** agent, làm cùng lúc để so |
Nhãn `simulated` | Số này do **đề bài tạo ra**, không phải đo thật |

---

## Bốn hình ảnh — nếu quên hết thì nhớ bốn cái này

| Ý | Hình ảnh |
| --- | --- |
Hoá đơn ≠ chi phí | Máy pha cà phê: tiền điện rẻ, nhưng vẫn phải trả lương người đứng kiểm từng ly |
Mẫu số | Người thợ sửa 10 áo, xong 8: vật liệu tính 10, giá thành chia 8 |
Chạy lại | Gọi lại tổng đài gặp đúng người không biết câu trả lời |
Không có đối chứng | Uống thuốc rồi khỏi cảm — không biết do thuốc hay tự khỏi |
Cụm | Hỏi 20 người 300 câu không bằng hỏi 300 người 20 câu |
Ngưỡng không có nền | Đặt báo cháy ở 25 độ trong phòng đang 28 độ |

---

## Nhắc trước khi nói

- **Mỗi ý một con số.** Đừng đọc hai con số trong một câu; người nghe chỉ giữ được một.
- **Dừng sau mỗi “bài học thứ…”.** Một nhịp lặng hai giây làm người nghe ghi lại được.
- **Viết lên bảng đúng ba thứ** nếu có bảng: `275 → 4.472 → 5.865`. Ba mũi tên đó là cả bài.
- **Không dùng từ “production”.** Gate 2a chỉ duyệt kế hoạch pilot.
- **Mọi số dẫn từ hai cột `_simulated`** phải nói kèm "số này là giả lập" ít nhất một lần trong bài.
