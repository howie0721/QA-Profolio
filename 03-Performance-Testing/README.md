# ⚡ 效能測試框架

## 🎯 這個模組在做什麼？

這裡測試**系統效能和承載能力**，確保：
- ✅ 系統能承受預期的使用者數量
- ✅ 回應時間在可接受範圍內
- ✅ 系統在高負載下不會崩潰
- ✅ 找出系統的效能瓶頸

---

## 🛠️ 使用的工具

### **Locust** - Python 效能測試框架
- 用 Python 寫測試腳本
- 有美觀的 Web UI 介面
- 支援分散式測試
- 即時查看測試結果

---

## 📚 學習步驟

### 步驟 1：安裝 Locust
```powershell
cd 03-Performance-Testing
pip install -r requirements.txt
```

### 步驟 2：啟動 Locust Web UI
```powershell
# 啟動 Locust
locust -f locust-scripts/basic_load_test.py

# 瀏覽器開啟：http://localhost:8089
```

### 步驟 3：設定測試參數
在 Web UI 中設定：
- **Number of users (總使用者數)**：100
- **Spawn rate (每秒增加幾個使用者)**：10
- **Host (目標網址)**：https://jsonplaceholder.typicode.com

### 步驟 4：查看測試結果
- 即時圖表
- 回應時間統計
- 失敗率
- RPS (每秒請求數)

---

## 🏗️ 測試腳本說明

### **基本概念**

```python
from locust import HttpUser, task, between

class MyUser(HttpUser):
    wait_time = between(1, 3)  # 每個請求間隔 1-3 秒
    
    @task(3)  # 權重 3（執行 3 次）
    def get_posts(self):
        self.client.get("/posts")
    
    @task(1)  # 權重 1（執行 1 次）
    def get_single_post(self):
        self.client.get("/posts/1")
```

### **白話解釋**：
- `HttpUser` = 一個虛擬使用者
- `@task` = 使用者會做的事情
- `wait_time` = 每次操作之間等多久
- 權重 = 這個操作執行的頻率

---

## 📊 測試場景

### 場景 1：基本負載測試
- 模擬 100 個使用者
- 測試 API 的基本效能

### 場景 2：壓力測試
- 逐步增加使用者到 500 人
- 找出系統的極限

### 場景 3：尖峰測試
- 突然增加大量使用者
- 模擬突發流量

---

## 📈 效能指標說明

### **回應時間 (Response Time)**
- **50th percentile (中位數)**：50% 的請求回應時間
- **95th percentile**：95% 的請求回應時間
- **99th percentile**：99% 的請求回應時間

**白話**：如果 95th percentile 是 200ms，表示 95% 的使用者在 200ms 內得到回應。

### **RPS (Requests Per Second)**
- 系統每秒能處理多少請求
- 數字越高 = 效能越好

### **失敗率 (Failure Rate)**
- 請求失敗的百分比
- 應該要 < 1%

---

## 🎬 Demo 影片腳本

**展示內容**（3 分鐘）：
1. 啟動 Locust Web UI
2. 設定測試參數（100 users, 10 spawn rate）
3. 開始測試，即時觀察圖表
4. 解釋測試結果（回應時間、RPS、失敗率）
5. 匯出測試報告

---

## 📝 效能測試報告範例

```
測試日期：2025-10-30
測試目標：JSONPlaceholder API
測試場景：基本負載測試

測試結果：
- 總請求數：10,000 次
- 成功率：99.8%
- 平均回應時間：150ms
- 95th percentile：250ms
- 最大併發使用者：100 人
- RPS：66.7 requests/sec

結論：
✅ 系統可以穩定承受 100 個併發使用者
✅ 回應時間在可接受範圍內 (< 300ms)
✅ 失敗率低於 1%
```

---

**下一步**: 查看 `locust-scripts/` 資料夾的測試腳本
