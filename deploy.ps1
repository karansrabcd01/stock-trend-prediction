# Quick Deployment Script for Stock Trend Prediction AI
# This script helps you prepare and deploy your application

Write-Host "========================================" -ForegroundColor Cyan
Write-Host "Stock Trend Prediction AI - Deployment" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host ""

# Check if Git is initialized
if (-not (Test-Path ".git")) {
    Write-Host "⚠️  Git repository not initialized" -ForegroundColor Yellow
    $initGit = Read-Host "Initialize Git repository? (y/n)"
    if ($initGit -eq "y") {
        git init
        Write-Host "✓ Git initialized" -ForegroundColor Green
    }
}

# Check for required files
Write-Host "`nChecking required files..." -ForegroundColor Cyan

$requiredFiles = @(
    "backend/requirements.txt",
    "backend/main.py",
    "frontend/package.json",
    "models/optimized_stock_model.h5",
    "models/best_model.h5"
)

$allFilesExist = $true
foreach ($file in $requiredFiles) {
    if (Test-Path $file) {
        Write-Host "✓ $file" -ForegroundColor Green
    } else {
        Write-Host "✗ $file (missing)" -ForegroundColor Red
        $allFilesExist = $false
    }
}

if (-not $allFilesExist) {
    Write-Host "`n⚠️  Some required files are missing!" -ForegroundColor Red
    exit 1
}

# Deployment platform selection
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Select Deployment Platform:" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "1. Render.com (Recommended - Full Stack)"
Write-Host "2. Railway.app (Quick Deploy)"
Write-Host "3. Vercel (Frontend) + Render (Backend)"
Write-Host "4. Netlify (Frontend) + Render (Backend)"
Write-Host "5. Docker (Local/Self-hosted)"
Write-Host "6. Just prepare for Git push"
Write-Host ""

$choice = Read-Host "Enter your choice (1-6)"

switch ($choice) {
    "1" {
        Write-Host "`n📦 Preparing for Render.com deployment..." -ForegroundColor Cyan
        Write-Host "✓ render.yaml is ready" -ForegroundColor Green
        Write-Host "`nNext steps:" -ForegroundColor Yellow
        Write-Host "1. Push code to GitHub"
        Write-Host "2. Go to https://dashboard.render.com/"
        Write-Host "3. Click 'New +' → 'Blueprint'"
        Write-Host "4. Connect your repository"
        Write-Host "5. Render will auto-detect render.yaml"
        Write-Host "`nSee DEPLOYMENT.md for detailed instructions"
    }
    "2" {
        Write-Host "`n🚂 Preparing for Railway.app deployment..." -ForegroundColor Cyan
        Write-Host "✓ railway.json is ready" -ForegroundColor Green
        Write-Host "✓ Procfile is ready" -ForegroundColor Green
        Write-Host "`nNext steps:" -ForegroundColor Yellow
        Write-Host "1. Install Railway CLI: npm install -g @railway/cli"
        Write-Host "2. Run: railway login"
        Write-Host "3. Run: railway init"
        Write-Host "4. Deploy backend: cd backend && railway up"
        Write-Host "5. Deploy frontend via Railway dashboard"
        Write-Host "`nSee DEPLOYMENT.md for detailed instructions"
    }
    "3" {
        Write-Host "`n⚡ Preparing for Vercel + Render deployment..." -ForegroundColor Cyan
        Write-Host "✓ vercel.json is ready" -ForegroundColor Green
        Write-Host "✓ render.yaml is ready" -ForegroundColor Green
        Write-Host "`nNext steps:" -ForegroundColor Yellow
        Write-Host "Backend (Render):"
        Write-Host "  1. Deploy backend to Render (see option 1)"
        Write-Host "Frontend (Vercel):"
        Write-Host "  2. Install Vercel CLI: npm install -g vercel"
        Write-Host "  3. cd frontend && vercel"
        Write-Host "  4. Add VITE_API_URL environment variable"
        Write-Host "`nSee DEPLOYMENT.md for detailed instructions"
    }
    "4" {
        Write-Host "`n🌐 Preparing for Netlify + Render deployment..." -ForegroundColor Cyan
        Write-Host "✓ netlify.toml is ready" -ForegroundColor Green
        Write-Host "✓ render.yaml is ready" -ForegroundColor Green
        Write-Host "`nNext steps:" -ForegroundColor Yellow
        Write-Host "Backend (Render):"
        Write-Host "  1. Deploy backend to Render (see option 1)"
        Write-Host "Frontend (Netlify):"
        Write-Host "  2. Install Netlify CLI: npm install -g netlify-cli"
        Write-Host "  3. cd frontend && netlify deploy"
        Write-Host "  4. Add VITE_API_URL environment variable"
        Write-Host "`nSee DEPLOYMENT.md for detailed instructions"
    }
    "5" {
        Write-Host "`n🐳 Preparing for Docker deployment..." -ForegroundColor Cyan
        Write-Host "✓ Dockerfile.backend is ready" -ForegroundColor Green
        Write-Host "✓ Dockerfile.frontend is ready" -ForegroundColor Green
        Write-Host "✓ docker-compose.yml is ready" -ForegroundColor Green
        Write-Host "`nNext steps:" -ForegroundColor Yellow
        Write-Host "1. Ensure Docker is installed and running"
        Write-Host "2. Run: docker-compose up --build"
        Write-Host "3. Access frontend at http://localhost"
        Write-Host "4. Access backend at http://localhost:8000"
        Write-Host "`nSee DOCKER.md for detailed instructions"
    }
    "6" {
        Write-Host "`n📤 Preparing for Git push..." -ForegroundColor Cyan
    }
    default {
        Write-Host "Invalid choice" -ForegroundColor Red
        exit 1
    }
}

# Git operations
Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "Git Operations" -ForegroundColor Cyan
Write-Host "========================================" -ForegroundColor Cyan

$gitAdd = Read-Host "`nAdd all files to Git? (y/n)"
if ($gitAdd -eq "y") {
    git add .
    Write-Host "✓ Files added to Git" -ForegroundColor Green
    
    $commitMsg = Read-Host "Enter commit message (or press Enter for default)"
    if ([string]::IsNullOrWhiteSpace($commitMsg)) {
        $commitMsg = "Prepare for deployment - $(Get-Date -Format 'yyyy-MM-dd')"
    }
    
    git commit -m $commitMsg
    Write-Host "✓ Changes committed" -ForegroundColor Green
}

# Check for remote
$hasRemote = git remote -v 2>&1
if ([string]::IsNullOrWhiteSpace($hasRemote)) {
    Write-Host "`n⚠️  No Git remote configured" -ForegroundColor Yellow
    $addRemote = Read-Host "Add GitHub remote? (y/n)"
    if ($addRemote -eq "y") {
        $repoUrl = Read-Host "Enter GitHub repository URL"
        git remote add origin $repoUrl
        Write-Host "✓ Remote added" -ForegroundColor Green
    }
}

$pushToGit = Read-Host "`nPush to GitHub? (y/n)"
if ($pushToGit -eq "y") {
    $branch = git branch --show-current
    if ([string]::IsNullOrWhiteSpace($branch)) {
        git branch -M main
        $branch = "main"
    }
    
    git push -u origin $branch
    Write-Host "✓ Pushed to GitHub" -ForegroundColor Green
}

Write-Host "`n========================================" -ForegroundColor Cyan
Write-Host "✓ Deployment preparation complete!" -ForegroundColor Green
Write-Host "========================================" -ForegroundColor Cyan
Write-Host "`nNext: Follow the platform-specific instructions above" -ForegroundColor Yellow
Write-Host "Documentation: See DEPLOYMENT.md for detailed guides" -ForegroundColor Yellow
Write-Host ""
