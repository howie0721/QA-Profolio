# 🐳 Docker 測試環境

## 📖 什麼是 Docker?

**Docker** 是一個容器化平台,可以把你的測試環境「打包」成一個標準化的容器,讓測試可以在任何電腦上以完全相同的方式運行。

### 🎯 **為什麼要用 Docker 做測試?**

1. **環境一致性** - 本地、CI/CD、生產環境完全相同
2. **快速部署** - 一個命令就能啟動完整測試環境
3. **隔離性** - 每個測試獨立運行,互不干擾
4. **可重現性** - 任何人都能用同樣的環境重現問題

---

## 📁 專案結構

```
05-Docker-Test-Environment/
├── README.md                    # 本文件
├── docker-compose.yml           # 多容器編排設定檔
├── dockerfiles/                 # 各類測試的 Dockerfile
│   ├── Dockerfile.api          # API 測試容器
│   ├── Dockerfile.web          # Web 自動化測試容器
│   └── Dockerfile.performance  # 效能測試容器
└── scripts/                     # 執行腳本
    ├── run-all-tests.sh        # 執行所有測試
    ├── run-api-tests.sh        # 執行 API 測試
    ├── run-web-tests.sh        # 執行 Web 測試
    └── run-performance-tests.sh # 執行效能測試
```

---

## 🚀 快速開始

### **前置需求**
- 安裝 Docker Desktop (Windows/Mac)
- 安裝 Docker Compose

### **1. 建立所有測試容器**
```bash
docker-compose build
```

### **2. 執行所有測試**
```bash
docker-compose up
```

### **3. 執行特定測試**
```bash
# 只執行 API 測試
docker-compose run api-tests

# 只執行 Web 測試
docker-compose run web-tests

# 只執行效能測試
docker-compose run performance-tests
```

### **4. 清理容器**
```bash
docker-compose down
```

---

## 📊 容器說明

### **1. API Tests Container**
- **基礎映像:** `python:3.12-slim`
- **測試框架:** pytest + requests
- **執行內容:** 8 個 API 測試案例
- **報告輸出:** `test-reports/api-report.html`

### **2. Web Tests Container**
- **基礎映像:** `python:3.12-slim`
- **瀏覽器:** Chrome Headless
- **測試框架:** Selenium + pytest
- **執行內容:** 15 個 Web UI 測試案例
- **報告輸出:** `test-reports/web-report.html`

### **3. Performance Tests Container**
- **基礎映像:** `python:3.12-slim`
- **測試工具:** Locust
- **執行內容:** API 效能壓測
- **報告輸出:** `test-reports/performance-report.html`

---

## 🔧 進階使用

### **查看容器日誌**
```bash
docker-compose logs api-tests
docker-compose logs web-tests
docker-compose logs performance-tests
```

### **進入容器內部除錯**
```bash
docker-compose run api-tests /bin/bash
```

### **僅重建特定容器**
```bash
docker-compose build api-tests
```

### **背景執行測試**
```bash
docker-compose up -d
```

---

## 🎓 學習重點

### **對初學者來說,這個章節學到:**

1. **Docker 基礎概念**
   - 什麼是容器 (Container)
   - 什麼是映像 (Image)
   - Dockerfile 怎麼寫

2. **Docker Compose**
   - 如何管理多個容器
   - 容器間如何共享資料 (Volumes)
   - 如何設定環境變數

3. **測試環境標準化**
   - 如何確保測試環境一致性
   - 如何在 CI/CD 中使用 Docker
   - 如何隔離測試依賴

4. **實戰技能**
   - 建立 Python 測試容器
   - 配置 Chrome Headless 容器
   - 整合測試報告輸出

---

## 📚 相關資源

- [Docker 官方文件](https://docs.docker.com/)
- [Docker Compose 教學](https://docs.docker.com/compose/)
- [Selenium Docker Images](https://github.com/SeleniumHQ/docker-selenium)

---

## ✅ 驗證清單

完成本章後,你應該能夠:

- [ ] 理解 Docker 容器化的概念
- [ ] 能夠撰寫基礎的 Dockerfile
- [ ] 能夠使用 docker-compose 管理多個容器
- [ ] 能夠在容器中執行所有類型的測試
- [ ] 能夠從容器中獲取測試報告
- [ ] 理解如何在 CI/CD 中使用 Docker

---

**下一步:** 完成 Docker 環境設置後,前往 [06-Documentation](../06-Documentation) 學習如何撰寫專業的測試文件。
