# Bug Report Template

## 🐛 Bug 報告編號: BUG-XXXX

---

## 📋 基本資訊

| 項目 | 內容 |
|------|------|
| **Bug ID** | BUG-XXXX |
| **報告日期** | YYYY-MM-DD |
| **報告者** | 你的名字 |
| **專案名稱** | 專案名稱 |
| **版本** | v1.0.0 |
| **環境** | Development / Staging / Production |
| **狀態** | 🆕 New / 🔄 In Progress / ✅ Fixed / 🚫 Won't Fix |

---

## 📝 Bug 摘要

**簡短描述問題 (一句話)**

範例: API 回傳錯誤的 HTTP 狀態碼 500 而非 404

---

## 🎯 嚴重度與優先級

### 嚴重度 (Severity)
- [ ] 🔴 Critical - 系統無法運作，影響所有使用者
- [ ] 🟠 High - 核心功能失效，影響大部分使用者
- [ ] 🟡 Medium - 功能部分失效，有替代方案
- [ ] 🟢 Low - 輕微問題，不影響主要功能

### 優先級 (Priority)
- [ ] 🔥 P0 - 立即修復
- [ ] ⚠️ P1 - 本次發布前修復
- [ ] 📌 P2 - 下次發布修復
- [ ] 💡 P3 - 有時間再修復

---

## 🔍 詳細描述

**詳細說明問題的現象與影響範圍**

範例:
當發送 GET 請求至不存在的資源 (例如 /posts/9999) 時，API 應回傳 HTTP 404 Not Found，但實際回傳 500 Internal Server Error。這會導致前端無法正確處理錯誤情境。

---

## 📍 重現步驟 (Steps to Reproduce)

**提供清楚的步驟，讓任何人都能重現此問題**

1. 開啟 Postman 或終端機
2. 發送 GET 請求至 `https://api.example.com/posts/9999`
3. 查看回應的 HTTP 狀態碼
4. 觀察到回傳 500 而非 404

---

## ✅ 預期結果 (Expected Result)

**描述正確的行為應該是什麼**

```
HTTP Status: 404 Not Found
Content-Type: application/json

Response Body:
{
  "error": "Resource not found",
  "message": "Post with ID 9999 does not exist"
}
```

---

## ❌ 實際結果 (Actual Result)

**描述實際發生的錯誤行為**

```
HTTP Status: 500 Internal Server Error
Content-Type: application/json

Response Body:
{
  "error": "Internal Server Error",
  "message": "Cannot read property 'id' of undefined"
}
```

---

## 🖼️ 截圖/影片 (Screenshots/Videos)

**附上截圖或螢幕錄影，輔助說明問題**

![Error Screenshot](path/to/screenshot.png)

或提供影片連結: [https://example.com/video.mp4](https://example.com/video.mp4)

---

## 📋 日誌/錯誤訊息 (Logs/Error Messages)

**附上相關的日誌或錯誤訊息**

```
[2025-10-31 10:30:45] ERROR: Cannot read property 'id' of undefined
    at getPostById (api/posts.js:45:12)
    at Layer.handle (express/lib/router/layer.js:95:5)
    at next (express/lib/router/route.js:137:13)

Stack Trace:
TypeError: Cannot read property 'id' of undefined
    at /app/controllers/postController.js:23:18
    at Layer.handle [as handle_request] (/app/node_modules/express/lib/router/layer.js:95:5)
```

---

## 🌍 測試環境資訊

### 作業系統
- [ ] Windows 11
- [ ] macOS 14.0
- [ ] Ubuntu 22.04
- [ ] 其他: ___________

### 瀏覽器 (如適用)
- [ ] Chrome 120.0
- [ ] Firefox 121.0
- [ ] Safari 17.0
- [ ] Edge 120.0

### 裝置 (如適用)
- [ ] Desktop
- [ ] Laptop
- [ ] Mobile (iOS)
- [ ] Mobile (Android)
- [ ] Tablet

### API/後端資訊
- **API 版本**: v1.2.3
- **後端框架**: Express.js 4.18.0
- **資料庫**: PostgreSQL 15.0
- **部署環境**: AWS EC2

### 網路環境
- **連線方式**: WiFi / 4G / 5G
- **網路速度**: 100 Mbps
- **VPN**: 是 / 否

---

## 🔄 發生頻率 (Frequency)

- [ ] 🔴 Always - 每次都會發生 (100%)
- [ ] 🟠 Often - 經常發生 (> 50%)
- [ ] 🟡 Sometimes - 有時發生 (< 50%)
- [ ] 🟢 Rarely - 很少發生 (< 10%)
- [ ] ⚪ Once - 只發生過一次

---

## 🔗 相關資訊

### 相關 Bug/Issue
- 相關 Bug ID: BUG-0123
- GitHub Issue: #456
- Jira Ticket: PROJ-789

### 相關測試案例
- Test Case ID: TC-API-003
- 測試文件: [API Test Cases](../test-cases/api-test-cases.md)

### 相關文件
- API 文件: [API Documentation](../api-docs/jsonplaceholder-api.md)
- 需求規格: [Product Requirements](link-to-requirements)

---

## 💡 建議解決方案 (Optional)

**如果你有想法，可以提供可能的解決方案**

範例:
建議在 `getPostById` 函數中加入 null check:

```javascript
async function getPostById(id) {
  const post = await Post.findById(id);
  
  if (!post) {
    return res.status(404).json({
      error: 'Not Found',
      message: `Post with ID ${id} does not exist`
    });
  }
  
  return res.status(200).json(post);
}
```

---

## 🧪 測試資料 (Test Data)

**提供重現問題所需的測試資料**

```json
{
  "postId": 9999,
  "endpoint": "https://api.example.com/posts/9999",
  "method": "GET",
  "headers": {
    "Content-Type": "application/json",
    "Authorization": "Bearer test-token-123"
  }
}
```

---

## ⚠️ 影響範圍 (Impact)

**描述此 Bug 影響的範圍**

- ✅ 影響的功能模組: Post Management API
- ✅ 影響的使用者: 所有 API 使用者
- ✅ 業務影響: 前端無法正確顯示錯誤訊息
- ✅ 安全影響: 可能洩漏內部錯誤資訊

---

## 🛠️ Workaround (暫時解決方案)

**如果有暫時的替代方案，請說明**

範例:
在前端加入錯誤處理，將所有 5xx 錯誤視為「找不到資源」:

```javascript
if (response.status >= 500 && response.status < 600) {
  // 暫時視為 404 處理
  showNotFoundError();
}
```

---

## 📌 附註 (Additional Notes)

**其他補充資訊**

- 此問題在 v1.2.0 版本首次出現
- 可能與最近的資料庫遷移有關
- 僅在生產環境發生，開發環境無此問題

---

## ✅ 驗證標準 (Verification Criteria)

**修復後需要驗證的項目**

- [ ] API 回傳正確的 404 狀態碼
- [ ] 錯誤訊息格式正確
- [ ] 不再出現 500 錯誤
- [ ] 現有的正向測試案例仍然通過
- [ ] 前端能正確處理 404 回應

---

## 📝 更新記錄 (Update History)

| 日期 | 更新者 | 狀態變更 | 備註 |
|------|--------|----------|------|
| 2025-10-31 | QA Engineer | 🆕 New → 🔄 In Progress | 已指派給 Backend Team |
| 2025-11-01 | Developer | 🔄 In Progress → ✅ Fixed | 已修復，PR #123 |
| 2025-11-02 | QA Engineer | ✅ Fixed → ✅ Verified | 驗證通過，已關閉 |

---

## 🏷️ 標籤 (Tags)

`API` `Backend` `Error-Handling` `HTTP-Status-Code` `P1` `High-Severity`

---

**報告範本版本**: 1.0  
**最後更新**: 2025-10-31  
**範本位置**: `/06-Documentation/bug-reports/bug-report-template.md`
