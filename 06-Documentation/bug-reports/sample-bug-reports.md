# Bug Report 範例

本文件展示實際的 Bug 報告範例，涵蓋不同類型與嚴重度的缺陷。

---

## 範例 1: API 錯誤狀態碼問題

### 🐛 Bug 報告編號: BUG-001

#### 📋 基本資訊

| 項目 | 內容 |
|------|------|
| **Bug ID** | BUG-001 |
| **報告日期** | 2025-10-25 |
| **報告者** | QA Engineer |
| **專案名稱** | JSONPlaceholder API Testing |
| **版本** | v1.0.0 |
| **環境** | Production |
| **狀態** | ✅ Fixed |

#### 📝 Bug 摘要
取得不存在的 Post 時，API 回傳空物件而非標準錯誤訊息

#### 🎯 嚴重度與優先級
- **嚴重度**: 🟡 Medium
- **優先級**: 📌 P2

#### 🔍 詳細描述
當使用者嘗試取得不存在的 Post (例如 ID=9999)，API 回傳 HTTP 404 狀態碼，但 response body 為空物件 `{}`，而非標準的錯誤訊息格式。這會導致前端無法顯示明確的錯誤資訊給使用者。

#### 📍 重現步驟
1. 使用 Postman 發送 GET 請求至 `https://jsonplaceholder.typicode.com/posts/9999`
2. 查看 response body
3. 觀察到回傳空物件 `{}`

#### ✅ 預期結果
```json
HTTP Status: 404 Not Found

Response Body:
{
  "error": "Not Found",
  "message": "Post with ID 9999 does not exist",
  "statusCode": 404
}
```

#### ❌ 實際結果
```json
HTTP Status: 404 Not Found

Response Body:
{}
```

#### 🌍 測試環境資訊
- **作業系統**: Windows 11
- **API 版本**: JSONPlaceholder v1
- **測試工具**: Postman 10.0, pytest + requests

#### 🔄 發生頻率
🔴 Always - 每次都會發生

#### 💡 建議解決方案
建議在 API 回應中加入標準的錯誤訊息格式:
```javascript
if (!post) {
  return res.status(404).json({
    error: 'Not Found',
    message: `Post with ID ${id} does not exist`,
    statusCode: 404
  });
}
```

#### ✅ 驗證結果
已驗證修復，API 現在回傳標準錯誤訊息格式。

---

## 範例 2: Web UI 元素定位失敗

### 🐛 Bug 報告編號: BUG-002

#### 📋 基本資訊

| 項目 | 內容 |
|------|------|
| **Bug ID** | BUG-002 |
| **報告日期** | 2025-10-28 |
| **報告者** | QA Engineer |
| **專案名稱** | Google Search Automation |
| **版本** | v1.0.0 |
| **環境** | CI/CD (GitHub Actions) |
| **狀態** | ✅ Fixed |

#### 📝 Bug 摘要
Selenium 測試在 CI 環境中因 Chrome session 問題而失敗

#### 🎯 嚴重度與優先級
- **嚴重度**: 🔴 Critical
- **優先級**: 🔥 P0

#### 🔍 詳細描述
Web 自動化測試在本地環境執行正常，但在 GitHub Actions CI 環境中執行時，Chrome WebDriver 無法啟動，導致所有 15 個測試失敗。錯誤訊息顯示 "session not created: Chrome failed to start"。

#### 📍 重現步驟
1. Push 程式碼至 GitHub 觸發 CI workflow
2. 觀察 GitHub Actions 執行日誌
3. 查看 Web Tests job 失敗
4. 檢查錯誤訊息

#### ❌ 實際結果
```
selenium.common.exceptions.SessionNotCreatedException: 
Message: session not created: Chrome failed to start: exited normally.
  (session not created: DevToolsActivePort file doesn't exist)
  (The process started from chrome location /usr/bin/google-chrome is no longer running)
```

#### 🌍 測試環境資訊
- **作業系統**: Ubuntu 22.04 (GitHub Actions Runner)
- **Chrome 版本**: 120.0
- **ChromeDriver 版本**: 120.0
- **Selenium 版本**: 4.15.2
- **執行環境**: Headless mode in CI

#### 🔄 發生頻率
🔴 Always - 在 CI 環境每次都失敗

#### 💡 解決方案
在 `driver_factory.py` 中新增 CI 環境專用的 Chrome options:

```python
if os.getenv('CI'):
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-gpu')
    
    # 使用唯一的 user-data-dir
    unique_dir = f"/tmp/chrome-user-data-{os.getpid()}-{int(time.time())}"
    options.add_argument(f'--user-data-dir={unique_dir}')
```

#### ✅ 驗證結果
✅ 修復後所有 15 個 Web 測試在 CI 環境中成功執行

#### 🔗 相關資訊
- GitHub PR: #15
- 相關測試: `test_google_search.py`
- CI Run: [GitHub Actions #42](https://github.com/user/repo/actions/runs/42)

---

## 範例 3: 效能測試回應時間超標

### 🐛 Bug 報告編號: BUG-003

#### 📋 基本資訊

| 項目 | 內容 |
|------|------|
| **Bug ID** | BUG-003 |
| **報告日期** | 2025-10-29 |
| **報告者** | Performance QA |
| **專案名稱** | API Performance Testing |
| **版本** | v1.1.0 |
| **環境** | Staging |
| **狀態** | 🔄 In Progress |

#### 📝 Bug 摘要
POST /posts API 在高負載下回應時間超過 SLA 標準

#### 🎯 嚴重度與優先級
- **嚴重度**: 🟠 High
- **優先級**: ⚠️ P1

#### 🔍 詳細描述
在執行負載測試時 (100 併發使用者)，POST /posts 端點的 P95 回應時間達到 3500ms，遠超過 SLA 標準 (P95 < 1000ms)。這會影響使用者體驗，特別是在高流量時段。

#### 📍 重現步驟
1. 使用 Locust 設定 100 併發使用者
2. 持續執行 POST /posts 請求 5 分鐘
3. 查看效能報告的 P95 回應時間
4. 觀察到 P95 為 3500ms

#### ✅ 預期結果
```
Performance SLA:
- P50 回應時間: < 500ms
- P95 回應時間: < 1000ms
- P99 回應時間: < 2000ms
- 錯誤率: < 1%
```

#### ❌ 實際結果
```
Performance Results:
- P50 回應時間: 850ms ❌
- P95 回應時間: 3500ms ❌
- P99 回應時間: 5200ms ❌
- 錯誤率: 0.5% ✅
```

#### 🖼️ 效能圖表

| 指標 | 目標 | 實際 | 狀態 |
|------|------|------|------|
| P50 | < 500ms | 850ms | ❌ |
| P95 | < 1000ms | 3500ms | ❌ |
| P99 | < 2000ms | 5200ms | ❌ |
| 錯誤率 | < 1% | 0.5% | ✅ |

#### 🌍 測試環境資訊
- **測試工具**: Locust 2.20.0
- **併發使用者**: 100
- **測試時長**: 5 分鐘
- **總請求數**: 8,500
- **後端環境**: AWS EC2 t3.medium

#### 🔄 發生頻率
🟠 Often - 在高負載下經常發生

#### 💡 建議解決方案
1. **資料庫優化**
   - 為常用查詢欄位加上索引
   - 優化 SQL 查詢語句
   
2. **快取機制**
   - 使用 Redis 快取熱門資料
   - 設定合理的 TTL
   
3. **水平擴展**
   - 增加 API Server 實例數
   - 使用 Load Balancer 分散流量
   
4. **非同步處理**
   - 將部分處理邏輯移至訊息佇列
   - 減少同步處理時間

#### ⚠️ 影響範圍
- 影響功能: 文章建立功能
- 影響使用者: 高流量時段的所有使用者
- 業務影響: 使用者體驗下降，可能導致流失

#### 🛠️ Workaround
暫時限制 POST 請求的 Rate Limit 為 10 requests/sec/user

#### 📌 附註
- 此問題在低負載 (< 20 使用者) 時不明顯
- 可能與資料庫連線池設定有關
- 需進一步分析資料庫慢查詢日誌

---

## 範例 4: Docker Build 失敗

### 🐛 Bug 報告編號: BUG-004

#### 📋 基本資訊

| 項目 | 內容 |
|------|------|
| **Bug ID** | BUG-004 |
| **報告日期** | 2025-10-31 |
| **報告者** | DevOps QA |
| **專案名稱** | Docker Test Environment |
| **版本** | v1.0.0 |
| **環境** | Local Development |
| **狀態** | ✅ Fixed |

#### 📝 Bug 摘要
Docker Compose build api-tests 失敗，找不到 requirements.txt

#### 🎯 嚴重度與優先級
- **嚴重度**: 🔴 Critical
- **優先級**: 🔥 P0

#### 🔍 詳細描述
執行 `docker-compose build api-tests` 時，Docker 建置過程失敗，錯誤訊息顯示找不到 `01-API-Testing-Framework/requirements.txt`。實際上 requirements.txt 存在於 `01-API-Testing-Framework/python-api-tests/requirements.txt`，但 Dockerfile 的 COPY 指令路徑不正確。

#### 📍 重現步驟
1. 進入 `05-Docker-Test-Environment` 目錄
2. 執行 `docker-compose build api-tests`
3. 觀察建置失敗

#### ❌ 實際結果
```
ERROR [api-tests 3/4] COPY 01-API-Testing-Framework/requirements.txt /app/01-API-Testing-Framework/requirements.txt
------
 > [api-tests 3/4] COPY 01-API-Testing-Framework/requirements.txt /app/01-API-Testing-Framework/requirements.txt:
------
failed to compute cache key: failed to calculate checksum of ref ::01-API-Testing-Framework/requirements.txt: 
"/01-API-Testing-Framework/requirements.txt": not found
```

#### 🌍 測試環境資訊
- **作業系統**: Windows 11
- **Docker 版本**: Docker Desktop 4.25.0
- **Docker Compose 版本**: 2.23.0

#### 🔄 發生頻率
🔴 Always - 每次 build 都失敗

#### 💡 解決方案
修改 `Dockerfile.api` 中的 RUN 指令:

```dockerfile
# 修改前
RUN pip install --no-cache-dir -r /app/01-API-Testing-Framework/requirements.txt

# 修改後
RUN pip install --no-cache-dir -r /app/01-API-Testing-Framework/python-api-tests/requirements.txt
```

同時修改 CMD 指令中的測試路徑:

```dockerfile
# 修改前
CMD ["pytest", "01-API-Testing-Framework/tests/", "-v", ...]

# 修改後
CMD ["pytest", "01-API-Testing-Framework/python-api-tests/tests/", "-v", ...]
```

#### ✅ 驗證結果
✅ Docker build 成功完成  
✅ 容器內所有 8 個 API 測試通過  
✅ 測試報告正確生成

#### 📝 更新記錄

| 日期 | 更新者 | 狀態變更 | 備註 |
|------|--------|----------|------|
| 2025-10-31 10:00 | QA Engineer | 🆕 New | 初次發現問題 |
| 2025-10-31 10:30 | DevOps | 🔄 In Progress | 開始修正 Dockerfile |
| 2025-10-31 11:00 | DevOps | ✅ Fixed | 修正完成 |
| 2025-10-31 11:50 | QA Engineer | ✅ Verified | 驗證通過 |

---

## Bug 報告最佳實踐總結

### ✅ 好的 Bug 報告特徵

1. **清楚的標題**: 一眼就能看出問題
2. **完整的重現步驟**: 任何人都能重現
3. **明確的預期與實際結果**: 清楚對比
4. **詳細的環境資訊**: 版本、OS、瀏覽器等
5. **附上截圖或日誌**: 輔助說明
6. **合理的嚴重度與優先級**: 幫助排程
7. **建設性的建議**: 提供解決方向

### ❌ 避免的錯誤

1. ❌ 標題太模糊: "系統有問題"
2. ❌ 缺少重現步驟: "隨便點點就會壞"
3. ❌ 沒有實際結果: "結果不對"
4. ❌ 缺少環境資訊: "在我的電腦上會壞"
5. ❌ 純粹抱怨: "這個系統真爛"

### 📊 Bug 生命週期

```
🆕 New (新建)
   ↓
🔍 Triaged (已分類)
   ↓
🔄 In Progress (修復中)
   ↓
✅ Fixed (已修復)
   ↓
🧪 Ready for Test (待驗證)
   ↓
✅ Verified (已驗證) / ↩️ Reopened (重新開啟)
   ↓
🏁 Closed (已關閉)
```

---

**文件擁有者**: QA Team  
**範本參考**: [Bug Report Template](./bug-report-template.md)  
**文件位置**: `/06-Documentation/bug-reports/sample-bug-reports.md`
