# PowerShell 腳本 - 執行所有測試
# 用途: 在 Windows 上執行所有 Docker 測試

Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "🚀 開始執行所有測試" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan

# 切換到 docker-compose.yml 所在目錄
Set-Location $PSScriptRoot\..

# 建立並執行所有測試容器
Write-Host ""
Write-Host "📦 建立測試容器..." -ForegroundColor Yellow
docker-compose build

if ($LASTEXITCODE -ne 0) {
    Write-Host "❌ 建立容器失敗!" -ForegroundColor Red
    exit 1
}

Write-Host ""
Write-Host "🧪 執行 API 測試..." -ForegroundColor Yellow
docker-compose run --rm api-tests

Write-Host ""
Write-Host "🌐 執行 Web 測試..." -ForegroundColor Yellow
docker-compose run --rm web-tests

Write-Host ""
Write-Host "⚡ 執行效能測試..." -ForegroundColor Yellow
docker-compose run --rm performance-tests

Write-Host ""
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host "✅ 所有測試執行完成!" -ForegroundColor Green
Write-Host "==========================================" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 測試報告位置:" -ForegroundColor Yellow
Write-Host "  - API Tests: ..\01-API-Testing-Framework\test-reports\"
Write-Host "  - Web Tests: ..\02-Web-Automation-Framework\selenium-pom\test-reports\"
Write-Host "  - Performance Tests: ..\03-Performance-Testing\locust-tests\reports\"
Write-Host ""
