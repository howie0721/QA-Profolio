# 06-Documentation - 專業文件撰寫

## 📋 章節目標

本章節展示如何撰寫專業的測試文件，包含測試計畫、測試案例、Bug 報告、API 文件等，展現完整的 QA 文件能力。

---

## 📂 目錄結構

```
06-Documentation/
├── README.md                          # 本文件
├── test-plans/                        # 測試計畫文件
│   ├── master-test-plan.md           # 主測試計畫
│   └── api-test-plan.md              # API 測試計畫
├── test-cases/                        # 測試案例文件
│   ├── api-test-cases.md             # API 測試案例
│   ├── web-test-cases.md             # Web 測試案例
│   └── performance-test-cases.md     # 效能測試案例
├── bug-reports/                       # Bug 報告模板與範例
│   ├── bug-report-template.md        # Bug 報告模板
│   └── sample-bug-reports.md         # Bug 報告範例
└── api-docs/                          # API 文件
    ├── jsonplaceholder-api.md        # JSONPlaceholder API 文件
    └── postman-collection.json       # Postman Collection
```

---

## 🎯 學習重點

### 1. 測試計畫 (Test Plan)
- **目的**: 定義測試範圍、策略、資源、時程
- **內容**: 測試目標、測試範圍、測試方法、風險評估
- **展現能力**: 專案規劃、風險管理、策略思維

### 2. 測試案例 (Test Cases)
- **目的**: 詳細記錄測試步驟與預期結果
- **內容**: 測試案例 ID、前置條件、測試步驟、預期結果
- **展現能力**: 細節把控、邏輯思維、可追溯性

### 3. Bug 報告 (Bug Report)
- **目的**: 清楚記錄缺陷資訊，協助開發團隊快速修復
- **內容**: 缺陷標題、重現步驟、實際結果、預期結果、環境資訊
- **展現能力**: 溝通能力、問題分析、文件撰寫

### 4. API 文件 (API Documentation)
- **目的**: 記錄 API 端點、參數、回應格式
- **內容**: API 端點、請求方法、參數說明、範例
- **展現能力**: 技術文件撰寫、API 理解

---

## 📖 使用方式

### 1. 查看測試計畫
```bash
# 查看主測試計畫
cat test-plans/master-test-plan.md

# 查看 API 測試計畫
cat test-plans/api-test-plan.md
```

### 2. 查看測試案例
```bash
# 查看 API 測試案例
cat test-cases/api-test-cases.md

# 查看 Web 測試案例
cat test-cases/web-test-cases.md
```

### 3. 查看 Bug 報告模板
```bash
# 查看 Bug 報告模板
cat bug-reports/bug-report-template.md

# 查看 Bug 報告範例
cat bug-reports/sample-bug-reports.md
```

### 4. 查看 API 文件
```bash
# 查看 API 文件
cat api-docs/jsonplaceholder-api.md
```

---

## 🎓 文件撰寫最佳實踐

### ✅ 測試計畫
1. **明確定義範圍**: 什麼要測、什麼不測
2. **量化測試目標**: 覆蓋率、缺陷率等指標
3. **風險評估**: 識別高風險區域
4. **資源規劃**: 人力、時間、工具

### ✅ 測試案例
1. **唯一 ID**: 方便追蹤與引用
2. **清晰步驟**: 任何人都能執行
3. **可驗證結果**: 預期結果明確
4. **分類標記**: 優先級、類型、模組

### ✅ Bug 報告
1. **清楚標題**: 一眼看出問題
2. **重現步驟**: 開發人員能重現
3. **環境資訊**: 瀏覽器、OS、版本
4. **附上截圖/日誌**: 輔助說明

### ✅ API 文件
1. **完整端點列表**: 所有 API 端點
2. **請求/回應範例**: 實際可用的範例
3. **錯誤碼說明**: 各種錯誤情境
4. **認證說明**: 如何取得 Token

---

## 📊 文件品質檢查清單

- [ ] 所有文件都有清楚的標題與目的
- [ ] 測試案例有唯一 ID 且可追溯
- [ ] Bug 報告包含重現步驟
- [ ] API 文件有完整的請求/回應範例
- [ ] 所有文件使用統一格式
- [ ] 文件有版本控制與更新日期
- [ ] 文件易於閱讀與理解

---

## 🚀 進階應用

### 1. 整合 Jira/Azure DevOps
- 將測試案例匯入測試管理工具
- 連結測試案例與需求
- 追蹤缺陷生命週期

### 2. 自動化文件生成
- 使用 Swagger/OpenAPI 生成 API 文件
- 從程式碼註解生成測試文件
- 自動更新測試覆蓋率報告

### 3. 文件協作
- 使用 Confluence 或 Notion 協作
- 建立文件審查流程
- 定期更新與維護

---

## 💡 面試展示重點

當面試官問到「如何撰寫測試文件」時，你可以展示：

1. **測試計畫**: 展現你的專案規劃與策略思維
2. **測試案例**: 展現你的細節把控與邏輯能力
3. **Bug 報告**: 展現你的溝通與問題分析能力
4. **API 文件**: 展現你的技術理解與文件撰寫能力

說明你如何：
- 根據專案需求訂定測試策略
- 設計可重複執行的測試案例
- 撰寫清楚的 Bug 報告協助團隊溝通
- 維護 API 文件確保測試可維護性

---

## 📚 延伸閱讀

- [IEEE 829 測試文件標準](https://en.wikipedia.org/wiki/Software_test_documentation)
- [如何撰寫有效的 Bug 報告](https://developer.mozilla.org/en-US/docs/Mozilla/QA/Bug_writing_guidelines)
- [API 文件最佳實踐](https://swagger.io/resources/articles/best-practices-in-api-documentation/)
- [測試案例設計技巧](https://www.guru99.com/test-case.html)

---

## ✅ 完成檢查

完成本章節後，你應該能夠：

- ✅ 撰寫完整的測試計畫文件
- ✅ 設計清楚的測試案例
- ✅ 撰寫專業的 Bug 報告
- ✅ 編寫 API 測試文件
- ✅ 優化專案 README
- ✅ 建立文件版本控制流程
