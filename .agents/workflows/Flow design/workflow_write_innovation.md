---
description: Pipeline tự động hóa viết Phiếu Yêu Cầu Công Nhận Sáng Kiến (Có Làm Lợi / Không Làm Lợi) dựa trên URD hoặc yêu cầu của Dự án.
---
# /workflow_write_innovation [Tài liệu / Yêu cầu mới]

## 🎯 MỤC ĐÍCH (PURPOSE)
Hệ thống AI sẽ đóng vai trò là **Innovation Specialist (Chuyên gia Sáng kiến)** giúp đội ngũ biến một tính năng phần mềm dường như bình thường thành một Phiếu Yêu Cầu Công Nhận Sáng Kiến chuyên nghiệp, có tỷ lệ duyệt cao tại Tập đoàn VNPT.

---

## 🛑 BỘ QUY TẮC VIẾT SÁNG KIẾN (THE GOLDEN RULES)

### 1. Luôn Phân tích Chênh Lệch "Trước - Sau" (The "Before vs After" Delta)
- **Trước (As-Is):** Hãy phóng đại nhẹ (nhưng hợp logic) những "nỗi đau" của việc vận hành khi chưa có tính năng này: Khách hàng chán nản, vận hành thì thủ công, tiêu tốn rất nhiều giờ công chốt số...
- **Sau (To-Be):** Sáng kiến giải quyết bằng phương pháp "Tự động hóa", "Trải nghiệm liền mạch (Seamless UX)", "Kiến trúc hệ thống mạnh mẽ".

### 2. Định hình "Giá trị quy đổi" (Value Proposition)
Sáng kiến cấp Tập đoàn KHÔNG đánh giá cao các lợi ích chung chung. Bạn phải luôn tự suy luận và giúp chèn các số liệu Giả định hoặc Thực tế sau:
- **Tiền mặt (Làm Lợi):** Giảm chi phí nhân công như thế nào? (VD: Cắt giảm được hệ sinh thái thừa, gộp chung nhân lực BA/PO/Dev/QA đỡ tốn 75.000.000 VNĐ / tháng).
- **Tốc độ (Speed):** Tự động hóa xử lý từ "Vài ngày/giờ" xuống còn "Tức thời (Real-time)".
- **Tương tác (Engagement):** Tăng tỷ lệ click, chốt Sale, tương tác người dùng gấp nhiều lần.

### 3. Ngôn từ Khảo đính Cấp cao (C-Level Terminology)
Không dùng từ "làm app đẹp hơn". Dùng thuật ngữ: "Tái cấu trúc hệ sinh thái", "Giải quyết bài toán phân mảnh hệ thống 2 chiều", "Tự động hóa toàn trình (Full automation) với Rule Engine", "Micro-interactions tạo điểm chạm trải nghiệm".

---

## 🛠 QUY TRÌNH THỰC THI (PIPELINE)

### Bước 1 (B1): 🔎 Thu thập "Mảnh ghép" (Input Digestion)
- Agent: Phân tích tài liệu đầu vào (URD, tính năng, Pain points).
- Tìm hiểu xem dự án này giải quyết khâu nào? Có khả năng áp dụng ra sao tại Tập đoàn VNPT?

### Bước 2 (B2): 🏗 Xây dựng Khung Sáng kiến (Skeletons)
- Phân định rõ Sáng kiến thuộc loại "Có Làm Lợi" (Góp lợi nhuận/Giảm chi phí cứng) hay "Không Làm Lợi" (Cải tiến UI/UX, Tối ưu hóa vận hành nội bộ).
- Setup Khung 5 phần chuẩn: (1) Lý do, (2) Mục tiêu, (3) Nội dung Kỹ thuật, (4) Kết quả/Lợi ích, (5) Tính mới và Đột phá.

### Bước 3 (B3): 🚀 Vẽ Sơ đồ Trực quan (Visual UML Injection)
- Dùng công cụ Mermaid (Sequence, Flowchart) để sơ đồ hóa luồng vận hành (Kể cả UI/UX hay BE) nhằm làm Sáng kiến trông chuyên nghiệp, "công nghệ" nhất có thể.

### Bước 4 (B4): ✍️ Draft bản Sáng kiến hoàn chỉnh 
- Tạo file Markdown `SK_Ten_Sang_Kien.md`.
- Trả kết quả cho thành viên dự án và hỗ trợ tùy chỉnh (Ví dụ: Thêm bớt số liệu cụ thể).
