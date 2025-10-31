# API Test Plan - JSONPlaceholder API

## 文件資訊

| 項目 | 內容 |
|------|------|
| **專案名稱** | JSONPlaceholder API Testing |
| **測試類型** | API Functional & Performance Testing |
| **文件版本** | 1.0 |
| **撰寫日期** | 2025-10-31 |
| **測試對象** | https://jsonplaceholder.typicode.com |

---

## 1. 測試目標

### 1.1 主要目標
- 驗證 JSONPlaceholder REST API 的功能正確性
- 確保 API 回應時間符合效能需求
- 驗證錯誤處理機制
- 確保資料格式與 API 文件一致

### 1.2 測試範圍

#### ✅ 測試範圍內
- **/posts** 端點的 CRUD 操作
- **/comments** 端點的查詢操作
- **/users** 端點的查詢操作
- HTTP 狀態碼驗證
- JSON 回應格式驗證
- 錯誤處理驗證
- API 回應時間驗證

#### ❌ 測試範圍外
- 認證與授權 (JSONPlaceholder 為公開 API)
- 資料持久化 (JSONPlaceholder 為 Mock API)
- 併發寫入衝突處理
- Rate Limiting 測試

---

## 2. 測試策略

### 2.1 測試類型優先級

| 測試類型 | 優先級 | 覆蓋率目標 | 自動化 |
|----------|--------|-----------|--------|
| **功能測試** | P0 | 100% | ✅ |
| **正向測試** | P0 | 100% | ✅ |
| **負向測試** | P1 | 80% | ✅ |
| **效能測試** | P1 | 核心端點 | ✅ |
| **資料驗證** | P0 | 100% | ✅ |

### 2.2 測試方法
- **等價類劃分**: 將輸入分為有效與無效等價類
- **邊界值分析**: 測試 ID 邊界值 (0, 1, 100, 101)
- **錯誤猜測**: 測試常見錯誤情境
- **狀態轉換**: 驗證資源的生命週期

---

## 3. API 端點測試矩陣

### 3.1 /posts 端點

| HTTP 方法 | 端點 | 測試案例數 | 優先級 | 狀態 |
|-----------|------|------------|--------|------|
| **GET** | /posts | 3 | P0 | ✅ |
| **GET** | /posts/{id} | 4 | P0 | ✅ |
| **POST** | /posts | 3 | P0 | ✅ |
| **PUT** | /posts/{id} | 2 | P1 | ✅ |
| **PATCH** | /posts/{id} | 1 | P1 | ⏳ |
| **DELETE** | /posts/{id} | 2 | P0 | ✅ |

### 3.2 /comments 端點

| HTTP 方法 | 端點 | 測試案例數 | 優先級 | 狀態 |
|-----------|------|------------|--------|------|
| **GET** | /comments | 2 | P1 | ⏳ |
| **GET** | /comments?postId={id} | 2 | P1 | ⏳ |

### 3.3 /users 端點

| HTTP 方法 | 端點 | 測試案例數 | 優先級 | 狀態 |
|-----------|------|------------|--------|------|
| **GET** | /users | 2 | P2 | ⏳ |
| **GET** | /users/{id} | 2 | P2 | ⏳ |

---

## 4. 測試案例設計

### 4.1 正向測試案例

#### TC-API-001: 取得所有文章
```
測試目標: 驗證 GET /posts 回傳所有文章
前置條件: API 服務正常運作
測試步驟:
  1. 發送 GET 請求至 /posts
  2. 驗證回應狀態碼為 200
  3. 驗證回傳資料為陣列
  4. 驗證陣列包含 100 個項目
  5. 驗證每個項目包含必要欄位
預期結果: 
  - HTTP 200
  - 回傳 100 個文章物件
  - 每個物件包含: userId, id, title, body
```

#### TC-API-002: 取得單一文章
```
測試目標: 驗證 GET /posts/{id} 回傳特定文章
前置條件: API 服務正常運作
測試資料: postId = 1
測試步驟:
  1. 發送 GET 請求至 /posts/1
  2. 驗證回應狀態碼為 200
  3. 驗證回傳資料為物件
  4. 驗證物件 id 為 1
預期結果:
  - HTTP 200
  - 回傳單一文章物件
  - id = 1
```

#### TC-API-004: 建立新文章
```
測試目標: 驗證 POST /posts 可建立新文章
前置條件: API 服務正常運作
測試資料:
  {
    "userId": 1,
    "title": "Test Post",
    "body": "This is a test post"
  }
測試步驟:
  1. 發送 POST 請求至 /posts
  2. 驗證回應狀態碼為 201
  3. 驗證回傳資料包含新 id
  4. 驗證回傳資料與輸入一致
預期結果:
  - HTTP 201
  - 回傳包含 id 的新物件
```

### 4.2 負向測試案例

#### TC-API-003: 取得不存在的文章
```
測試目標: 驗證 GET /posts/{id} 處理不存在的資源
前置條件: API 服務正常運作
測試資料: postId = 9999 (不存在)
測試步驟:
  1. 發送 GET 請求至 /posts/9999
  2. 驗證回應狀態碼為 404
預期結果:
  - HTTP 404
  - 回傳空物件或錯誤訊息
```

#### TC-API-005: 建立缺少必要欄位的文章
```
測試目標: 驗證 POST /posts 的資料驗證
前置條件: API 服務正常運作
測試資料:
  {
    "userId": 1
    // 缺少 title 和 body
  }
測試步驟:
  1. 發送 POST 請求至 /posts
  2. 驗證回應狀態碼
預期結果:
  - HTTP 400 或 422
  - 回傳錯誤訊息
```

### 4.3 效能測試案例

#### TC-API-008: API 回應時間驗證
```
測試目標: 驗證 API 回應時間符合 SLA
前置條件: API 服務正常運作
效能需求: 回應時間 < 1000ms (P95)
測試步驟:
  1. 發送 GET 請求至 /posts
  2. 記錄回應時間
  3. 重複執行 100 次
  4. 計算 P95 回應時間
預期結果:
  - P95 回應時間 < 1000ms
  - P99 回應時間 < 2000ms
```

---

## 5. 資料驗證規則

### 5.1 Post 物件結構
```json
{
  "userId": integer (1-10),
  "id": integer (1-100),
  "title": string (非空),
  "body": string (非空)
}
```

### 5.2 驗證項目
- ✅ 欄位存在性 (必要欄位不可缺少)
- ✅ 資料型別 (int, string, etc.)
- ✅ 資料範圍 (userId: 1-10, id: 1-100)
- ✅ 資料格式 (非空字串)

---

## 6. 測試環境

### 6.1 環境配置

| 項目 | 內容 |
|------|------|
| **Base URL** | https://jsonplaceholder.typicode.com |
| **協定** | HTTPS |
| **測試工具** | pytest + requests |
| **Python 版本** | 3.12 |
| **執行環境** | Local / GitHub Actions / Docker |

### 6.2 測試資料
- 使用 JSONPlaceholder 提供的測試資料
- 不需要資料準備與清理 (Mock API)
- 測試資料獨立且可重複執行

---

## 7. 測試執行

### 7.1 本地執行
```bash
# 進入專案目錄
cd 01-API-Testing-Framework/python-api-tests

# 安裝依賴
pip install -r requirements.txt

# 執行所有測試
pytest tests/ -v

# 執行特定測試
pytest tests/test_posts_api.py -v

# 生成 HTML 報告
pytest tests/ --html=reports/api-report.html --self-contained-html
```

### 7.2 Docker 執行
```bash
# 進入 Docker 環境目錄
cd 05-Docker-Test-Environment

# 執行 API 測試
docker-compose run --rm api-tests

# 查看報告
ls -la test-reports/
```

### 7.3 CI/CD 執行
- 每次 Push 至 main 分支自動觸發
- 每次 Pull Request 自動執行測試
- 測試報告自動上傳至 Artifacts

---

## 8. 測試報告

### 8.1 報告類型
- **HTML 報告**: pytest-html 生成的詳細報告
- **Allure 報告**: 視覺化測試報告
- **CI/CD 日誌**: GitHub Actions 執行日誌

### 8.2 報告內容
- ✅ 測試執行摘要 (通過/失敗/略過)
- ✅ 每個測試案例的執行結果
- ✅ 失敗測試的錯誤訊息
- ✅ 執行時間統計
- ✅ 環境資訊

---

## 9. 缺陷管理

### 9.1 缺陷嚴重度

| 等級 | 定義 | 範例 |
|------|------|------|
| **Critical** | 系統無法運作 | API 完全無回應 |
| **High** | 核心功能失效 | POST 請求無法建立資源 |
| **Medium** | 功能部分失效 | 錯誤訊息不正確 |
| **Low** | 體驗問題 | 回應時間較慢 |

### 9.2 缺陷追蹤
- 使用 Bug Report Template 記錄缺陷
- 將缺陷提交至 GitHub Issues
- 追蹤缺陷修復與驗證

---

## 10. 風險與假設

### 10.1 風險
1. **API 服務不穩定**: JSONPlaceholder 可能維護或中斷
   - 緩解策略: 建立 Mock Server 備用
2. **API 規格變更**: API 端點或回應格式變更
   - 緩解策略: 定期檢查 API 文件、版本控制

### 10.2 假設
1. JSONPlaceholder API 可公開存取
2. API 回應時間穩定
3. 測試資料不會被刪除或修改
4. API 無認證需求

---

## 11. 測試完成標準

測試可以結束當：
- ✅ 所有 P0 測試案例已執行並通過
- ✅ 測試通過率 ≥ 95%
- ✅ 所有 Critical/High 缺陷已修復
- ✅ 測試報告已產生並審查
- ✅ API 效能符合 SLA 需求

---

## 12. 附錄

### 12.1 相關文件
- [API Test Cases](../test-cases/api-test-cases.md)
- [API Documentation](../api-docs/jsonplaceholder-api.md)
- [Bug Report Template](../bug-reports/bug-report-template.md)

### 12.2 測試案例統計

| 狀態 | 數量 | 百分比 |
|------|------|--------|
| ✅ 已完成 | 8 | 50% |
| 🔄 進行中 | 3 | 19% |
| ⏳ 待開始 | 5 | 31% |
| **總計** | **16** | **100%** |

---

**文件擁有者**: QA Team  
**下次審查日期**: 每月第一週  
**文件位置**: `/06-Documentation/test-plans/api-test-plan.md`
