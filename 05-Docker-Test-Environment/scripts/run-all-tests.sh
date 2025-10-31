#!/bin/bash

# 執行所有測試容器
# 用途: 一次性執行 API、Web、Performance 測試

set -e  # 遇到錯誤立即停止

echo "=========================================="
echo "🚀 開始執行所有測試"
echo "=========================================="

# 切換到 docker-compose.yml 所在目錄
cd "$(dirname "$0")/.."

# 建立並執行所有測試容器
echo ""
echo "📦 建立測試容器..."
docker-compose build

echo ""
echo "🧪 執行 API 測試..."
docker-compose run --rm api-tests

echo ""
echo "🌐 執行 Web 測試..."
docker-compose run --rm web-tests

echo ""
echo "⚡執行效能測試..."
docker-compose run --rm performance-tests

echo ""
echo "=========================================="
echo "✅ 所有測試執行完成!"
echo "=========================================="
echo ""
echo "📊 測試報告位置:"
echo "  - API Tests: ../01-API-Testing-Framework/test-reports/"
echo "  - Web Tests: ../02-Web-Automation-Framework/selenium-pom/test-reports/"
echo "  - Performance Tests: ../03-Performance-Testing/locust-tests/reports/"
echo ""
