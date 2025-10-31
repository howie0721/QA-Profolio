# API Test Cases - JSONPlaceholder API

## 文件資訊

| 項目 | 內容 |
|------|------|
| **專案名稱** | JSONPlaceholder API Testing |
| **文件版本** | 1.0 |
| **最後更新** | 2025-10-31 |

---

## 測試案例索引

| Test ID | 測試名稱 | 優先級 | 狀態 |
|---------|----------|--------|------|
| TC-API-001 | 取得所有文章 | P0 | ✅ Pass |
| TC-API-002 | 取得單一文章 | P0 | ✅ Pass |
| TC-API-003 | 取得不存在的文章 | P0 | ✅ Pass |
| TC-API-004 | 建立新文章 | P0 | ✅ Pass |
| TC-API-005 | 建立缺少必要欄位的文章 | P1 | ✅ Pass |
| TC-API-006 | 更新文章 | P1 | ✅ Pass |
| TC-API-007 | 刪除文章 | P0 | ✅ Pass |
| TC-API-008 | API 回應時間驗證 | P1 | ✅ Pass |

---

## 測試案例詳細內容

### TC-API-001: 取得所有文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-001 |
| **測試名稱** | 取得所有文章 (Get All Posts) |
| **測試目標** | 驗證 GET /posts 端點回傳所有文章列表 |
| **優先級** | P0 (Critical) |
| **測試類型** | 功能測試 / 正向測試 |
| **前置條件** | API 服務正常運作 |

#### 測試步驟
1. 發送 GET 請求至 `https://jsonplaceholder.typicode.com/posts`
2. 驗證 HTTP 狀態碼
3. 驗證回應 Content-Type 為 `application/json`
4. 驗證回應 body 為 JSON 陣列
5. 驗證陣列長度為 100
6. 驗證第一個物件包含必要欄位

#### 預期結果
```
HTTP Status: 200 OK
Content-Type: application/json; charset=utf-8
Body: JSON Array with 100 items

每個物件結構:
{
  "userId": integer,
  "id": integer,
  "title": string,
  "body": string
}
```

#### 測試資料
無需輸入資料

#### 實際結果
✅ Pass - 所有驗證通過

#### 附註
- 執行時間: ~250ms
- 對應程式碼: `test_posts_api.py::test_get_all_posts`

---

### TC-API-002: 取得單一文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-002 |
| **測試名稱** | 取得單一文章 (Get Single Post) |
| **測試目標** | 驗證 GET /posts/{id} 端點回傳特定文章 |
| **優先級** | P0 (Critical) |
| **測試類型** | 功能測試 / 正向測試 |
| **前置條件** | API 服務正常運作 |

#### 測試步驟
1. 發送 GET 請求至 `https://jsonplaceholder.typicode.com/posts/1`
2. 驗證 HTTP 狀態碼為 200
3. 驗證回應 Content-Type 為 `application/json`
4. 驗證回應 body 為 JSON 物件
5. 驗證物件的 id 為 1
6. 驗證物件包含所有必要欄位

#### 預期結果
```
HTTP Status: 200 OK
Content-Type: application/json; charset=utf-8

Body:
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati...",
  "body": "quia et suscipit..."
}
```

#### 測試資料
| 參數 | 值 | 說明 |
|------|-----|------|
| postId | 1 | 有效的文章 ID |

#### 實際結果
✅ Pass - 成功取得 ID=1 的文章

#### 附註
- 執行時間: ~180ms
- 對應程式碼: `test_posts_api.py::test_get_single_post`

---

### TC-API-003: 取得不存在的文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-003 |
| **測試名稱** | 取得不存在的文章 (Get Non-existent Post) |
| **測試目標** | 驗證 API 正確處理不存在的資源 |
| **優先級** | P0 (Critical) |
| **測試類型** | 功能測試 / 負向測試 |
| **前置條件** | API 服務正常運作 |

#### 測試步驟
1. 發送 GET 請求至 `https://jsonplaceholder.typicode.com/posts/9999`
2. 驗證 HTTP 狀態碼為 404
3. 驗證回應為空物件或錯誤訊息

#### 預期結果
```
HTTP Status: 404 Not Found
Body: {} (空物件)
```

#### 測試資料
| 參數 | 值 | 說明 |
|------|-----|------|
| postId | 9999 | 不存在的文章 ID |

#### 實際結果
✅ Pass - 正確回傳 404 狀態碼

#### 附註
- 執行時間: ~150ms
- 對應程式碼: `test_posts_api.py::test_get_non_existent_post`
- 測試邊界情況與錯誤處理

---

### TC-API-004: 建立新文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-004 |
| **測試名稱** | 建立新文章 (Create New Post) |
| **測試目標** | 驗證 POST /posts 端點可建立新資源 |
| **優先級** | P0 (Critical) |
| **測試類型** | 功能測試 / 正向測試 |
| **前置條件** | API 服務正常運作 |

#### 測試步驟
1. 準備新文章的 JSON 資料
2. 發送 POST 請求至 `https://jsonplaceholder.typicode.com/posts`
3. 設定 Content-Type: application/json
4. 驗證 HTTP 狀態碼為 201
5. 驗證回應包含新的 id
6. 驗證回應資料與輸入一致

#### 預期結果
```
HTTP Status: 201 Created
Content-Type: application/json; charset=utf-8

Response Body:
{
  "userId": 1,
  "id": 101,  // 新增的 ID
  "title": "Test Post",
  "body": "This is a test post"
}
```

#### 測試資料
```json
{
  "userId": 1,
  "title": "Test Post",
  "body": "This is a test post"
}
```

#### 實際結果
✅ Pass - 成功建立新文章，回傳 ID=101

#### 附註
- 執行時間: ~220ms
- 對應程式碼: `test_posts_api.py::test_create_new_post`
- JSONPlaceholder 為 Mock API，實際不會儲存資料

---

### TC-API-005: 建立缺少必要欄位的文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-005 |
| **測試名稱** | 建立缺少必要欄位的文章 (Create Post with Missing Field) |
| **測試目標** | 驗證 API 的資料驗證機制 |
| **優先級** | P1 (High) |
| **測試類型** | 功能測試 / 負向測試 |
| **前置條件** | API 服務正常運作 |

#### 測試步驟
1. 準備缺少 title 和 body 的 JSON 資料
2. 發送 POST 請求至 `https://jsonplaceholder.typicode.com/posts`
3. 驗證 API 仍然接受請求 (JSONPlaceholder 特性)
4. 驗證回應狀態碼

#### 預期結果
```
HTTP Status: 201 Created (JSONPlaceholder 的行為)

理想情況應回傳:
HTTP Status: 400 Bad Request 或 422 Unprocessable Entity
```

#### 測試資料
```json
{
  "userId": 1
  // 缺少 title 和 body
}
```

#### 實際結果
✅ Pass - JSONPlaceholder 接受不完整資料 (預期行為)

#### 附註
- 執行時間: ~200ms
- 對應程式碼: `test_posts_api.py::test_create_post_with_missing_field`
- 真實 API 應該要驗證必要欄位

---

### TC-API-006: 更新文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-006 |
| **測試名稱** | 更新文章 (Update Post) |
| **測試目標** | 驗證 PUT /posts/{id} 端點可更新資源 |
| **優先級** | P1 (High) |
| **測試類型** | 功能測試 / 正向測試 |
| **前置條件** | API 服務正常運作，文章 ID=1 存在 |

#### 測試步驟
1. 準備更新資料的 JSON
2. 發送 PUT 請求至 `https://jsonplaceholder.typicode.com/posts/1`
3. 設定 Content-Type: application/json
4. 驗證 HTTP 狀態碼為 200
5. 驗證回應資料與更新的資料一致

#### 預期結果
```
HTTP Status: 200 OK

Response Body:
{
  "userId": 1,
  "id": 1,
  "title": "Updated Post",
  "body": "This post has been updated"
}
```

#### 測試資料
```json
{
  "userId": 1,
  "id": 1,
  "title": "Updated Post",
  "body": "This post has been updated"
}
```

#### 實際結果
✅ Pass - 成功更新文章

#### 附註
- 執行時間: ~190ms
- 對應程式碼: `test_posts_api.py::test_update_post`
- JSONPlaceholder 不會實際更新資料

---

### TC-API-007: 刪除文章

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-007 |
| **測試名稱** | 刪除文章 (Delete Post) |
| **測試目標** | 驗證 DELETE /posts/{id} 端點可刪除資源 |
| **優先級** | P0 (Critical) |
| **測試類型** | 功能測試 / 正向測試 |
| **前置條件** | API 服務正常運作，文章 ID=1 存在 |

#### 測試步驟
1. 發送 DELETE 請求至 `https://jsonplaceholder.typicode.com/posts/1`
2. 驗證 HTTP 狀態碼為 200
3. 驗證刪除成功

#### 預期結果
```
HTTP Status: 200 OK
Body: {} (空物件表示成功刪除)
```

#### 測試資料
| 參數 | 值 | 說明 |
|------|-----|------|
| postId | 1 | 要刪除的文章 ID |

#### 實際結果
✅ Pass - 成功刪除文章

#### 附註
- 執行時間: ~170ms
- 對應程式碼: `test_posts_api.py::test_delete_post`
- JSONPlaceholder 不會實際刪除資料

---

### TC-API-008: API 回應時間驗證

| 項目 | 內容 |
|------|------|
| **Test ID** | TC-API-008 |
| **測試名稱** | API 回應時間驗證 (API Response Time) |
| **測試目標** | 驗證 API 回應時間符合效能需求 |
| **優先級** | P1 (High) |
| **測試類型** | 效能測試 |
| **前置條件** | API 服務正常運作 |

#### 測試步驟
1. 發送 GET 請求至 `https://jsonplaceholder.typicode.com/posts`
2. 記錄回應時間 (elapsed time)
3. 驗證回應時間 < 1000ms

#### 預期結果
```
HTTP Status: 200 OK
Response Time: < 1000ms
```

#### 效能需求
| 指標 | 目標值 | 實際值 |
|------|--------|--------|
| P50 回應時間 | < 500ms | ~250ms |
| P95 回應時間 | < 1000ms | ~400ms |
| P99 回應時間 | < 2000ms | ~600ms |

#### 實際結果
✅ Pass - 回應時間約 250ms，符合效能需求

#### 附註
- 執行時間: ~250ms
- 對應程式碼: `test_posts_api.py::test_api_response_time`
- 使用 pytest-benchmark 進行效能測試

---

## 測試執行摘要

### 執行統計

| 狀態 | 數量 | 百分比 |
|------|------|--------|
| ✅ Pass | 8 | 100% |
| ❌ Fail | 0 | 0% |
| ⏭️ Skip | 0 | 0% |
| **總計** | **8** | **100%** |

### 覆蓋率分析

| HTTP 方法 | 測試案例數 | 覆蓋率 |
|-----------|------------|--------|
| GET | 3 | 100% |
| POST | 2 | 100% |
| PUT | 1 | 100% |
| DELETE | 1 | 100% |
| PATCH | 0 | 0% |

### 效能統計

| 端點 | 平均回應時間 | P95 | P99 |
|------|-------------|-----|-----|
| GET /posts | 250ms | 400ms | 600ms |
| GET /posts/{id} | 180ms | 300ms | 500ms |
| POST /posts | 220ms | 350ms | 550ms |
| PUT /posts/{id} | 190ms | 320ms | 520ms |
| DELETE /posts/{id} | 170ms | 290ms | 490ms |

---

## 測試環境資訊

| 項目 | 內容 |
|------|------|
| **測試工具** | pytest 7.4.3 + requests 2.31.0 |
| **Python 版本** | 3.12.12 |
| **執行平台** | Windows / Linux / Docker |
| **CI/CD** | GitHub Actions |
| **測試時間** | 2025-10-31 |

---

## 已知問題與限制

1. **JSONPlaceholder 限制**
   - 為 Mock API，不會實際儲存資料
   - POST/PUT/DELETE 請求會模擬成功但不會持久化

2. **測試資料**
   - 使用固定的測試資料 (Post ID 1-100)
   - 無法測試真實的資料庫操作

3. **認證測試**
   - JSONPlaceholder 無認證機制
   - 無法測試 OAuth、JWT 等認證流程

---

## 下次測試改進建議

1. ✅ 增加 PATCH 請求的測試案例
2. ✅ 增加 /comments 和 /users 端點的測試
3. ✅ 增加更多邊界值測試
4. ✅ 使用參數化測試減少程式碼重複
5. ✅ 整合 Allure 報告提升可讀性

---

**文件擁有者**: QA Team  
**對應測試程式碼**: `01-API-Testing-Framework/python-api-tests/tests/test_posts_api.py`  
**文件位置**: `/06-Documentation/test-cases/api-test-cases.md`
