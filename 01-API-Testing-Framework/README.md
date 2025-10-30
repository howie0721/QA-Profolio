# 📡 API 測試框架

## 🎯 這個模組在做什麼？

這裡測試**後端 API**，確保：
- ✅ API 能正確回應
- ✅ 回應速度夠快
- ✅ 回應的資料格式正確
- ✅ 錯誤情況有正確處理

---

## 🛠️ 使用的工具

1. **Postman** - 手動測試 API（像用滑鼠點點看）
2. **Newman** - 自動執行 Postman 測試（讓電腦自動測）
3. **Python + pytest** - 寫程式碼來測試 API

---

## 📚 學習步驟

### 步驟 1：安裝 Newman
```powershell
npm install -g newman newman-reporter-htmlextra
```

### 步驟 2：安裝 Python 套件
```powershell
cd 01-API-Testing-Framework/python-api-tests
pip install -r requirements.txt
```

### 步驟 3：執行測試
```powershell
# 執行 Python API 測試
pytest tests/ -v --html=../reports/api-test-report.html

# 執行 Postman 測試
newman run postman/API-Test-Collection.json -r htmlextra --reporter-htmlextra-export reports/postman-report.html
```

---

## 📖 測試範例說明

我們會測試一個**免費的公開 API**：`https://jsonplaceholder.typicode.com`

這是一個假資料 API，專門給開發者練習用的。

### 測試項目：
1. **GET** - 取得資料（查詢）
2. **POST** - 新增資料（建立）
3. **PUT** - 更新資料（修改）
4. **DELETE** - 刪除資料

---

## 🎬 Demo 影片腳本

**展示內容**（3 分鐘）：
1. 打開 Postman，展示測試集合
2. 執行一次完整的測試
3. 查看測試報告（成功/失敗統計）

---

**下一步**: 前往 `python-api-tests` 資料夾查看測試程式碼
