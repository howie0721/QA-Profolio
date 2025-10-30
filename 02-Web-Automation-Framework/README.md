# 🌐 Web 自動化測試框架

## 🎯 這個模組在做什麼？

這裡測試**網頁 UI（使用者介面）**，確保：
- ✅ 網頁元素能正確顯示
- ✅ 按鈕點擊有正確反應
- ✅ 表單能正確提交
- ✅ 跨瀏覽器相容性

---

## 🛠️ 使用的工具

1. **Selenium WebDriver** - 控制瀏覽器的工具
2. **Page Object Model (POM)** - 設計模式，讓程式碼更好維護
3. **pytest** - 測試框架
4. **WebDriverManager** - 自動管理瀏覽器驅動

---

## 📚 學習步驟

### 步驟 1：安裝套件
```powershell
cd 02-Web-Automation-Framework/selenium-pom
pip install -r requirements.txt
```

### 步驟 2：執行測試
```powershell
# 執行所有測試
pytest tests/ -v

# 產生測試報告
pytest tests/ -v --html=../test-reports/web-test-report.html --self-contained-html
```

### 步驟 3：選擇瀏覽器
```powershell
# 使用 Chrome（預設）
pytest tests/ -v

# 使用 Firefox
pytest tests/ -v --browser=firefox

# 使用 Edge
pytest tests/ -v --browser=edge
```

---

## 🏗️ 架構說明

```
selenium-pom/
├── pages/              # 頁面物件（Page Objects）
│   ├── base_page.py   # 基礎頁面類別（所有頁面的父類別）
│   ├── home_page.py   # 首頁
│   └── login_page.py  # 登入頁
├── tests/             # 測試案例
│   ├── conftest.py    # pytest 設定
│   └── test_*.py      # 測試檔案
├── utils/             # 工具類別
│   └── driver_factory.py  # 瀏覽器驅動工廠
└── requirements.txt   # 所需套件
```

### 為什麼要這樣設計？

1. **pages/** - 把每個網頁當成一個「類別」
   - 例如：`LoginPage` 類別包含所有登入頁的元素和操作
   - 好處：網頁改版時，只改這個檔案就好

2. **tests/** - 測試案例
   - 使用 Page Objects 來寫測試
   - 程式碼簡潔易讀

3. **utils/** - 共用工具
   - 建立瀏覽器驅動
   - 設定瀏覽器選項

---

## 📖 測試範例說明

我們會測試一個**練習用的網站**：
- **The Internet** - `https://the-internet.herokuapp.com/`
  - 這是一個專門給測試工程師練習的網站
  - 包含各種常見的測試場景

### 測試項目：
1. ✅ 登入功能
2. ✅ 表單填寫
3. ✅ 下拉選單
4. ✅ 檔案上傳
5. ✅ JavaScript 警告框

---

## 🎬 Demo 影片腳本

**展示內容**（3 分鐘）：
1. 執行測試，看到瀏覽器自動打開
2. 網頁自動操作（填表單、點按鈕）
3. 查看測試報告

---

**下一步**: 查看 `pages/` 資料夾了解 Page Object 設計
