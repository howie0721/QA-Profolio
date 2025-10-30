# Jenkins CI/CD Setup Guide

## 📋 Overview

This directory contains Jenkins Pipeline configuration for automating the QA Portfolio test suite.

---

## 🚀 Prerequisites

Before setting up Jenkins, ensure you have:

- ✅ Jenkins installed (2.400+)
- ✅ Required Jenkins plugins:
  - Pipeline
  - Git Plugin
  - HTML Publisher Plugin
  - JUnit Plugin
  - Blue Ocean (optional, for better UI)
- ✅ Python 3.12+ installed on Jenkins agent
- ✅ Git configured
- ✅ Chrome/Chromium browser (for Web tests)

---

## 📂 Files in This Directory

```
jenkins/
├── Jenkinsfile                    # Main pipeline configuration
├── README.md                      # This file
└── jenkins-job-config.xml         # Jenkins job XML configuration (optional)
```

---

## 🛠️ Setup Instructions

### Step 1: Create Jenkins Pipeline Job

1. **Open Jenkins Dashboard**
   - Navigate to: `http://localhost:8080` (or your Jenkins URL)

2. **Create New Item**
   - Click "New Item"
   - Enter name: `QA-Portfolio-Pipeline`
   - Select "Pipeline"
   - Click "OK"

### Step 2: Configure Pipeline

1. **General Settings**
   - ✅ Check "GitHub project" (if applicable)
   - Project URL: `https://github.com/howie0721/QA-Profolio`

2. **Build Triggers**
   - ✅ Check "Poll SCM"
   - Schedule: `H/5 * * * *` (every 5 minutes)
   - OR
   - ✅ Check "GitHub hook trigger for GITScm polling"

3. **Pipeline Configuration**
   - Definition: `Pipeline script from SCM`
   - SCM: `Git`
   - Repository URL: `https://github.com/howie0721/QA-Profolio.git`
   - Branch: `*/main`
   - Script Path: `04-CI-CD-Integration/jenkins/Jenkinsfile`

4. **Parameters**
   The pipeline automatically creates these parameters:
   - `TEST_SUITE`: Choose which tests to run (all/api/web/performance)
   - `SKIP_PERFORMANCE_TESTS`: Skip performance tests (boolean)

### Step 3: Configure Required Plugins

Install these Jenkins plugins:

```bash
# Using Jenkins CLI
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin pipeline-stage-view
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin htmlpublisher
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin junit
java -jar jenkins-cli.jar -s http://localhost:8080/ install-plugin git
```

Or install via Jenkins UI:
1. Manage Jenkins → Manage Plugins
2. Search and install:
   - Pipeline
   - HTML Publisher Plugin
   - JUnit Plugin
   - Git Plugin

### Step 4: Configure System

1. **Global Tool Configuration**
   - Manage Jenkins → Global Tool Configuration
   - Add Python installation (if not auto-detected)

2. **Security Settings**
   - Enable "HTML Publisher Plugin" to render HTML reports
   - Manage Jenkins → Configure Global Security
   - Find "Markup Formatter" and set to "Safe HTML"

---

## 🎮 Running the Pipeline

### Method 1: Manual Trigger

1. Go to your pipeline job
2. Click "Build with Parameters"
3. Select test suite and options
4. Click "Build"

### Method 2: Git Push Trigger

```powershell
# Make changes to your code
git add .
git commit -m "Update tests"
git push origin main

# Jenkins will automatically detect changes and run pipeline
```

### Method 3: Scheduled Run

Pipeline runs automatically based on cron schedule:
- Daily at 2 AM: `0 2 * * *`
- Poll SCM every 5 minutes: `H/5 * * * *`

---

## 📊 Pipeline Stages

The Jenkins pipeline consists of these stages:

```
1. Checkout           → Get code from Git repository
2. Setup Environment  → Install Python and dependencies
3. API Tests          → Run pytest API tests
4. Web UI Tests       → Run Selenium tests (headless)
5. Performance Tests  → Run Locust load tests
6. Generate Summary   → Create test report summary
```

---

## 📈 Viewing Test Reports

After pipeline execution, view reports:

1. **Test Results Tab**
   - Click on build number → "Test Results"
   - View JUnit test results

2. **HTML Reports**
   - API Test Report
   - Web Test Report
   - Performance Test Report

3. **Console Output**
   - Click build number → "Console Output"
   - View detailed logs

---

## 🔧 Customizing the Pipeline

### Add Email Notifications

Add to `post` section in Jenkinsfile:

```groovy
post {
    success {
        emailext (
            to: 'your.email@example.com',
            subject: "✅ Build ${env.BUILD_NUMBER} Passed",
            body: "All tests passed successfully!"
        )
    }
}
```

### Add Slack Notifications

```groovy
post {
    success {
        slackSend (
            color: 'good',
            message: "✅ Build ${env.BUILD_NUMBER} passed!"
        )
    }
}
```

### Change Test Timeout

```groovy
options {
    timeout(time: 1, unit: 'HOURS')
}
```

---

## 🐛 Troubleshooting

### Issue: Python not found

**Solution:**
```groovy
environment {
    PATH = "/usr/local/bin:$PATH"
}
```

### Issue: Chrome not available

**Solution:** Install Chrome on Jenkins agent
```bash
# For Ubuntu/Debian
sudo apt-get update
sudo apt-get install -y chromium-browser chromium-chromedriver
```

### Issue: HTML reports not rendering

**Solution:** Configure Content Security Policy
```bash
# In Jenkins startup script
-Dhudson.model.DirectoryBrowserSupport.CSP="sandbox allow-scripts; default-src 'self'; style-src 'self' 'unsafe-inline';"
```

---

## 📝 Jenkins Job Configuration (XML)

To backup or import Jenkins job configuration:

```powershell
# Export job configuration
curl -u admin:password http://localhost:8080/job/QA-Portfolio-Pipeline/config.xml > jenkins-job-config.xml

# Import job configuration
curl -X POST -u admin:password http://localhost:8080/createItem?name=QA-Portfolio-Pipeline --data-binary @jenkins-job-config.xml -H "Content-Type: text/xml"
```

---

## 🎯 Best Practices

1. **Use Declarative Pipeline**
   - Easier to read and maintain
   - Better error handling

2. **Parameterize Your Pipeline**
   - Make it flexible for different scenarios
   - Allow selective test execution

3. **Archive Artifacts**
   - Save test reports for historical analysis
   - Keep screenshots on failure

4. **Clean Workspace**
   - Always clean up after build
   - Prevents disk space issues

5. **Use Stages Wisely**
   - Break down into logical steps
   - Makes debugging easier

---

## 📚 Additional Resources

- [Jenkins Pipeline Documentation](https://www.jenkins.io/doc/book/pipeline/)
- [Jenkins Plugins Index](https://plugins.jenkins.io/)
- [Pipeline Syntax Reference](https://www.jenkins.io/doc/book/pipeline/syntax/)

---

**Last Updated:** 2025-10-30  
**Maintained By:** QA Team
