# JSONPlaceholder API Documentation

## 📚 API 概述

**JSONPlaceholder** 是一個免費的線上 REST API，提供假資料用於測試與原型開發。

| 項目 | 內容 |
|------|------|
| **Base URL** | https://jsonplaceholder.typicode.com |
| **協定** | HTTPS |
| **認證** | 無需認證 (公開 API) |
| **回應格式** | JSON |
| **支援方法** | GET, POST, PUT, PATCH, DELETE |

---

## 🎯 資源列表

JSONPlaceholder 提供以下資源:

| 資源 | 端點 | 說明 | 資料筆數 |
|------|------|------|----------|
| **Posts** | /posts | 文章 | 100 |
| **Comments** | /comments | 留言 | 500 |
| **Albums** | /albums | 相簿 | 100 |
| **Photos** | /photos | 照片 | 5000 |
| **Todos** | /todos | 待辦事項 | 200 |
| **Users** | /users | 使用者 | 10 |

本文件主要聚焦在 **Posts** 資源的測試。

---

## 📋 Posts API 端點

### 1. 取得所有文章 (Get All Posts)

#### 請求
```http
GET /posts
Host: jsonplaceholder.typicode.com
```

#### 回應範例
```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

[
  {
    "userId": 1,
    "id": 1,
    "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
    "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum..."
  },
  {
    "userId": 1,
    "id": 2,
    "title": "qui est esse",
    "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae..."
  },
  // ... 98 more items
]
```

#### 回應欄位說明

| 欄位 | 型別 | 說明 | 範例 |
|------|------|------|------|
| userId | integer | 文章作者 ID | 1-10 |
| id | integer | 文章 ID | 1-100 |
| title | string | 文章標題 | "sunt aut facere..." |
| body | string | 文章內容 | "quia et suscipit..." |

#### 使用範例

**cURL**
```bash
curl https://jsonplaceholder.typicode.com/posts
```

**Python (requests)**
```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
posts = response.json()
print(f"取得 {len(posts)} 篇文章")
```

**JavaScript (fetch)**
```javascript
fetch('https://jsonplaceholder.typicode.com/posts')
  .then(response => response.json())
  .then(posts => console.log(`取得 ${posts.length} 篇文章`));
```

---

### 2. 取得單一文章 (Get Single Post)

#### 請求
```http
GET /posts/{id}
Host: jsonplaceholder.typicode.com
```

#### 路徑參數

| 參數 | 型別 | 必填 | 說明 |
|------|------|------|------|
| id | integer | ✅ | 文章 ID (1-100) |

#### 回應範例

**成功 (200 OK)**
```json
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum..."
}
```

**失敗 (404 Not Found)**
```json
{}
```

#### 使用範例

**cURL**
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

**Python (requests)**
```python
import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
if response.status_code == 200:
    post = response.json()
    print(f"文章標題: {post['title']}")
else:
    print("文章不存在")
```

---

### 3. 建立文章 (Create Post)

#### 請求
```http
POST /posts
Host: jsonplaceholder.typicode.com
Content-Type: application/json

{
  "userId": 1,
  "title": "新文章標題",
  "body": "文章內容"
}
```

#### 請求 Body 欄位

| 欄位 | 型別 | 必填 | 說明 |
|------|------|------|------|
| userId | integer | ✅ | 文章作者 ID |
| title | string | ✅ | 文章標題 |
| body | string | ✅ | 文章內容 |

#### 回應範例
```json
HTTP/1.1 201 Created
Content-Type: application/json; charset=utf-8

{
  "userId": 1,
  "id": 101,
  "title": "新文章標題",
  "body": "文章內容"
}
```

#### 使用範例

**cURL**
```bash
curl -X POST https://jsonplaceholder.typicode.com/posts \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 1,
    "title": "新文章標題",
    "body": "文章內容"
  }'
```

**Python (requests)**
```python
import requests

new_post = {
    "userId": 1,
    "title": "新文章標題",
    "body": "文章內容"
}

response = requests.post(
    'https://jsonplaceholder.typicode.com/posts',
    json=new_post
)

if response.status_code == 201:
    created_post = response.json()
    print(f"建立成功，新文章 ID: {created_post['id']}")
```

**JavaScript (fetch)**
```javascript
fetch('https://jsonplaceholder.typicode.com/posts', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    userId: 1,
    title: '新文章標題',
    body: '文章內容',
  }),
})
  .then(response => response.json())
  .then(data => console.log('建立成功:', data));
```

---

### 4. 更新文章 (Update Post)

#### 請求 (PUT - 完整更新)
```http
PUT /posts/{id}
Host: jsonplaceholder.typicode.com
Content-Type: application/json

{
  "userId": 1,
  "id": 1,
  "title": "更新後的標題",
  "body": "更新後的內容"
}
```

#### 路徑參數

| 參數 | 型別 | 必填 | 說明 |
|------|------|------|------|
| id | integer | ✅ | 要更新的文章 ID |

#### 回應範例
```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "userId": 1,
  "id": 1,
  "title": "更新後的標題",
  "body": "更新後的內容"
}
```

#### 使用範例

**cURL**
```bash
curl -X PUT https://jsonplaceholder.typicode.com/posts/1 \
  -H "Content-Type: application/json" \
  -d '{
    "userId": 1,
    "id": 1,
    "title": "更新後的標題",
    "body": "更新後的內容"
  }'
```

**Python (requests)**
```python
import requests

updated_post = {
    "userId": 1,
    "id": 1,
    "title": "更新後的標題",
    "body": "更新後的內容"
}

response = requests.put(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=updated_post
)

if response.status_code == 200:
    print("更新成功")
```

---

### 5. 部分更新文章 (Patch Post)

#### 請求 (PATCH - 部分更新)
```http
PATCH /posts/{id}
Host: jsonplaceholder.typicode.com
Content-Type: application/json

{
  "title": "只更新標題"
}
```

#### 回應範例
```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{
  "userId": 1,
  "id": 1,
  "title": "只更新標題",
  "body": "原本的內容"
}
```

#### 使用範例

**Python (requests)**
```python
import requests

partial_update = {
    "title": "只更新標題"
}

response = requests.patch(
    'https://jsonplaceholder.typicode.com/posts/1',
    json=partial_update
)

if response.status_code == 200:
    print("部分更新成功")
```

---

### 6. 刪除文章 (Delete Post)

#### 請求
```http
DELETE /posts/{id}
Host: jsonplaceholder.typicode.com
```

#### 路徑參數

| 參數 | 型別 | 必填 | 說明 |
|------|------|------|------|
| id | integer | ✅ | 要刪除的文章 ID |

#### 回應範例
```json
HTTP/1.1 200 OK
Content-Type: application/json; charset=utf-8

{}
```

#### 使用範例

**cURL**
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

**Python (requests)**
```python
import requests

response = requests.delete('https://jsonplaceholder.typicode.com/posts/1')

if response.status_code == 200:
    print("刪除成功")
```

---

## 🔍 查詢參數 (Query Parameters)

### 依 userId 過濾文章

#### 請求
```http
GET /posts?userId=1
Host: jsonplaceholder.typicode.com
```

#### 回應
回傳所有 userId=1 的文章 (共 10 篇)

#### 使用範例
```python
import requests

response = requests.get(
    'https://jsonplaceholder.typicode.com/posts',
    params={'userId': 1}
)
posts = response.json()
print(f"使用者 1 有 {len(posts)} 篇文章")
```

---

## 📊 HTTP 狀態碼

| 狀態碼 | 說明 | 使用情境 |
|--------|------|----------|
| **200 OK** | 請求成功 | GET, PUT, PATCH, DELETE 成功 |
| **201 Created** | 資源建立成功 | POST 成功建立資源 |
| **404 Not Found** | 資源不存在 | GET 不存在的 ID |
| **500 Internal Server Error** | 伺服器錯誤 | 伺服器異常 |

---

## ⚠️ 重要提醒

### JSONPlaceholder 特性

1. **假資料 (Fake Data)**
   - 所有操作都是模擬的
   - POST/PUT/PATCH/DELETE 不會真正修改資料
   - 每次請求都會回傳相同的資料

2. **無認證**
   - 不需要 API Key 或 Token
   - 任何人都可以存取

3. **Rate Limiting**
   - 無明確的 Rate Limit
   - 建議合理使用，避免過度請求

4. **CORS**
   - 支援 CORS (Cross-Origin Resource Sharing)
   - 可從瀏覽器直接呼叫

---

## 🧪 測試範例

### 完整的測試流程

```python
import requests

BASE_URL = 'https://jsonplaceholder.typicode.com'

# 1. 取得所有文章
response = requests.get(f'{BASE_URL}/posts')
assert response.status_code == 200
assert len(response.json()) == 100
print("✅ 取得所有文章成功")

# 2. 取得單一文章
response = requests.get(f'{BASE_URL}/posts/1')
assert response.status_code == 200
assert response.json()['id'] == 1
print("✅ 取得單一文章成功")

# 3. 建立新文章
new_post = {
    "userId": 1,
    "title": "Test Post",
    "body": "This is a test post"
}
response = requests.post(f'{BASE_URL}/posts', json=new_post)
assert response.status_code == 201
assert response.json()['id'] == 101
print("✅ 建立新文章成功")

# 4. 更新文章
updated_post = {
    "userId": 1,
    "id": 1,
    "title": "Updated Post",
    "body": "This post has been updated"
}
response = requests.put(f'{BASE_URL}/posts/1', json=updated_post)
assert response.status_code == 200
print("✅ 更新文章成功")

# 5. 刪除文章
response = requests.delete(f'{BASE_URL}/posts/1')
assert response.status_code == 200
print("✅ 刪除文章成功")

# 6. 測試不存在的資源
response = requests.get(f'{BASE_URL}/posts/9999')
assert response.status_code == 404
print("✅ 錯誤處理正確")

print("\n🎉 所有測試通過!")
```

---

## 📦 Postman Collection

你可以使用以下 Postman Collection 快速測試 API:

### 匯入方式
1. 開啟 Postman
2. File → Import
3. 選擇 `postman-collection.json`
4. 開始測試

### Collection 結構
```
JSONPlaceholder API
├── Posts
│   ├── Get All Posts
│   ├── Get Single Post
│   ├── Get Non-existent Post (404)
│   ├── Create New Post
│   ├── Update Post
│   └── Delete Post
└── Tests
    └── Run All Tests
```

---

## 🔗 相關資源

- **官方網站**: https://jsonplaceholder.typicode.com/
- **GitHub**: https://github.com/typicode/jsonplaceholder
- **API Guide**: https://jsonplaceholder.typicode.com/guide/

---

## 📚 其他資源端點

### Comments (留言)
```http
GET /posts/1/comments    # 取得文章的所有留言
GET /comments?postId=1   # 用查詢參數取得文章留言
```

### Users (使用者)
```http
GET /users               # 取得所有使用者
GET /users/1             # 取得單一使用者
GET /users/1/posts       # 取得使用者的所有文章
```

### Nested Routes (巢狀路由)
```http
GET /posts/1/comments    # 文章的留言
GET /albums/1/photos     # 相簿的照片
GET /users/1/albums      # 使用者的相簿
GET /users/1/todos       # 使用者的待辦事項
```

---

## 💡 測試建議

### 應該測試的項目
1. ✅ HTTP 狀態碼驗證
2. ✅ 回應資料格式驗證
3. ✅ 必要欄位存在性驗證
4. ✅ 資料型別驗證
5. ✅ 錯誤處理 (404, 500)
6. ✅ 回應時間驗證

### 測試案例範例
- 正向測試: 取得存在的資源
- 負向測試: 取得不存在的資源
- 邊界測試: ID=0, ID=101
- 效能測試: 回應時間 < 1000ms

---

**文件版本**: 1.0  
**最後更新**: 2025-10-31  
**維護者**: QA Team  
**文件位置**: `/06-Documentation/api-docs/jsonplaceholder-api.md`
