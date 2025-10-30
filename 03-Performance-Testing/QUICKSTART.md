# Performance Testing Quick Start Guide

## Installation

```powershell
# Navigate to the performance testing directory
cd 03-Performance-Testing

# Install required packages
pip install -r requirements.txt
```

---

## Running Tests

### Option 1: Web UI Mode (Recommended for Beginners)

**Start Locust with Web UI:**
```powershell
cd locust-scripts
locust -f basic_load_test.py
```

**Then:**
1. Open browser: http://localhost:8089
2. Enter test parameters:
   - **Number of users**: 100
   - **Spawn rate**: 10
   - **Host**: https://jsonplaceholder.typicode.com
3. Click **"Start swarming"**
4. Watch real-time results! 📊

---

### Option 2: Headless Mode (No UI)

**Run test from command line:**
```powershell
locust -f locust-scripts/basic_load_test.py `
  --host=https://jsonplaceholder.typicode.com `
  --users 100 `
  --spawn-rate 10 `
  --run-time 5m `
  --headless `
  --html=../performance-reports/test-report.html
```

This will:
- Run for 5 minutes
- Simulate 100 users
- Generate HTML report automatically

---

## Test Scenarios

### Scenario 1: Basic Load Test (Beginner)
```powershell
locust -f locust-scripts/basic_load_test.py
```
- Tests normal usage patterns
- Good starting point

### Scenario 2: Step Load Test (Intermediate)
```powershell
locust -f locust-scripts/step_load_test.py --host=https://jsonplaceholder.typicode.com --users 200 --spawn-rate 10 --run-time 5m
```
- Gradually increases load
- Finds capacity limits

### Scenario 3: Stress Test (Advanced)
```powershell
locust -f locust-scripts/stress_test.py --host=https://jsonplaceholder.typicode.com --users 500 --spawn-rate 50
```
- Pushes system to limits
- Identifies breaking points

---

## Understanding Results

### Key Metrics

| Metric | What it means | Good Value |
|--------|---------------|------------|
| **Average Response Time** | How long requests take on average | < 300ms |
| **95th Percentile** | 95% of requests faster than this | < 500ms |
| **Failure Rate** | % of failed requests | < 1% |
| **RPS** | Requests per second | Higher = better |

### What to Look For

✅ **Good Signs:**
- Response time stays steady as users increase
- Failure rate < 1%
- No errors in logs

⚠️ **Warning Signs:**
- Response time increases sharply
- Failure rate > 1%
- Errors appearing

❌ **Bad Signs:**
- System crashes
- Failure rate > 5%
- Response time > 3 seconds

---

## Exporting Results

### Download HTML Report
In Web UI:
1. Click **"Download Data"** tab
2. Click **"Download Report"**

### Command Line Export
```powershell
# Generate HTML report
locust -f basic_load_test.py --host=https://jsonplaceholder.typicode.com --users 100 --spawn-rate 10 --run-time 2m --headless --html=report.html

# Generate CSV stats
locust -f basic_load_test.py --host=https://jsonplaceholder.typicode.com --users 100 --spawn-rate 10 --run-time 2m --headless --csv=results
```

---

## Tips for Better Tests

### 1. Start Small
- Begin with 10 users
- Gradually increase to find limits

### 2. Run Long Enough
- Minimum 5 minutes for reliable results
- 10-15 minutes for thorough testing

### 3. Monitor Server
- Watch CPU/Memory usage
- Check application logs
- Monitor database

### 4. Test Realistic Scenarios
- Mix different operations
- Use realistic wait times
- Vary request patterns

---

## Troubleshooting

### "Connection refused" error
- Check if target URL is correct
- Ensure target server is running
- Check firewall settings

### Locust won't start
- Make sure Locust is installed: `pip install locust`
- Check Python version: `python --version` (need 3.8+)

### Tests running too slow
- Reduce number of users
- Increase wait times
- Check network connection

---

## Next Steps

After running tests:
1. Review the test report
2. Identify performance bottlenecks
3. Compare with requirements
4. Create action plan for improvements
5. Re-test after optimizations

---

**Happy Testing! 🚀**
