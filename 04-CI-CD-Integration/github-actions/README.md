# GitHub Actions CI/CD Setup Guide

## 📋 Overview

This directory contains GitHub Actions workflow configurations for automating the QA Portfolio test suite directly on GitHub.

---

## 🎯 What is GitHub Actions?

GitHub Actions is a CI/CD platform that lets you automate your build, test, and deployment pipeline directly in GitHub. No external servers needed!

### Key Benefits:
- ✅ **Free for public repos** (2,000 minutes/month for private repos)
- ✅ **No setup required** - runs on GitHub's servers
- ✅ **Easy to configure** - YAML files in `.github/workflows/`
- ✅ **Great for demos** - perfect for portfolio projects

---

## 📂 Workflow Files

```
.github/workflows/
├── api-tests.yml              # API test automation
├── web-tests.yml              # Web UI test automation
├── performance-tests.yml      # Performance test automation
├── full-test-suite.yml        # Run all tests together
└── README.md                  # This file
```

---

## 🚀 Quick Start

### Step 1: Push to GitHub

All workflow files are already in place. Simply push to your repository:

```powershell
git add .
git commit -m "Add CI/CD workflows"
git push origin main
```

### Step 2: Workflows Activate Automatically

Once pushed, workflows will:
- ✅ Run on every push to `main` branch
- ✅ Run on every pull request
- ✅ Can be triggered manually

### Step 3: View Results

1. Go to your GitHub repository
2. Click "Actions" tab
3. See all workflow runs and their status

---

## 📊 Workflow Details

### 1. API Tests (`api-tests.yml`)

**Triggers:**
- Push to `main` (if API files changed)
- Pull requests
- Manual trigger

**What it does:**
```
1. Checks out code
2. Sets up Python 3.12
3. Installs dependencies
4. Runs pytest API tests
5. Uploads HTML test report
```

**Run manually:**
1. Go to Actions → API Tests
2. Click "Run workflow"
3. Select branch → Run

### 2. Web Tests (`web-tests.yml`)

**Triggers:**
- Push to `main` (if Web files changed)
- Pull requests
- Manual trigger

**What it does:**
```
1. Checks out code
2. Sets up Python 3.12
3. Installs Chrome browser
4. Runs Selenium tests (headless mode)
5. Uploads test reports and screenshots
```

**Special Features:**
- Runs in headless mode (no GUI)
- Takes screenshots on failure
- Supports multiple browsers (Chrome, Firefox)

### 3. Performance Tests (`performance-tests.yml`)

**Triggers:**
- Daily at 2 AM UTC (scheduled)
- Manual trigger with custom parameters

**What it does:**
```
1. Checks out code
2. Sets up Python 3.12
3. Installs Locust
4. Runs load test with configurable users/duration
5. Uploads performance reports
```

**Parameters (Manual Run):**
- `users`: Number of concurrent users (default: 50)
- `duration`: Test duration (default: 2m)

**Run manually:**
```
1. Go to Actions → Performance Tests
2. Click "Run workflow"
3. Enter parameters:
   - Users: 100
   - Duration: 5m
4. Click "Run workflow"
```

### 4. Full Test Suite (`full-test-suite.yml`)

**Triggers:**
- Push to `main`
- Pull requests
- Every Monday at 8 AM UTC
- Manual trigger

**What it does:**
```
1. Runs API tests
2. If API tests pass → Runs Web tests
3. If Web tests pass → Runs Performance tests
4. Generates combined summary report
```

**Why use this:**
- Complete test coverage
- Tests run in sequence
- Single place to see all results

---

## 🎮 How to Use

### Method 1: Automatic (Recommended)

Just push your code - workflows run automatically!

```powershell
# Make changes
git add .
git commit -m "Add new test cases"
git push origin main

# Check GitHub Actions tab to see results
```

### Method 2: Manual Trigger

Perfect for testing before merging:

```
1. Go to repository → Actions
2. Choose a workflow
3. Click "Run workflow" button
4. Select branch
5. Click green "Run workflow" button
```

### Method 3: Pull Request

Create a PR to see test results before merging:

```powershell
# Create feature branch
git checkout -b feature/new-tests

# Make changes
git add .
git commit -m "Add new tests"
git push origin feature/new-tests

# Create PR on GitHub
# Tests run automatically on PR
```

---

## 📈 Understanding Workflow Status

### Status Icons

- ✅ **Green check** = All tests passed
- ❌ **Red X** = Tests failed
- 🟡 **Yellow dot** = Tests running
- ⚪ **Gray circle** = Tests queued
- ⏭️ **Skip icon** = Tests skipped

### Where to Find Results

1. **Actions Tab**
   - See all workflow runs
   - Filter by workflow, branch, or status

2. **Commit Status**
   - Each commit shows test status
   - Green checkmark = all passed

3. **Pull Request Checks**
   - PRs show required checks
   - Must pass before merge

4. **Test Reports**
   - Click on workflow run
   - Download artifacts (HTML reports)

---

## 📁 Downloading Test Reports

### Step-by-Step:

1. Go to Actions → Select a workflow run
2. Scroll down to "Artifacts" section
3. Download:
   - `api-test-report` (API tests)
   - `web-test-report` (Web tests)
   - `performance-test-report` (Performance tests)
   - `failure-screenshots` (if tests failed)

4. Extract ZIP file
5. Open `.html` files in browser

---

## 🔧 Customizing Workflows

### Change Trigger Conditions

```yaml
# Run only on specific branches
on:
  push:
    branches: [ main, develop ]

# Run only when certain files change
on:
  push:
    paths:
      - 'tests/**'
      - 'src/**'
```

### Add Notifications

**Slack Notification:**
```yaml
- name: Slack Notification
  uses: 8398a7/action-slack@v3
  with:
    status: ${{ job.status }}
    text: 'Test Results: ${{ job.status }}'
    webhook_url: ${{ secrets.SLACK_WEBHOOK }}
```

**Email Notification:**
```yaml
- name: Send Email
  uses: dawidd6/action-send-mail@v3
  with:
    server_address: smtp.gmail.com
    server_port: 465
    username: ${{ secrets.EMAIL_USERNAME }}
    password: ${{ secrets.EMAIL_PASSWORD }}
    subject: Test Results
    body: Tests completed with status ${{ job.status }}
    to: your.email@example.com
```

### Add More Test Environments

```yaml
strategy:
  matrix:
    python-version: [3.10, 3.11, 3.12]
    os: [ubuntu-latest, windows-latest, macos-latest]
```

---

## 🐛 Troubleshooting

### Issue: Workflow not running

**Check:**
1. Workflow file is in `.github/workflows/` folder
2. YAML syntax is correct (use YAML validator)
3. Branch name matches trigger condition

### Issue: Tests failing on GitHub but passing locally

**Common causes:**
1. Different Python version
2. Missing environment variables
3. Headless mode issues (for Web tests)

**Solution:**
```yaml
- name: Debug Info
  run: |
    python --version
    pip list
    pwd
    ls -la
```

### Issue: Browser tests fail

**Solution:** Ensure headless mode is enabled
```yaml
env:
  HEADLESS: true
```

### Issue: Artifacts not uploaded

**Check:**
1. Path is correct
2. Files exist after test run
3. Use `if: always()` to upload even on failure

---

## 💰 GitHub Actions Usage Limits

### Free Tier (Public Repos)
- ✅ **Unlimited minutes**
- ✅ 20 concurrent jobs

### Free Tier (Private Repos)
- ⏱️ 2,000 minutes/month
- 👥 20 concurrent jobs

### Tips to Save Minutes:
1. Use `paths` filter to run only when needed
2. Cache dependencies (`cache: 'pip'`)
3. Run performance tests only on schedule
4. Cancel previous runs on new push

---

## 🎯 Best Practices

1. **Use Matrix Strategy**
   ```yaml
   strategy:
     matrix:
       python-version: [3.10, 3.12]
   ```

2. **Cache Dependencies**
   ```yaml
   - uses: actions/setup-python@v5
     with:
       cache: 'pip'
   ```

3. **Fail Fast**
   ```yaml
   strategy:
     fail-fast: true
   ```

4. **Always Upload Reports**
   ```yaml
   - uses: actions/upload-artifact@v4
     if: always()
   ```

5. **Add Status Badges**
   ```markdown
   ![API Tests](https://github.com/username/repo/workflows/API%20Tests/badge.svg)
   ```

---

## 📊 Adding Status Badges to README

Add these to your main README.md:

```markdown
## Build Status

![API Tests](https://github.com/howie0721/QA-Profolio/workflows/API%20Tests/badge.svg)
![Web Tests](https://github.com/howie0721/QA-Profolio/workflows/Web%20Automation%20Tests/badge.svg)
![Performance Tests](https://github.com/howie0721/QA-Profolio/workflows/Performance%20Tests/badge.svg)
```

---

## 📚 Additional Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Marketplace (Pre-built Actions)](https://github.com/marketplace?type=actions)
- [Example Workflows](https://github.com/actions/starter-workflows)

---

## 🆚 GitHub Actions vs Jenkins

| Feature | GitHub Actions | Jenkins |
|---------|---------------|---------|
| **Setup** | No setup needed | Requires server |
| **Cost** | Free for public repos | Self-hosted (your costs) |
| **Maintenance** | Zero maintenance | Requires updates |
| **Integration** | Native GitHub integration | Requires plugins |
| **Best For** | Small-medium projects, demos | Enterprise, complex pipelines |

---

**Last Updated:** 2025-10-30  
**Maintained By:** QA Team
