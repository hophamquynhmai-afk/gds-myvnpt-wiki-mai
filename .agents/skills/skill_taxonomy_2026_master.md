# 🧠 Skill: Taxonomy 2026 - Chuẩn hóa Sự kiện GDS

## 📌 Tổng quan
Skill này định nghĩa các quy tắc vàng để phân loại và đặt tên sự kiện (event tracking) cho hệ sinh thái MyVNPT. Mọi event được bóc tách từ URD phải tuân thủ nghiêm ngặt chuẩn này.

## 🧬 Cấu trúc định danh (Naming Convention)
**Công thức:** `[Action]_[Object]_[Context]` (Dạng `snake_case`)
- **Ví dụ:** `click_button_login`, `view_screen_home`, `swipe_banner_promo`.

## 📁 Phân loại Category (Event Category)

### 1. Engagement (Tương tác)
- **Mô tả:** Người dùng khám phá, xem nội dung, hoặc thực hiện các hành động không trực tiếp ra tiền nhưng tăng tính gắn kết.
- **Dấu hiệu:** `view`, `click` (vào banner, tin tức), `share`, `like`.
- **Ví dụ:** `view_news_promotion`, `click_banner_hot_deal`.

### 2. Transaction (Giao dịch)
- **Mô tả:** Các bước trong luồng mua sắm, thanh toán, đăng ký gói cước. ĐÂY LÀ CHỈ SỐ QUAN TRỌNG NHẤT.
- **Dấu hiệu:** `confirm`, `order`, `payment`, `pincode`, `otp_success`.
- **Ví dụ:** `click_confirm_payment`, `transaction_success_esim`.

### 3. Utility (Tiện ích)
- **Mô tả:** Các tính năng hỗ trợ, quản lý tài khoản, cài đặt.
- **Dấu hiệu:** `search`, `login`, `change_setting`, `download`, `upload`.
- **Ví dụ:** `search_utility_near_me`, `login_biometric_success`.

### 4. Lifecycle (Vòng đời)
- **Mô tả:** Cài đặt, gỡ app, cập nhật phiên bản, đăng ký tài khoản mới.
- **Ví dụ:** `app_update_start`, `registration_finish`.

## 🛠 Quy tắc bóc tách từ URD
1. **Dựa vào UI/UX:** Mọi nút bấm (CTA - Call to Action) phải có 1 event `click`.
2. **Dựa vào Logic:** Mọi kết quả API (Thành công/Thất bại) phải có event ghi lại trạng thái.
3. **Màn hình:** Mọi màn hình chính trong luồng phải có event `view_screen`.

---
> *Skill này là "linh hồn" của Event Tracking Analyst, đảm bảo dữ liệu đổ về Google Sheet luôn sạch và nhất quán.*
