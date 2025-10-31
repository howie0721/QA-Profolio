# 🚀 Docker 測試環境 - 快速入門指南

## 📋 前置準備

### 1. 安裝 Docker Desktop
- **Windows/Mac:** 下載並安裝 [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- **驗證安裝:** 開啟終端機執行
  ```bash
  docker --version
  docker-compose --version
  ```

### 2. 確認 Docker 運行中
- 啟動 Docker Desktop 應用程式
- 確認系統托盤圖示顯示 "Docker is running"

---

## 🎯 使用方式

### **方法 1: 使用 PowerShell 腳本 (Windows 推薦)**

#### 執行所有測試
```powershell
cd 05-Docker-Test-Environment\scripts
.\run-all-tests.ps1
```

### **方法 2: 使用 docker-compose 命令**

#### 建立所有容器
```bash
cd 05-Docker-Test-Environment
docker-compose build
```

#### 執行所有測試
```bash
docker-compose up
```

#### 執行特定測試
```bash
# API 測試
docker-compose run --rm api-tests

# Web 測試
docker-compose run --rm web-tests

# 效能測試
docker-compose run --rm performance-tests
```

#### 清理容器
```bash
docker-compose down
```

---

## 📊 查看測試報告

測試執行完成後,報告會自動生成在以下位置:

```
QA-Portfolio/
├── 01-API-Testing-Framework/test-reports/
│   └── api-docker-report.html
├── 02-Web-Automation-Framework/selenium-pom/test-reports/
│   └── web-docker-report.html
└── 03-Performance-Testing/locust-tests/reports/
    └── performance-docker-report.html
```

直接用瀏覽器開啟 HTML 檔案即可查看報告。

---

## 🔍 常見問題排查

### 問題 1: Docker 容器建置失敗
**解決方法:**
```bash
# 清除所有舊容器和映像
docker-compose down --rmi all
docker system prune -a

# 重新建置
docker-compose build --no-cache
```

### 問題 2: Web 測試失敗 (Chrome 相關)
**原因:** Chrome 在容器中需要更多記憶體

**解決方法:** docker-compose.yml 中已設定 `shm_size: '2gb'`,確保 Docker Desktop 分配足夠記憶體 (建議至少 4GB)

### 問題 3: 容器無法連接網路
**解決方法:**
```bash
# 重新建立網路
docker network rm qa-test-network
docker network create qa-test-network
```

### 問題 4: 測試報告沒有生成
**檢查:**
1. 確認 volumes 掛載路徑正確
2. 查看容器日誌: `docker-compose logs api-tests`
3. 手動進入容器檢查: `docker-compose run --rm api-tests /bin/bash`

---

## 🎓 進階技巧

### 查看容器日誌
```bash
docker-compose logs api-tests
docker-compose logs -f web-tests  # 即時查看
```

### 進入容器內部除錯
```bash
docker-compose run --rm api-tests /bin/bash
```

### 僅重建特定容器
```bash
docker-compose build api-tests
docker-compose build web-tests
```

### 背景執行
```bash
docker-compose up -d
docker-compose ps  # 查看運行狀態
```

### 查看資源使用
```bash
docker stats
```

---

## ✅ 驗證步驟

完成設置後,執行以下命令驗證:

```bash
# 1. 驗證 Docker
docker --version

# 2. 驗證 docker-compose
docker-compose --version

# 3. 驗證映像建置
docker-compose build

# 4. 驗證容器執行
docker-compose run --rm api-tests

# 5. 驗證報告生成
# 檢查 test-reports 資料夾是否有 HTML 檔案
```

---

## 🎉 成功指標

如果看到以下訊息,表示設置成功:

```
✅ 所有測試執行完成!
📊 測試報告位置:
  - API Tests: ../01-API-Testing-Framework/test-reports/
  - Web Tests: ../02-Web-Automation-Framework/selenium-pom/test-reports/
  - Performance Tests: ../03-Performance-Testing/locust-tests/reports/
```

---

**下一步:** 前往 [06-Documentation](../06-Documentation) 學習如何撰寫專業測試文件! 🚀
