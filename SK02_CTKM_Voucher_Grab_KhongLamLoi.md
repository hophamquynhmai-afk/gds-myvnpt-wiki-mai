# PHIẾU YÊU CẦU CÔNG NHẬN SÁNG KIẾN
**Tên sáng kiến:** Tự động hóa và Số hóa luồng tặng thưởng Voucher (Cross-selling) tích hợp Real-time trên MyVNPT
**Loại Sáng kiến:** Không làm lợi trực tiếp (Tối ưu Trải nghiệm và Nâng cao Năng lực Cạnh tranh)

---

## I. LÝ DO VÀ SỰ CẦN THIẾT (BACKGROUND & RATIONALE)
### 1. Hiện trạng (As-Is)
- Các chương trình khuyến mại (CTKM), tặng Voucher của VNPT (đặc biệt là hợp tác với các đối tác lớn như Grab) trước đây thường được triển khai dưới dạng thủ công hoặc thông báo qua SMS sau một khoảng thời gian trễ.
- Khách hàng sau khi hoàn tất thanh toán mua SIM, hoặc đăng ký mua gói cước thường kết thúc ngay hành trình mua sắm. Trải nghiệm thiếu các điểm chạm "WOW" tức thời (Micro-interactions) để giữ chân khách hàng.
- Thu thập danh sách khách hàng đủ điều kiện và gửi mã Voucher thường mất thời gian, đòi hỏi hậu kiểm và dễ gặp sai sót về đối tượng nhận.

### 2. Nhu cầu cải tiến (To-Be)
- **Nhu cầu số hóa:** Xây dựng một luồng Marketing In-app có khả năng bắt sự kiện (event-triggered) thanh toán thành công theo thời gian thực (Real-time) để kích hoạt phần thưởng lập tức.
- **Khoảng trống thị trường:** Việc tặng mã Voucher ngay tại màn hình thanh toán thành công (Success Screen) kết hợp tự động gửi SMS sẽ gia tăng đáng kể độ gắn kết của người dùng (User Engagement) và khuyến khích họ thực hiện thêm giao dịch (Cross-selling).

## II. MỤC TIÊU SÁNG KIẾN (OBJECTIVES)
- **Liền mạch trải nghiệm (Seamless UX):** Tích hợp phân hệ nhận quà mượt mà ngay sau luồng thanh toán (Mua SIM, Mua Gói), không làm gián đoạn hay bắt người dùng phải thoát khỏi ngữ cảnh hiện tại.
- **Tự động hóa toàn trình (Full Automation):** Số hóa 100% nghiệp vụ phát quà, cấu hình luật (Rule Engine) áp dụng cho đơn ≥ 10.000đ, hạn chế tối đa sự can thiệp của con người.
- **Cá nhân hóa đa ngôn ngữ:** Chuẩn hóa giao diện song ngữ (Việt - Anh) và gửi thông báo đúng tới SĐT đang tương tác (SĐT Login hoặc SĐT liên hệ).
- **Quản lý linh hoạt:** Quản lý tập trung kho Voucher, có cơ chế báo lỗi tinh tế (Error Handling) khi hết kho hoặc nghẽn mạng.

## III. NỘI DUNG VÀ GIẢI PHÁP KỸ THUẬT (TECHNICAL INNOVATION)
Dựa trên phân tích kịch bản nghiệp vụ (URD), sáng kiến này đã thiết kế luồng xử lý mới với các điểm nổi bật sau:

**Sơ đồ Luồng Nghiệp vụ Cải tiến (User Flow - Sequence Diagram):**

![Sơ đồ Tuần tự](C:\Users\caida\gds-myvnpt-wiki\Voucher_Grab_Sequence.png)

**Mô tả Quy trình (Process flow detail):**

*   **Giai đoạn 1: Xác thực giao dịch & hiển thị lời mời nhận quà**
    1.  Khách hàng thực hiện thanh toán thành công một giao dịch trên ứng dụng MyVNPT (mua SIM hoặc đăng ký gói cước).
    2.  Ngay sau khi giao dịch hoàn tất, ứng dụng MyVNPT gọi API gửi thông tin giao dịch đến Hệ thống quản lý CTKM/Voucher để kiểm tra điều kiện chương trình.
    3.  Hệ thống tự động đối chiếu các điều kiện khuyến mại (ví dụ: giá trị đơn hàng, loại sản phẩm, thời gian chương trình).
    4.  Nếu giao dịch đủ điều kiện, hệ thống trả về status hợp lệ cho ứng dụng.
    5.  Ứng dụng MyVNPT kích hoạt Banner/Box “Nhận voucher” hiển thị trực tiếp trên màn hình giao dịch thành công (Success Screen) nhằm khuyến khích khách hàng nhận ưu đãi.

*   **Giai đoạn 2: Cấp mã & trả thưởng đa kênh**
    6.  Khách hàng bấm nút “Nhận voucher” trên giao diện ứng dụng.
    7.  Ứng dụng MyVNPT gửi request cấp mã voucher tới hệ thống.
    8.  Hệ thống xử lý và thực hiện đồng thời hai luồng nghiệp vụ:
        *   **Cấp voucher nội bộ**: Lấy một mã voucher từ kho voucher, gán vào tài khoản khách hàng và lưu vào cơ sở dữ liệu.
        *   **Gửi thông tin qua SMS**: Gửi yêu cầu tới Cổng SMS để gửi tin nhắn chứa mã voucher tới số điện thoại của khách hàng.
    9.  Sau khi xử lý hoàn tất, Hệ cập nhật trạng thái giao diện thành “Đã nhận” nhằm tránh việc khách hàng bấm nhận lặp lại trên CSDL.

**1. Tích hợp Native Banner tại Success Screen**
- Thiết lập hệ thống lắng nghe trạng thái thanh toán. Khi người dùng mua SIM/eSIM hoặc Gói cước thành công, hệ thống trực tiếp gọi API kiểm tra điều kiện CTKM Grab.
- Hiển thị Banner theo quy tắc Stateful:
  - **Chưa nhận:** Nút `[Nhận ngay]` nổi bật + Banner quảng cáo.
  - **Đã nhận:** Giao diện vô hiệu hóa nút nhận, thông báo "Bạn đã đăng ký nhận voucher thành công!".

**2. Tối ưu UX/UI & Error Handling**
- **Micro-interactions:** Sử dụng Popup (Dialog) ngay khi click nhận quà thành công với thông điệp rõ ràng, cá nhân hoá SĐT đích.
- **Zero-Dead-End (Không có ngõ cụt):** Khi kho Voucher trống, hệ thống trả về Toast thông báo thân thiện "Rất tiếc, voucher đã được phát hết", tránh gây bức xúc cho khách hàng.

**3. Kiến trúc Backend tự động phân bổ quà tặng**
- **Xử lý số điện thoại động:** Tự động bắt SĐT của phiên đăng nhập. Nếu là khách (Guest), tự động lấy SĐT liên hệ trên đơn hàng để làm thông số nhận SMS.
- **Tích hợp cổng SMS Vshop:** Gọi API Brandname tự động, truyền trực tiếp các biến thời gian thực: `[Mã voucher]`, `[Mã đơn hàng]`, `[Hạn dùng]`.

## IV. BẢNG KẾT QUẢ SO SÁNH (BEFORE & AFTER)

| Tiêu chí | Trước khi áp dụng sáng kiến (Thủ công) | Sau khi áp dụng sáng kiến (Tự động hóa) |
| :--- | :--- | :--- |
| **Tốc độ nhận quà** | Trễ từ vài giờ đến vài ngày (Chờ chốt danh sách) | **Real-time (Ngay lập tức)** sau 1 giây click nhận |
| **Trải nghiệm UX** | Rời rạc, khách hàng hay quên chương trình ưu đãi | **Liền mạch,** giữ chân khách tại App, tăng tỷ lệ Open-rate của SMS |
| **Quy trình Vận hành** | Thủ công (Xuất dữ liệu, gửi SMS tay hoặc định kỳ) | **Tự động 100%**, có hệ thống báo cáo (Tracking CTKM, Mã đơn) đầy đủ |
| **Xử lý trích xuất** | Dễ sai sót gửi nhầm số | Engine tự động xác minh: **SĐT Login** hoặc **SĐT Liên hệ mua hàng** |

## V. TỰ ĐÁNH GIÁ TÍNH MỚI VÀ SÁNG TẠO
**1. Tính mới (Novelty)**
Lần đầu tiên luồng phát Voucher đối tác bên ngoài (Grab) được nhúng (embed) trực tiếp vào sâu bên trong luồng Thanh toán (Payment Gateway) của MyVNPT dưới dạng sự kiện thời gian thực thay vì các chiến dịch Push Notification đại trà truyền thống.

**2. Tính sáng tạo (Creativity & Breakthrough)**
- **Xử lý linh hoạt đối tượng mục tiêu:** Sáng tạo trong việc "gom" luồng xử lý cho cả tệp Khách hàng đã Đăng nhập và Khách hàng Vãng lai (Chưa đăng nhập) vào chung 1 module code, tiết kiệm nguồn lực bảo trì.
- **Chuẩn hóa Giao thức Báo cáo:** Hệ thống không chỉ cấp code, mà còn tự động sinh File Reporting chứa đầy đủ Tracking (SĐT, Mã đơn, ID CTKM, Tên Gói, Tổng giá trị), giúp đối soát (Reconciliation) với đối tác Grab một cách hoàn toàn minh bạch, chuẩn xác.

---
*Bản thảo sáng kiến được tự động tạo bởi GDS Innovation Agent.*
