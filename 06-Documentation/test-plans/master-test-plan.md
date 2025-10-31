# Master Test Plan - QA Portfolio 專案

## 文件資訊

| 項目 | 內容 |
|------|------|
| **專案名稱** | QA Portfolio - Automated Testing Framework |
| **文件版本** | 1.0 |
| **撰寫日期** | 2025-10-31 |
| **撰寫者** | QA Engineer |
| **審核者** | - |
| **狀態** | Draft / In Review / Approved |

---

## 1. 專案概述

### 1.1 專案背景
本專案為展示 QA 工程師技能的自動化測試框架集合，涵蓋 API 測試、Web UI 測試、效能測試等多個面向，並整合 CI/CD 與 Docker 容器化技術。

### 1.2 專案目標
- 建立完整的自動化測試框架
- 展現 QA 工程師的技術能力
- 提供可重複使用的測試範例
- 整合 CI/CD 實現持續測試

### 1.3 測試對象
- **API**: JSONPlaceholder REST API (https://jsonplaceholder.typicode.com)
- **Web**: Google 搜尋功能
- **Performance**: 模擬高負載情境的效能測試

---

## 2. 測試策略

### 2.1 測試類型

| 測試類型 | 覆蓋範圍 | 優先級 | 自動化程度 |
|----------|----------|--------|------------|
| **API 測試** | 所有 REST API 端點 | 高 | 100% |
| **功能測試** | 核心業務流程 | 高 | 80% |
| **UI 測試** | 關鍵使用者路徑 | 中 | 70% |
| **效能測試** | 高流量端點 | 中 | 100% |
| **安全測試** | 認證授權機制 | 低 | 50% |

### 2.2 測試方法
- **黑箱測試**: 基於需求規格的功能驗證
- **迴歸測試**: 每次程式碼變更後執行完整測試套件
- **冒煙測試**: 快速驗證核心功能正常運作
- **效能測試**: 模擬實際使用場景的負載測試

### 2.3 測試環境

| 環境 | 用途 | 部署方式 |
|------|------|----------|
| **Local** | 開發與除錯 | Docker Compose |
| **CI/CD** | 自動化測試 | GitHub Actions |
| **Staging** | 整合測試 | - |
| **Production** | 監控測試 | - |

---

## 3. 測試範圍

### 3.1 測試範圍內 (In Scope)

#### API 測試
- ✅ CRUD 操作驗證 (GET, POST, PUT, DELETE)
- ✅ HTTP 狀態碼驗證
- ✅ 回應資料格式驗證
- ✅ 錯誤處理驗證
- ✅ API 回應時間驗證

#### Web UI 測試
- ✅ 搜尋功能驗證
- ✅ 頁面元素驗證
- ✅ 導航功能驗證
- ✅ 跨瀏覽器測試 (Chrome, Firefox)

#### 效能測試
- ✅ 併發使用者模擬
- ✅ 回應時間統計
- ✅ 吞吐量測試
- ✅ 壓力測試

### 3.2 測試範圍外 (Out of Scope)
- ❌ 行動裝置測試 (Mobile Testing)
- ❌ 可用性測試 (Usability Testing)
- ❌ 深度安全測試 (Penetration Testing)
- ❌ 多語系測試 (i18n Testing)

---

## 4. 測試資源

### 4.1 團隊成員

| 角色 | 姓名 | 職責 |
|------|------|------|
| **QA Lead** | - | 測試策略規劃、團隊協調 |
| **QA Engineer** | You | 測試案例設計、自動化開發 |
| **DevOps** | - | CI/CD 整合、環境維護 |

### 4.2 測試工具

| 類型 | 工具 | 用途 |
|------|------|------|
| **API 測試** | pytest + requests | REST API 自動化測試 |
| **Web 測試** | Selenium + Python | Web UI 自動化測試 |
| **效能測試** | Locust | 負載與效能測試 |
| **報告工具** | pytest-html, Allure | 測試報告生成 |
| **CI/CD** | GitHub Actions | 持續整合與部署 |
| **容器化** | Docker, Docker Compose | 測試環境管理 |
| **版本控制** | Git, GitHub | 程式碼版本管理 |

### 4.3 硬體需求
- **本機開發**: Windows/Mac/Linux, 8GB RAM, 20GB 磁碟空間
- **CI/CD Runner**: GitHub Actions (Ubuntu-latest)
- **Docker**: Docker Desktop 或 Docker Engine

---

## 5. 測試時程

### 5.1 測試階段

| 階段 | 活動 | 預計時間 | 狀態 |
|------|------|----------|------|
| **階段 1** | API 測試框架開發 | 1 週 | ✅ 完成 |
| **階段 2** | Web 測試框架開發 | 1 週 | ✅ 完成 |
| **階段 3** | 效能測試框架開發 | 1 週 | ✅ 完成 |
| **階段 4** | CI/CD 整合 | 3 天 | ✅ 完成 |
| **階段 5** | Docker 容器化 | 3 天 | ✅ 完成 |
| **階段 6** | 文件撰寫 | 2 天 | 🔄 進行中 |
| **階段 7** | 專案優化與整理 | 2 天 | ⏳ 待開始 |

### 5.2 里程碑

| 里程碑 | 完成日期 | 交付物 |
|--------|----------|--------|
| **M1: 測試框架建立** | Week 3 | 三種測試框架程式碼 |
| **M2: CI/CD 整合** | Week 4 | GitHub Actions 工作流程 |
| **M3: 容器化部署** | Week 5 | Docker Compose 配置 |
| **M4: 文件完成** | Week 6 | 完整測試文件 |

---

## 6. 風險評估

### 6.1 風險矩陣

| 風險 | 機率 | 影響 | 風險等級 | 應對策略 |
|------|------|------|----------|----------|
| **測試環境不穩定** | 低 | 高 | 中 | 使用 Docker 確保環境一致性 |
| **第三方 API 變更** | 中 | 中 | 中 | 定期檢查 API 文件、建立 Mock Server |
| **CI/CD 執行失敗** | 低 | 中 | 低 | 設定錯誤通知、保留測試日誌 |
| **測試資料不一致** | 中 | 低 | 低 | 使用測試資料工廠、清理資料 |
| **瀏覽器相容性問題** | 低 | 中 | 低 | 使用最新穩定版 WebDriver |

### 6.2 應急計畫
- **API 服務中斷**: 切換至 Mock Server 或本地 API
- **CI/CD 失敗**: 本地執行測試並手動驗證
- **Docker 建置失敗**: 使用本地 Python 環境執行

---

## 7. 測試交付物

### 7.1 測試文件
- ✅ 主測試計畫 (本文件)
- ✅ API 測試計畫
- ✅ 測試案例文件
- ✅ Bug 報告模板
- ✅ API 文件

### 7.2 測試程式碼
- ✅ API 測試框架
- ✅ Web 測試框架
- ✅ 效能測試框架
- ✅ CI/CD 配置檔
- ✅ Docker 配置檔

### 7.3 測試報告
- ✅ HTML 測試報告
- ✅ Allure 測試報告
- ✅ 效能測試報告
- ✅ CI/CD 執行日誌

---

## 8. 成功標準

### 8.1 量化指標

| 指標 | 目標 | 實際 | 狀態 |
|------|------|------|------|
| **測試覆蓋率** | ≥ 80% | 85% | ✅ |
| **測試通過率** | ≥ 95% | 100% | ✅ |
| **API 回應時間** | < 1000ms | 250ms | ✅ |
| **CI/CD 執行時間** | < 5 分鐘 | 3 分鐘 | ✅ |
| **缺陷發現率** | - | - | - |

### 8.2 質化標準
- ✅ 所有測試案例可自動執行
- ✅ 測試報告清楚易讀
- ✅ CI/CD 整合穩定運作
- ✅ Docker 環境可重複部署
- ✅ 文件完整且易於理解

---

## 9. 測試結束標準

測試可以結束當：
1. ✅ 所有測試案例已執行完畢
2. ✅ 測試通過率達到目標 (≥ 95%)
3. ✅ 所有高優先級缺陷已修復並驗證
4. ✅ 測試報告已產生並審查
5. ✅ 測試文件已完成並歸檔

---

## 10. 附錄

### 10.1 相關文件
- [API Test Plan](./api-test-plan.md)
- [API Test Cases](../test-cases/api-test-cases.md)
- [Bug Report Template](../bug-reports/bug-report-template.md)
- [API Documentation](../api-docs/jsonplaceholder-api.md)

### 10.2 參考資料
- [IEEE 829 測試文件標準](https://en.wikipedia.org/wiki/Software_test_documentation)
- [ISTQB 測試術語](https://glossary.istqb.org/)
- [JSONPlaceholder API 文件](https://jsonplaceholder.typicode.com/)

### 10.3 版本歷史

| 版本 | 日期 | 變更內容 | 作者 |
|------|------|----------|------|
| 1.0 | 2025-10-31 | 初版建立 | QA Engineer |

---

## 11. 核准簽名

| 角色 | 姓名 | 簽名 | 日期 |
|------|------|------|------|
| **QA Lead** | - | - | - |
| **Project Manager** | - | - | - |
| **Tech Lead** | - | - | - |

---

**文件擁有者**: QA Team  
**下次審查日期**: 每月第一週  
**文件位置**: `/06-Documentation/test-plans/master-test-plan.md`
