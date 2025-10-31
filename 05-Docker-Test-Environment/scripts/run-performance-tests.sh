#!/bin/bash

# 執行效能測試容器
# 用途: 單獨執行 Locust 效能測試

set -e

echo "=========================================="
echo "⚡ 執行效能測試"
echo "=========================================="

cd "$(dirname "$0")/.."

# 建立並執行效能測試容器
docker-compose build performance-tests
docker-compose run --rm performance-tests

echo ""
echo "✅ 效能測試完成!"
echo "📊 報告位置: ../03-Performance-Testing/locust-tests/reports/"
