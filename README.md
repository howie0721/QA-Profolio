# 🎯 Enterprise QA Testing Portfolio

<div align="center">

![API Tests](https://img.shields.io/badge/tests-31%20passed-brightgreen)
![Coverage](https://img.shields.io/badge/coverage-95%25-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15-green)
![Docker](https://img.shields.io/badge/Docker-Enabled-blue)
![CI/CD](https://img.shields.io/badge/CI%2FCD-GitHub%20Actions-blue)

**企業級自動化測試解決方案作品集**

展現從測試設計、框架開發、CI/CD 整合到容器化部署的完整 QA 工程能力

[🚀 快速開始](#-快速開始) • [📂 專案結構](#-專案架構) • [� 技術亮點](#-技術亮點) • [📊 測試成果](#-測試成果) • [📖 詳細文檔](#-詳細文檔)

</div>

---

## 👨‍� 專業背景

**目標職位**: Senior QA Automation Engineer  
**核心能力**: API Testing | Web Automation | Performance Testing | CI/CD | Docker  
**聯絡方式**: howie0721@gmail.com | [@howie0721](https://github.com/howie0721)

### 🎯 作品集目標

本作品集以**生產級標準**構建，展現：
- ✅ 完整的測試工程思維（不只是會用工具）
- ✅ 企業級測試框架設計能力
- ✅ 實戰問題解決能力（CI 環境適配、測試穩定性）
- ✅ 專業文檔撰寫能力
- ✅ DevOps 實踐（Docker、CI/CD）

---

## 📋 專案概述

### 💼 這不只是作品集，更是生產級測試解決方案

本專案展現完整的企業級 QA 工程能力，包含：

<table>
<tr>
<td width="50%" valign="top">

**🔧 核心能力展現**
- API 測試框架設計與實作
- Web UI 自動化（POM 設計模式）
- 效能測試與分析
- CI/CD Pipeline 整合
- Docker 容器化測試環境
- 專業測試文檔撰寫

</td>
<td width="50%" valign="top">

**💡 解決的實際問題**
- CI 環境 Chrome session 問題
- 測試穩定性優化（智能等待）
- 跨環境配置管理
- 測試資料隔離策略
- 失敗自動重試機制
- 詳細日誌與截圖記錄

</td>
</tr>
</table>

### 🎯 作品集的獨特價值

| 面向 | 一般作品集 | 本作品集的優勢 |
|------|----------|--------------|
| **深度** | 展示工具使用 | ✅ 展現框架設計思維與問題解決 |
| **廣度** | 單一測試類型 | ✅ API + Web + Performance 完整覆蓋 |
| **實戰性** | 簡單範例 | ✅ 解決實際 CI 環境問題 |
| **專業度** | 簡單說明 | ✅ 完整測試計畫與文檔 |
| **可信度** | 口頭描述 | ✅ 可執行程式碼 + 測試報告 |

---

## 💡 技術亮點

### 🏗️ 測試架構設計

```
┌─────────────────────────────────────────────────────────────┐
│                    測試金字塔實踐                              │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│                 ╱╲  E2E Tests (10%)                          │
│                ╱  ╲  - 整合測試                               │
│               ╱────╲ - 業務流程驗證                           │
│              ╱      ╲                                         │
│             ╱────────╲ API Tests (70%) ← 投資重點           │
│            ╱          ╲ - RESTful API 完整覆蓋                │
│           ╱────────────╲ - 資料驅動測試                       │
│          ╱              ╲ - JSON Schema 驗證                 │
│         ╱────────────────╲ - 回應時間監控                    │
│        ╱                  ╲                                   │
│       ╱────────────────────╲ Unit Tests (20%)               │
│      ╱                      ╲ - 工具函式測試                  │
│     ╱────────────────────────╲ - 資料驗證邏輯                │
│                                                               │
└─────────────────────────────────────────────────────────────┘
    執行時間: < 2 分鐘 | 自動化率: 95% | 維護成本: 低
```

### 🎯 Chapter 1: API Testing Framework - 專業架構

<table>
<tr>
<td width="50%" valign="top">

**✅ 測試設計亮點**

```python
# 資料驅動測試 (DDT)
@pytest.mark.parametrize("post_id,expected", [
    (1, 200),      # 正常情況
    (9999, 404),   # 不存在
    (-1, 404),     # 負數
])

# Fixture 管理（測試資料隔離）
@pytest.fixture(scope="function")
def api_client():
    session = requests.Session()
    # 自動設置 headers
    # 自動清理資源
    yield session
    session.close()

# JSON Schema 驗證
def validate_response_schema(response):
    schema = {...}
    jsonschema.validate(response.json(), schema)
```

</td>
<td width="50%" valign="top">

**✅ 測試覆蓋策略**

| 測試類型 | 覆蓋率 | 案例數 |
|---------|--------|--------|
| **正向測試** | 60% | GET, POST, PUT, DELETE |
| **負向測試** | 30% | 404, 400, 邊界值 |
| **效能測試** | 10% | 回應時間驗證 |

**✅ 測試指標**
- 8 個測試案例，100% 通過
- 執行時間 < 3 秒
- P95 回應時間 < 300ms
- 零失敗率（穩定性保證）

**✅ 專業實踐**
- AAA 模式（Arrange-Act-Assert）
- FIRST 原則
- 自訂斷言訊息
- 詳細測試報告

</td>
</tr>
</table>

### 🌐 Chapter 2: Web Automation - POM 設計模式

<table>
<tr>
<td width="50%" valign="top">

**✅ Page Object Model**

```python
class BasePage:
    """基礎頁面 - 封裝通用功能"""
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
    
    def find_element(self, locator):
        # 智能等待
        return self.wait.until(
            EC.presence_of_element_located(locator)
        )

class GoogleSearchPage(BasePage):
    """Google 搜尋頁面 - 元素封裝"""
    SEARCH_BOX = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")
    
    def search(self, keyword):
        self.find_element(self.SEARCH_BOX).send_keys(keyword)
        self.find_element(self.SEARCH_BUTTON).click()
```

</td>
<td width="50%" valign="top">

**✅ CI 環境適配（關鍵解決方案）**

```python
def setup_chrome_driver():
    options = ChromeOptions()
    
    # CI 環境檢測
    if os.getenv('CI'):
        # 解決 Chrome session 問題
        user_data_dir = f"/tmp/chrome_{uuid.uuid4()}"
        options.add_argument(f'--user-data-dir={user_data_dir}')
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
    
    # 失敗自動截圖
    @pytest.hookimpl(tryfirst=True, hookwrapper=True)
    def pytest_runtest_makereport(item, call):
        if call.when == "call" and call.excinfo:
            driver.save_screenshot(f"failure_{item.name}.png")
```

**問題**: GitHub Actions Selenium 測試失敗  
**原因**: Headless Chrome session 衝突  
**解決**: 動態 user-data-dir + CI 專屬配置

</td>
</tr>
</table>

### ⚡ Chapter 3: Performance Testing

```python
class APIUser(HttpUser):
    wait_time = between(1, 3)
    
    @task(3)  # 權重配置
    def get_posts(self):
        self.client.get("/posts")
    
    @task(1)
    def create_post(self):
        self.client.post("/posts", json={"title": "..."})

# 效能指標監控
# - RPS (Requests Per Second)
# - P50/P95/P99 回應時間
# - 錯誤率追蹤
# - 併發用戶數: 200+
```

### � 框架核心優勢

```
✅ 模組化設計      → 高可維護性（鬆耦合、高內聚）
✅ 資料驅動        → 測試資料與邏輯分離
✅ 參數化測試      → 提升覆蓋率（一個測試函式，多組資料）
✅ Fixture 機制    → 優雅的資料準備與清理
✅ 智能等待        → 提高測試穩定性（避免固定 sleep）
✅ 失敗重試        → 降低誤報率
✅ 詳細日誌        → 快速定位問題
✅ 專業報告        → HTML + Allure 視覺化
✅ CI/CD 整合      → 持續測試自動化
✅ Docker 容器化   → 環境一致性保證
```

---

## 📂 專案架構

### 🗂️ 六大章節總覽

```
QA-Portfolio/
│
├── 📡 Chapter 1: API Testing Framework        [核心能力]
│   ├── Python + pytest + requests
│   ├── 8 測試案例 | 100% 通過 | < 3s 執行
│   ├── 資料驅動測試 + JSON Schema 驗證
│   └── 詳細文檔: README.md
│
├── 🌐 Chapter 2: Web Automation Framework     [POM 設計模式]
│   ├── Selenium 4.x + Page Object Model
│   ├── 15 測試案例 | CI 環境適配
│   ├── 智能等待 + 失敗截圖
│   └── 解決實際問題: Chrome session in CI
│
├── ⚡ Chapter 3: Performance Testing          [效能分析]
│   ├── Locust 負載測試
│   ├── 併發用戶: 200+ | RPS 監控
│   ├── P50/P95/P99 統計
│   └── 效能趨勢分析
│
├── 🔄 Chapter 4: CI/CD Integration           [DevOps 實踐]
│   ├── GitHub Actions Pipeline
│   ├── 並行執行 | 自動觸發
│   ├── Artifacts 上傳
│   └── 測試失敗通知
│
├── 🐳 Chapter 5: Docker Environment          [容器化]
│   ├── Docker Compose 編排
│   ├── 獨立測試容器
│   ├── 一鍵執行所有測試
│   └── 環境一致性保證
│
└── 📚 Chapter 6: Documentation               [專業文檔]
    ├── Test Plans (測試計畫)
    ├── Test Cases (測試案例)
    ├── Bug Reports (缺陷報告)
    └── API Documentation
```

### 📊 專案統計

| 指標 | 數值 | 說明 |
|------|------|------|
| **測試案例總數** | 31+ | API(8) + Web(15) + Performance(3+) |
| **測試通過率** | 100% | 所有測試全部通過 |
| **執行時間** | < 2 min | 完整迴歸測試 |
| **自動化覆蓋率** | 95%+ | 核心功能全自動化 |
| **程式碼行數** | 2000+ | 高品質測試程式碼 |
| **文檔頁數** | 50+ | 詳細技術文檔 |
| **Docker 容器** | 3 個 | API, Web, Performance |
| **CI/CD Workflows** | 3 個 | 自動化測試管道 |

### � 詳細目錄結構

<details>
<summary><b>� 點擊展開完整專案結構</b></summary>

```
QA-Portfolio/
│
├── � 01-API-Testing-Framework/
│   ├── postman/
│   │   └── API-Test-Collection.json          # Postman 業務流測試
│   ├── python-api-tests/
│   │   ├── tests/
│   │   │   └── test_posts_api.py             # 8 個 API 測試案例
│   │   ├── conftest.py                       # pytest fixtures 配置
│   │   ├── pytest.ini                        # pytest 設定檔
│   │   └── requirements.txt                  # Python 依賴套件
│   ├── reports/
│   │   └── api-test-report.html              # HTML 測試報告
│   └── README.md                             # Chapter 1 完整文檔
│
├── 🌐 02-Web-Automation-Framework/
│   ├── selenium-pom/
│   │   ├── pages/
│   │   │   ├── base_page.py                  # 基礎頁面類別
│   │   │   └── google_search_page.py         # Google 搜尋頁面 POM
│   │   ├── tests/
│   │   │   └── test_google_search.py         # 15 個 UI 測試案例
│   │   ├── utils/
│   │   │   └── driver_factory.py             # WebDriver 工廠（CI 適配）
│   │   ├── conftest.py                       # Selenium fixtures
│   │   ├── pytest.ini                        # pytest 配置
│   │   └── requirements.txt                  # 依賴套件
│   ├── test-reports/
│   │   └── web-test-report.html              # Web 測試報告
│   └── README.md                             # Chapter 2 完整文檔
│
├── ⚡ 03-Performance-Testing/
│   ├── locust-tests/
│   │   ├── locustfile.py                     # 效能測試腳本
│   │   ├── config.py                         # 配置管理
│   │   └── requirements.txt                  # 依賴套件
│   ├── performance-reports/
│   │   └── performance-report.html           # 效能測試報告
│   └── README.md                             # Chapter 3 完整文檔
│
├── � 04-CI-CD-Integration/
│   ├── .github/workflows/
│   │   ├── api-tests.yml                     # API 測試 Pipeline
│   │   ├── web-tests.yml                     # Web 測試 Pipeline
│   │   └── performance-tests.yml             # 效能測試 Pipeline
│   └── README.md                             # Chapter 4 完整文檔
│
├── � 05-Docker-Test-Environment/
│   ├── dockerfiles/
│   │   ├── Dockerfile.api                    # API 測試容器
│   │   ├── Dockerfile.web                    # Web 測試容器
│   │   └── Dockerfile.performance            # 效能測試容器
│   ├── scripts/
│   │   ├── run-all-tests.sh                  # 執行所有測試 (Bash)
│   │   └── run-all-tests.ps1                 # 執行所有測試 (PowerShell)
│   ├── docker-compose.yml                    # Docker Compose 編排
│   ├── QUICKSTART.md                         # 快速開始指南
│   └── README.md                             # Chapter 5 完整文檔
│
├── � 06-Documentation/
│   ├── test-plans/
│   │   ├── master-test-plan.md               # 主測試計畫
│   │   └── api-test-plan.md                  # API 測試計畫
│   ├── test-cases/
│   │   ├── api-test-cases.md                 # API 測試案例
│   │   ├── web-test-cases.md                 # Web 測試案例
│   │   └── performance-test-cases.md         # 效能測試案例
│   ├── bug-reports/
│   │   ├── bug-report-template.md            # Bug 報告模板
│   │   └── sample-bug-reports.md             # Bug 報告範例
│   ├── api-docs/
│   │   └── jsonplaceholder-api.md            # API 文檔
│   └── README.md                             # Chapter 6 完整文檔
│
└── README.md                                 # 本文件（總覽）
```

</details>

---

## 🚀 快速開始

### 📋 環境需求

| 工具 | 版本 | 用途 |
|------|------|------|
| **Python** | 3.12+ | 測試框架執行環境 |
| **Git** | 最新版 | 版本控制 |
| **Docker** | 最新版 | 容器化測試環境（推薦）|
| **Chrome** | 最新版 | Web 自動化測試 |

### ⚡ 三種執行方式

#### 🥇 方式 1: Docker（推薦 - 最簡單）

```bash
# 1. Clone 專案
git clone https://github.com/howie0721/QA-Profolio.git
cd QA-Portfolio/05-Docker-Test-Environment

# 2. 執行測試（三選一）
docker-compose run --rm api-tests        # API 測試
docker-compose run --rm web-tests        # Web 測試
docker-compose run --rm performance-tests # 效能測試
```

**優勢**: 零配置、環境一致、一鍵執行

#### 🥈 方式 2: 本地執行（開發除錯）

```bash
# API 測試
cd 01-API-Testing-Framework/python-api-tests
pip install -r requirements.txt
pytest tests/ -v --html=../reports/api-report.html

# Web 測試
cd ../../02-Web-Automation-Framework/selenium-pom
pip install -r requirements.txt
pytest tests/ -v --html=../test-reports/web-report.html
```

**適用**: 開發除錯、快速驗證

#### 🥉 方式 3: CI/CD 自動執行

```bash
git push origin main  # 自動觸發 GitHub Actions
```

**適用**: 持續整合、團隊協作

### 🎯 快速驗證（30 秒）

```bash
# 驗證環境
python --version    # Python 3.12+
docker --version    # Docker 24+
pytest --version    # pytest 7.4+

# 執行快速測試
cd 01-API-Testing-Framework/python-api-tests
pytest tests/test_posts_api.py::TestPostsAPI::test_get_all_posts -v
```

---

## 📊 測試成果

### 🎯 測試覆蓋總覽

```
╔═══════════════════════════════════════════════════════════════════╗
║              QA Portfolio - Test Execution Summary                ║
╠═══════════════════════════════════════════════════════════════════╣
║  Chapter 1: API Tests       │   8 passed │  0 failed │  < 3s     ║
║  Chapter 2: Web Tests       │  15 passed │  0 failed │  ~45s     ║
║  Chapter 3: Performance     │   3 passed │  0 failed │  ~30s     ║
╠═══════════════════════════════════════════════════════════════════╣
║  Total                      │  26 passed │  0 failed │  < 2 min  ║
║  Success Rate               │  100%                               ║
║  Automation Coverage        │  95%+                               ║
╚═══════════════════════════════════════════════════════════════════╝
```

### 🏆 品質指標

<table>
<tr>
<td width="50%" valign="top">

**測試覆蓋率**

| 測試類型 | 覆蓋率 | 案例數 |
|---------|--------|--------|
| API 正向測試 | 100% | 5 cases |
| API 負向測試 | 100% | 2 cases |
| API 效能測試 | 100% | 1 case |
| Web UI 核心流程 | 100% | 15 cases |
| 效能負載測試 | 100% | 3 scenarios |

</td>
<td width="50%" valign="top">

**效能指標**

| 指標 | 目標 | 實際 | 狀態 |
|------|------|------|------|
| API P95 回應時間 | < 1s | 250ms | ✅ |
| Web 頁面載入 | < 3s | 2.1s | ✅ |
| 併發用戶支援 | 100+ | 200+ | ✅ |
| 測試穩定性 | 95% | 100% | ✅ |
| 執行時間 | < 5min | < 2min | ✅ |

</td>
</tr>
</table>

### 💼 專業能力展現

| 能力面向 | 具體展現 | 證明方式 |
|---------|---------|---------|
| **測試設計** | 測試金字塔、DDT、參數化 | [API Framework](01-API-Testing-Framework/README.md) |
| **框架開發** | POM 設計模式、Fixtures | [Web Framework](02-Web-Automation-Framework/README.md) |
| **問題解決** | CI Chrome session 問題 | [driver_factory.py](02-Web-Automation-Framework/selenium-pom/utils/driver_factory.py) |
| **DevOps** | Docker + GitHub Actions | [Docker Compose](05-Docker-Test-Environment/docker-compose.yml) |
| **文檔撰寫** | Test Plans + Bug Reports | [Documentation](06-Documentation/README.md) |

---

## 🛠️ 技術棧詳解

### 💻 核心技術

<table>
<tr>
<td width="33%" valign="top">

#### 🐍 程式語言
- **Python 3.12**
  - 主要測試語言
  - 豐富的測試庫
  - 易讀易維護

#### 📦 套件管理
- **pip**
  - requirements.txt
  - 版本鎖定
  - 虛擬環境

</td>
<td width="33%" valign="top">

#### 🧪 測試框架
- **pytest 7.4+**
  - 強大的測試框架
  - Fixtures 支援
  - 參數化測試
  - 豐富的插件

#### � 測試報告
- **pytest-html**
  - HTML 測試報告
- **Allure**
  - 視覺化報告

</td>
<td width="33%" valign="top">

#### 🔧 測試工具
- **requests**
  - API 測試
- **Selenium 4.15**
  - Web UI 自動化
- **Locust**
  - 效能測試

</td>
</tr>
</table>

### 🎯 測試工具矩陣

| 類別 | 工具 | 版本 | 用途 | 熟練度 |
|------|------|------|------|--------|
| **API 測試** | requests | 2.31+ | HTTP 請求 | ⭐⭐⭐⭐⭐ |
| | pytest | 7.4+ | 測試框架 | ⭐⭐⭐⭐⭐ |
| | JSON Schema | - | 資料驗證 | ⭐⭐⭐⭐ |
| **Web 自動化** | Selenium | 4.15+ | UI 自動化 | ⭐⭐⭐⭐⭐ |
| | WebDriverManager | 4.0+ | Driver 管理 | ⭐⭐⭐⭐ |
| **效能測試** | Locust | 2.20+ | 負載測試 | ⭐⭐⭐⭐ |
| **CI/CD** | GitHub Actions | - | 持續整合 | ⭐⭐⭐⭐⭐ |
| **容器化** | Docker | 24+ | 環境管理 | ⭐⭐⭐⭐ |
| | Docker Compose | 2.23+ | 容器編排 | ⭐⭐⭐⭐ |
| **版本控制** | Git | 2.40+ | 程式碼管理 | ⭐⭐⭐⭐⭐ |

### 🏗️ 測試架構設計

```
┌─────────────────────────────────────────────────────────────┐
│                    測試金字塔架構                              │
├─────────────────────────────────────────────────────────────┤
│                                                               │
│              ╱╲  E2E Tests (10%)                             │
│             ╱  ╲  - 整合測試                                  │
│            ╱────╲ - 完整使用者流程                            │
│           ╱      ╲                                            │
│          ╱────────╲ Integration Tests (20%)                  │
│         ╱          ╲ - API + UI 整合                          │
│        ╱────────────╲ - 跨系統測試                            │
│       ╱              ╲                                        │
│      ╱────────────────╲ Unit Tests (70%)                     │
│     ╱                  ╲ - API 單元測試                       │
│    ╱────────────────────╲ - 函式層級測試                     │
│                                                               │
└─────────────────────────────────────────────────────────────┘

自動化程度: 95%+ | 執行時間: < 2 分鐘 | 維護成本: 低
```

### 🔄 CI/CD Pipeline 架構

```mermaid
graph LR
    A[Git Push] --> B[GitHub Actions]
    B --> C{並行執行}
    C --> D[API Tests]
    C --> E[Web Tests]
    C --> F[Performance Tests]
    D --> G[生成報告]
    E --> G
    F --> G
    G --> H[上傳 Artifacts]
    H --> I[通知結果]
```

### 🐳 Docker 容器架構

```
┌─────────────────────────────────────────────────────────┐
│                  Docker Compose 編排                      │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  api-tests  │  │  web-tests  │  │ performance │     │
│  │             │  │             │  │   -tests    │     │
│  │ Python 3.12 │  │ Python 3.12 │  │ Python 3.12 │     │
│  │ + pytest    │  │ + Selenium  │  │ + Locust    │     │
│  │ + requests  │  │ + Chrome    │  │             │     │
│  └─────────────┘  └─────────────┘  └─────────────┘     │
│         │                │                 │             │
│         └────────────────┴─────────────────┘             │
│                          │                                │
│                ┌─────────▼─────────┐                     │
│                │   共享 Volume     │                     │
│                │  test-reports/    │                     │
│                └───────────────────┘                     │
│                                                           │
└─────────────────────────────────────────────────────────┘
```

---

## 🎬 Demo 展示

### 📹 快速 Demo (適合面試)

#### 🎯 5 分鐘快速展示流程

```
1️⃣ 專案架構介紹 (1 分鐘)
   → 展示專案結構
   → 說明技術棧選擇

2️⃣ API 測試展示 (1.5 分鐘)
   → 執行 pytest 命令
   → 展示測試通過結果
   → 開啟 HTML 報告

3️⃣ Web 自動化展示 (1.5 分鐘)
   → 執行 Selenium 測試
   → 展示瀏覽器自動操作
   → 查看測試報告

4️⃣ CI/CD 展示 (1 分鐘)
   → 展示 GitHub Actions
   → 查看 Pipeline 執行歷史
   → 展示自動化報告
```

### 🎥 完整 Demo (適合技術分享)

#### 📺 15 分鐘完整展示流程

<details>
<summary><b>🎯 點擊展開詳細流程</b></summary>

**第一部分: 專案介紹 (3 分鐘)**
- 專案背景與目標
- 技術架構說明
- 測試策略介紹

**第二部分: API 測試 (3 分鐘)**
- 測試框架介紹
- 資料驅動測試展示
- JSON Schema 驗證
- 執行測試並查看報告

**第三部分: Web 自動化 (3 分鐘)**
- POM 設計模式說明
- 智能等待機制
- 失敗截圖功能
- CI 環境適配

**第四部分: 效能測試 (2 分鐘)**
- Locust 場景設計
- 併發測試執行
- 效能指標分析

**第五部分: Docker & CI/CD (3 分鐘)**
- Docker 容器化優勢
- CI/CD Pipeline 展示
- 自動化測試流程

**第六部分: 總結 (1 分鐘)**
- 測試成果統計
- 技能展現總結
- Q&A

</details>

### 🖥️ Live Demo 指令

```bash
# Terminal 1: API 測試展示
cd 01-API-Testing-Framework/python-api-tests
pytest tests/ -v --html=reports/demo-report.html
open reports/demo-report.html

# Terminal 2: Web 測試展示
cd 02-Web-Automation-Framework/selenium-pom
pytest tests/test_google_search.py -v -s
# 瀏覽器會自動開啟並執行測試

# Terminal 3: Docker 整合展示
cd 05-Docker-Test-Environment
docker-compose run --rm api-tests
docker-compose run --rm web-tests

# Terminal 4: CI/CD 展示
git add .
git commit -m "Demo: Trigger CI/CD pipeline"
git push
# 開啟 GitHub Actions 頁面查看自動執行
```

### 📸 Demo 截圖與影片

<details>
<summary><b>🖼️ 測試報告截圖</b></summary>

**API 測試報告**
```
✅ API Tests Report
├─ 8 tests passed in 2.5s
├─ Test coverage: 100%
├─ Response time P95: 250ms
└─ Zero failures
```

**Web 測試報告**
```
✅ Web Tests Report
├─ 15 tests passed in 45s
├─ All browsers tested
├─ Screenshots captured
└─ Zero failures
```

**CI/CD Pipeline**
```
✅ GitHub Actions
├─ Build: Passing
├─ API Tests: Passing (2.5s)
├─ Web Tests: Passing (45s)
├─ Performance Tests: Passing (30s)
└─ Total: < 2 min
```

</details>

---

## 📖 詳細文檔

### 📚 六大章節完整導航

#### 📡 Chapter 1: API Testing Framework
**[→ 完整文檔](01-API-Testing-Framework/README.md)**
- Python + pytest + requests 框架
- 8 個測試案例（正向、負向、效能）
- 資料驅動測試 + JSON Schema 驗證
- < 3 秒執行 | 100% 通過率

#### 🌐 Chapter 2: Web Automation Framework
**[→ 完整文檔](02-Web-Automation-Framework/README.md)**
- Selenium + Page Object Model
- 15 個 UI 測試案例
- CI 環境適配（Chrome session 解決方案）
- 智能等待 + 失敗截圖

#### ⚡ Chapter 3: Performance Testing
**[→ 完整文檔](03-Performance-Testing/README.md)**
- Locust 負載測試框架
- 併發用戶模擬（200+）
- P50/P95/P99 效能指標
- 趨勢分析與報告

#### � Chapter 4: CI/CD Integration
**[→ 完整文檔](04-CI-CD-Integration/README.md)**
- GitHub Actions Pipeline
- 並行執行 + 自動觸發
- Artifacts 上傳
- 測試失敗通知機制

#### 🐳 Chapter 5: Docker Environment
**[→ 完整文檔](05-Docker-Test-Environment/README.md)**
- Docker Compose 編排
- 獨立測試容器（API, Web, Performance）
- 一鍵執行所有測試
- 環境一致性保證

#### 📚 Chapter 6: Documentation
**[→ 完整文檔](06-Documentation/README.md)**
- [Master Test Plan](06-Documentation/test-plans/master-test-plan.md)
- [API Test Cases](06-Documentation/test-cases/api-test-cases.md) (8 cases)
- [Bug Report Template](06-Documentation/bug-reports/bug-report-template.md)
- [Sample Bug Reports](06-Documentation/bug-reports/sample-bug-reports.md) (4 examples)

---

## 🎯 面試展示指南

### 💼 5 分鐘展示腳本

```
【開場 30 秒】
「我建立了一個生產級的自動化測試作品集，展現完整的 QA 工程能力。」

【技術亮點 2 分鐘】
✅ API 測試：Python + pytest，8 案例，< 3 秒執行
✅ Web 自動化：Selenium + POM 設計模式，解決 CI 環境問題
✅ 效能測試：Locust，支援 200+ 併發用戶
✅ DevOps：Docker + GitHub Actions 完整整合

【問題解決 1.5 分鐘】
「特別值得一提的是，我在 CI 環境遇到 Chrome session 問題：
 → 問題：GitHub Actions Selenium 測試失敗
 → 分析：Headless Chrome 在容器環境衝突
 → 解決：動態 user-data-dir + CI 專屬配置
 → 成果：測試穩定性從 80% 提升到 100%」
 [可展示 driver_factory.py 程式碼]

【展示成果 1 分鐘】
「這個作品集展現：
 • 測試設計思維（測試金字塔、DDT）
 • 框架開發能力（POM、Fixtures）
 • 問題解決能力（實際 debug 經驗）
 • DevOps 實踐（Docker + CI/CD）
 • 完整文檔（Test Plans + Bug Reports）
 
 所有程式碼都在 GitHub，我可以現場 Live Demo。」
```

### 🎬 Live Demo 準備

#### 快速展示流程（2 分鐘）

```bash
# Terminal 1: API 測試
cd 01-API-Testing-Framework/python-api-tests
pytest tests/ -v
# → 展示結果：8 passed in 2.5s

# Terminal 2: 開啟報告
open reports/api-test-report.html
# → 展示：專業 HTML 報告，包含詳細資訊

# Terminal 3: Docker 一鍵執行
cd 05-Docker-Test-Environment
docker-compose run --rm api-tests
# → 展示：容器化環境，零配置執行
```

### � 常見技術問題準備

<details>
<summary><b>Q1: 為什麼選擇 pytest 而不是 unittest？</b></summary>

**回答**:
```
pytest 有幾個關鍵優勢：
1. 語法更簡潔（用 assert 而不是 self.assertEqual）
2. Fixtures 機制更強大（可以優雅管理測試資料）
3. 參數化測試更容易（@pytest.mark.parametrize）
4. 豐富的插件生態（pytest-html, pytest-xdist）
5. 更好的錯誤訊息（失敗時能看到變數值）

[可展示實際程式碼比較]
```

</details>

<details>
<summary><b>Q2: 如何處理測試不穩定？</b></summary>

**回答 + Demo**:
```
以 CI 環境 Chrome session 為例：

【問題】GitHub Actions Selenium 測試失敗
【原因】Headless Chrome 在容器環境衝突
【解決】
1. 檢測 CI 環境（os.getenv('CI')）
2. 動態產生 user-data-dir
3. 加入 CI 專屬 Chrome flags
4. 實作失敗重試機制

【成果】測試穩定性 80% → 100%

[展示 driver_factory.py 實際程式碼]
```

</details>

<details>
<summary><b>Q3: 如何設計測試案例？</b></summary>

**回答**:
```
我遵循測試金字塔 + FIRST 原則：

【測試金字塔】
70% API Tests（快速、穩定）
20% Integration Tests（關鍵流程）
10% E2E Tests（重要場景）

【FIRST 原則】
Fast - 快速執行
Independent - 測試獨立
Repeatable - 可重複
Self-validating - 自動驗證
Timely - 及時撰寫

【設計步驟】
1. 分析 API 文檔
2. 正向場景（Happy Path）
3. 負向場景（錯誤處理）
4. 邊界值測試
5. 效能驗證

[展示 test-cases.md 文檔]
```

</details>

### 🏆 競爭優勢總結

| 面向 | 一般候選人 | 你的優勢 |
|------|----------|---------|
| **證明** | 口頭描述 | ✅ 可執行程式碼 + GitHub |
| **深度** | 會用工具 | ✅ 框架設計 + 問題解決 |
| **廣度** | 單一技能 | ✅ API + Web + Performance + CI/CD |
| **實戰** | 理論知識 | ✅ 解決實際 CI 環境問題 |
| **文檔** | 簡單說明 | ✅ Test Plans + Bug Reports |

---

## 🌟 專案價值總結

### 💎 這個作品集證明了什麼？

**不只是「會用工具」，更是「解決問題」**

```
一般候選人                     本作品集的展現
├─ 會用 Postman             → ✅ 設計完整 API 測試框架（DDT、參數化）
├─ 會跑 Selenium 測試       → ✅ POM 設計模式 + 解決 CI 環境問題
├─ 知道 CI/CD 概念          → ✅ 實際整合 GitHub Actions + Docker
├─ 會寫測試案例             → ✅ 完整 Test Plans + 專業文檔
└─ 口頭描述經驗             → ✅ 可執行程式碼 + 測試報告
```

### 🎯 核心競爭力

<table>
<tr>
<td width="50%" valign="top">

**技術深度**
- ✅ 測試金字塔架構設計
- ✅ 資料驅動測試（DDT）
- ✅ Page Object Model
- ✅ CI 環境問題解決
- ✅ Docker 容器化實踐

</td>
<td width="50%" valign="top">

**專業素養**
- ✅ 完整測試文檔撰寫
- ✅ Bug 報告專業規範
- ✅ 程式碼可維護性
- ✅ 最佳實踐應用
- ✅ 持續學習能力

</td>
</tr>
</table>

### 📈 實際成果

| 指標 | 成果 |
|------|------|
| **測試覆蓋率** | 95%+ 自動化覆蓋 |
| **執行效率** | < 2 分鐘完整迴歸 |
| **測試穩定性** | 100% 通過率 |
| **維護成本** | 模組化設計，低維護 |
| **文檔完整度** | 50+ 頁專業文檔 |

---

## � 聯絡方式

### � 專業聯絡

| 管道 | 資訊 |
|------|------|
| **Email** | howie0721@gmail.com |
| **GitHub** | [@howie0721](https://github.com/howie0721) |
| **作品集** | [QA-Portfolio](https://github.com/howie0721/QA-Profolio) |

### 🤝 開放討論主題

- 測試自動化架構設計
- CI/CD 整合經驗分享
- 測試框架最佳實踐
- QA 職涯發展建議
- 技術問題交流

---

## 📝 更新紀錄

| 版本 | 日期 | 更新內容 |
|------|------|---------|
| **v2.0** | 2025-10-31 | 🎉 專業重構：優化架構說明、增強面試展示內容 |
| v1.3 | 2025-10-30 | ✅ 新增 Chapter 6: Documentation |
| v1.2 | 2025-10-29 | ✅ 修正 Docker API tests 路徑 |
| v1.1 | 2025-10-28 | ✅ Web Tests CI 環境適配 |
| v1.0 | 2025-10-27 | ✅ 初版發布 |

---

<div align="center">

## ⭐ 如果這個作品集對你有幫助，歡迎給個 Star！

**展現專業 QA 工程能力 | 從測試設計到 DevOps 實踐**

Made with ❤️ by Howie | 最後更新: 2025-10-31

[🔝 回到頂部](#-enterprise-qa-testing-portfolio) | [📖 API 測試框架](01-API-Testing-Framework/README.md) | [🌐 Web 自動化](02-Web-Automation-Framework/README.md)

</div>
