#!/bin/bash

# 執行 API 測試容器
# 用途: 單獨執行 API 測試

set -e

echo "=========================================="
echo "🧪 執行 API 測試"
echo "=========================================="

cd "$(dirname "$0")/.."

# 建立並執行 API 測試容器
docker-compose build api-tests
docker-compose run --rm api-tests

echo ""
echo "✅ API 測試完成!"
echo "📊 報告位置: ../01-API-Testing-Framework/test-reports/"
