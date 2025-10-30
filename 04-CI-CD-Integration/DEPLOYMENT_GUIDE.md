# 🚀 GitHub Deployment Guide

## 📋 Step-by-Step Guide to Deploy Your QA Portfolio

This guide will help you:
1. Initialize Git repository
2. Create GitHub repository
3. Push code to GitHub
4. Activate CI/CD workflows
5. Verify everything works

---

## ✅ Prerequisites Check

Before starting, ensure you have:
- [x] Git installed (`git --version`)
- [x] GitHub account created
- [x] All test frameworks completed (Chapters 1-4)

---

## 🎯 Step 1: Initialize Git Repository

### Open PowerShell in project root folder

```powershell
# Navigate to project folder
cd C:\Users\howie\Dev\Projects\LLM_Test_Plan\QA-Portfolio

# Initialize Git
git init

# Check status
git status
```

**Expected Output:**
```
Initialized empty Git repository in .../QA-Portfolio/.git/
```

---

## 📝 Step 2: Create .gitignore File

Create a `.gitignore` file to exclude unnecessary files:

```powershell
# Create .gitignore
@"
# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
env/
venv/
ENV/
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Testing
.pytest_cache/
.coverage
htmlcov/
.tox/
*.log

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Test Reports (keep in repo for demo)
# Uncomment if you don't want to commit reports
# reports/
# test-reports/
# performance-reports/

# Screenshots
screenshots/
"@ | Out-File -FilePath .gitignore -Encoding UTF8
```

---

## 📦 Step 3: Stage and Commit Files

```powershell
# Add all files to staging
git add .

# Check what will be committed
git status

# Create initial commit
git commit -m "Initial commit: Complete QA Portfolio with CI/CD"
```

**Expected Output:**
```
[main (root-commit) abc1234] Initial commit: Complete QA Portfolio with CI/CD
 XX files changed, XXXX insertions(+)
 create mode 100644 .github/workflows/api-tests.yml
 ...
```

---

## 🌐 Step 4: Create GitHub Repository

### Option A: Using GitHub Website (Recommended for Beginners)

1. **Go to GitHub**: https://github.com
2. **Click** "New" button (top right) or "+" icon
3. **Repository name**: `QA-Profolio` (or `QA-Portfolio`)
4. **Description**: "Comprehensive QA Automation Portfolio - API, Web, Performance Testing with CI/CD"
5. **Visibility**: 
   - ✅ **Public** (Recommended for portfolio - Free GitHub Actions)
   - Or **Private** (2,000 minutes/month GitHub Actions)
6. **DO NOT** initialize with README, .gitignore, or license
7. **Click** "Create repository"

### Option B: Using GitHub CLI (Advanced)

```powershell
# Install GitHub CLI if not already installed
# Download from: https://cli.github.com/

# Login to GitHub
gh auth login

# Create repository
gh repo create QA-Profolio --public --description "QA Automation Portfolio"
```

---

## 🔗 Step 5: Connect Local Repository to GitHub

After creating the repository on GitHub, you'll see a screen with commands. Use these:

```powershell
# Add GitHub as remote origin
git remote add origin https://github.com/howie0721/QA-Profolio.git

# Verify remote is added
git remote -v

# Push code to GitHub
git branch -M main
git push -u origin main
```

**If you need to authenticate:**
- Windows will prompt for GitHub credentials
- Use your GitHub username and **Personal Access Token** (not password)

### Creating Personal Access Token (PAT):
1. GitHub → Settings → Developer settings
2. Personal access tokens → Tokens (classic)
3. Generate new token → Select `repo` scope
4. Copy token (you won't see it again!)
5. Use token as password when pushing

---

## ✨ Step 6: Verify GitHub Actions Activated

### Check GitHub Actions:

1. **Go to your repository** on GitHub
2. **Click "Actions" tab**
3. **You should see:**
   - API Tests workflow
   - Web Automation Tests workflow
   - Performance Tests workflow
   - Full Test Suite workflow

### First Run:

GitHub Actions will **automatically run** on your first push! 🎉

**Wait 2-5 minutes**, then:
- Check if workflows appear
- Click on a workflow to see progress
- Green checkmark = Success ✅
- Red X = Failed (check logs) ❌

---

## 🎮 Step 7: Trigger Manual Test Run

Let's test the workflows manually:

1. **Go to Actions tab**
2. **Select "API Tests" workflow**
3. **Click "Run workflow" button**
4. **Select branch**: main
5. **Click green "Run workflow"**

**Wait 2-3 minutes** and see the results!

---

## 📊 Step 8: View Test Results

### Download Test Reports:

1. Click on completed workflow run
2. Scroll to "Artifacts" section
3. Download:
   - `api-test-report`
   - `web-test-report`
   - `performance-test-report`

### Open HTML Reports:

```powershell
# Extract ZIP files
# Open .html files in browser
```

---

## 🎯 Step 9: Add Status Badges to README

Add these badges to show off your passing tests!

Edit your `README.md` and add at the top:

```markdown
# 🎯 QA Portfolio

![API Tests](https://github.com/howie0721/QA-Profolio/workflows/API%20Tests/badge.svg)
![Web Tests](https://github.com/howie0721/QA-Profolio/workflows/Web%20Automation%20Tests/badge.svg)
![Performance Tests](https://github.com/howie0721/QA-Profolio/workflows/Performance%20Tests/badge.svg)

> Complete QA Automation Portfolio demonstrating API, Web, and Performance Testing with CI/CD
```

**Commit and push:**
```powershell
git add README.md
git commit -m "Add CI/CD status badges"
git push origin main
```

---

## 🐛 Troubleshooting

### Issue: Push rejected

**Error:**
```
! [rejected]        main -> main (fetch first)
```

**Solution:**
```powershell
git pull origin main --allow-unrelated-histories
git push origin main
```

### Issue: Authentication failed

**Solution:**
1. Use Personal Access Token instead of password
2. Or configure SSH key

**With PAT:**
```powershell
# Windows Credential Manager will save it
git push origin main
# Enter username: howie0721
# Enter password: <paste your PAT>
```

### Issue: Workflows not appearing

**Check:**
1. Files are in `.github/workflows/` (with dot!)
2. YAML syntax is correct
3. Repository is not private (or has Actions enabled)
4. Wait 1-2 minutes after push

**Force trigger:**
```powershell
# Make a small change
echo "# Test" >> README.md
git add README.md
git commit -m "Trigger workflows"
git push origin main
```

### Issue: Tests failing on GitHub but passing locally

**Common causes:**
1. Different Python version
2. Windows vs Linux differences
3. Missing dependencies

**Check workflow logs:**
1. Actions → Failed workflow → Click on red X
2. Read error messages
3. Fix and push again

---

## 📈 Verification Checklist

After completing all steps, verify:

- [ ] ✅ Repository exists on GitHub
- [ ] ✅ All files are pushed
- [ ] ✅ GitHub Actions tab is visible
- [ ] ✅ At least one workflow has run
- [ ] ✅ Workflows show green checkmarks
- [ ] ✅ Can download test report artifacts
- [ ] ✅ Status badges show "passing"

---

## 🎤 For Interview Demo

### What to Say:

**Show GitHub Repository:**
```
"This is my QA Portfolio hosted on GitHub. I've set up 
automated testing using GitHub Actions."
```

**Show Actions Tab:**
```
"Every time I push code, these workflows run automatically:
- API tests
- Web automation tests
- Performance tests

You can see all green checkmarks, meaning all tests passed."
```

**Trigger Manual Run:**
```
"I can also run tests manually. Let me show you..."
[Click Run workflow]
"In 2-3 minutes, we'll see the results."
```

**Show Test Reports:**
```
"Here are the detailed test reports. I can download them
and show you exactly what was tested and the results."
```

### Impressive Points:

✅ "CI/CD ensures code quality automatically"  
✅ "Tests run on every push - catches bugs early"  
✅ "Free to run on GitHub for public repos"  
✅ "Easy to maintain and scale"  
✅ "Shows DevOps and automation skills"

---

## 🚀 Next Steps

After deployment:

1. **Verify all workflows pass** ✅
2. **Add status badges to README** ✅
3. **Test manual workflow triggers** ✅
4. **Download and review test reports** ✅
5. **Move to Chapter 5: Docker** →

---

## 📞 Need Help?

If you encounter issues:

1. **Check workflow logs** in GitHub Actions
2. **Verify YAML syntax** using online validators
3. **Read error messages** carefully
4. **Google the error** - likely others had same issue
5. **Check GitHub Actions documentation**

---

## 🎓 What You've Accomplished

By completing this:

✅ Set up professional Git workflow  
✅ Deployed code to GitHub  
✅ Configured CI/CD pipelines  
✅ Automated all tests  
✅ Created a live demo portfolio  
✅ Demonstrated DevOps skills  

**Congratulations!** 🎉 You now have a professional QA portfolio with automated testing!

---

**Last Updated:** 2025-10-30  
**Author:** QA Team  
**Status:** Ready for Interview Demo 🚀
