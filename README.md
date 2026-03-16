# 🚀 GDS Event Tracking Specialist - AI Agent

Bộ công cụ AI chuyên biệt để bóc tách Event Tracking từ URD (User Requirement Document) và đổ dữ liệu chuẩn Taxonomy 2026 lên Google Sheets.

## 📦 Thành phần
- **Agent Role:** `event_tracking_analyst.md`
- **Workflow:** Tự động hóa quy trình bóc tách và ép chuẩn.
- **Skill:** Bộ quy tắc Taxonomy 2026 (Engagement, Transaction, Utility).
- **Engine:** Script Python kết nối Google Sheets API (`manage_event_sheets.py`).

## 🛠 Hướng dẫn cài đặt (Chỉ 1 câu lệnh)

Dán câu lệnh này vào Terminal (Bash) để tải về:
```bash
git clone -b event-tracking-agent https://github.com/hophamquynhmai-afk/gds-myvnpt-wiki-mai.git gds-agent && cd gds-agent && pip install -r requirements.txt
```

## ⚙️ Cấu hình
1. Chuẩn bị file `credentials.json` (Google Cloud Console) đặt cùng thư mục.
2. Đảm bảo bạn có quyền truy cập vào Master Sheet của GDS.

## 🤖 Cách dùng trong Chat AI
Gõ lệnh này kèm link file URD:
`/workflow_create_events_standard [link hoặc path tới file URD]`

---
*Phát triển bởi team GDS - MyVNPT.*
