#!/bin/bash

# 執行 Web 測試容器
# 用途: 單獨執行 Selenium Web 測試

set -e

echo "=========================================="
echo "🌐 執行 Web 自動化測試"
echo "=========================================="

cd "$(dirname "$0")/.."

# 建立並執行 Web 測試容器
docker-compose build web-tests
docker-compose run --rm web-tests

echo ""
echo "✅ Web 測試完成!"
echo "📊 報告位置: ../02-Web-Automation-Framework/selenium-pom/test-reports/"
