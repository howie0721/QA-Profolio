#  Chapter 2: Web Automation Framework

<div align="center">

![Web Tests](https://img.shields.io/badge/tests-15%20passed-brightgreen)
![Python](https://img.shields.io/badge/Python-3.12-blue)
![Selenium](https://img.shields.io/badge/Selenium-4.15-blue)

**企業級 Web UI 自動化測試框架 - Selenium + POM + pytest**

</div>

---

##  框架概述

採用 **Page Object Model (POM)** 設計模式的企業級 Web UI 自動化測試框架。

###  為什麼重要？

`
 錯誤: 把所有程式碼寫在一個測試檔案裡
 正確: 使用 POM 模式，測試程式碼與頁面元素分離
`

##  快速開始

`powershell
# 安裝依賴
cd selenium-pom
pip install -r requirements.txt

# 執行測試
pytest tests/ -v

# 生成報告
pytest tests/ --html=test-reports/report.html
`

##  POM 架構設計

- **pages/** - 頁面物件層
- **tests/** - 測試案例層  
- **utils/** - 工具函式層

詳細內容請參考 [主 README](../README.md)

