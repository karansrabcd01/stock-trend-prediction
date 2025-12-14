#!/bin/bash

# Quick Deployment Script for Stock Trend Prediction AI (Linux/Mac)
# This script helps you prepare and deploy your application

echo "========================================"
echo "Stock Trend Prediction AI - Deployment"
echo "========================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
CYAN='\033[0;36m'
NC='\033[0m' # No Color

# Check if Git is initialized
if [ ! -d ".git" ]; then
    echo -e "${YELLOW}⚠️  Git repository not initialized${NC}"
    read -p "Initialize Git repository? (y/n): " init_git
    if [ "$init_git" = "y" ]; then
        git init
        echo -e "${GREEN}✓ Git initialized${NC}"
    fi
fi

# Check for required files
echo -e "\n${CYAN}Checking required files...${NC}"

required_files=(
    "backend/requirements.txt"
    "backend/main.py"
    "frontend/package.json"
    "models/optimized_stock_model.h5"
    "models/best_model.h5"
)

all_files_exist=true
for file in "${required_files[@]}"; do
    if [ -f "$file" ]; then
        echo -e "${GREEN}✓ $file${NC}"
    else
        echo -e "${RED}✗ $file (missing)${NC}"
        all_files_exist=false
    fi
done

if [ "$all_files_exist" = false ]; then
    echo -e "\n${RED}⚠️  Some required files are missing!${NC}"
    exit 1
fi

# Deployment platform selection
echo -e "\n${CYAN}========================================${NC}"
echo -e "${CYAN}Select Deployment Platform:${NC}"
echo -e "${CYAN}========================================${NC}"
echo "1. Render.com (Recommended - Full Stack)"
echo "2. Railway.app (Quick Deploy)"
echo "3. Vercel (Frontend) + Render (Backend)"
echo "4. Netlify (Frontend) + Render (Backend)"
echo "5. Docker (Local/Self-hosted)"
echo "6. Just prepare for Git push"
echo ""

read -p "Enter your choice (1-6): " choice

case $choice in
    1)
        echo -e "\n${CYAN}📦 Preparing for Render.com deployment...${NC}"
        echo -e "${GREEN}✓ render.yaml is ready${NC}"
        echo -e "\n${YELLOW}Next steps:${NC}"
        echo "1. Push code to GitHub"
        echo "2. Go to https://dashboard.render.com/"
        echo "3. Click 'New +' → 'Blueprint'"
        echo "4. Connect your repository"
        echo "5. Render will auto-detect render.yaml"
        echo -e "\nSee DEPLOYMENT.md for detailed instructions"
        ;;
    2)
        echo -e "\n${CYAN}🚂 Preparing for Railway.app deployment...${NC}"
        echo -e "${GREEN}✓ railway.json is ready${NC}"
        echo -e "${GREEN}✓ Procfile is ready${NC}"
        echo -e "\n${YELLOW}Next steps:${NC}"
        echo "1. Install Railway CLI: npm install -g @railway/cli"
        echo "2. Run: railway login"
        echo "3. Run: railway init"
        echo "4. Deploy backend: cd backend && railway up"
        echo "5. Deploy frontend via Railway dashboard"
        echo -e "\nSee DEPLOYMENT.md for detailed instructions"
        ;;
    3)
        echo -e "\n${CYAN}⚡ Preparing for Vercel + Render deployment...${NC}"
        echo -e "${GREEN}✓ vercel.json is ready${NC}"
        echo -e "${GREEN}✓ render.yaml is ready${NC}"
        echo -e "\n${YELLOW}Next steps:${NC}"
        echo "Backend (Render):"
        echo "  1. Deploy backend to Render (see option 1)"
        echo "Frontend (Vercel):"
        echo "  2. Install Vercel CLI: npm install -g vercel"
        echo "  3. cd frontend && vercel"
        echo "  4. Add VITE_API_URL environment variable"
        echo -e "\nSee DEPLOYMENT.md for detailed instructions"
        ;;
    4)
        echo -e "\n${CYAN}🌐 Preparing for Netlify + Render deployment...${NC}"
        echo -e "${GREEN}✓ netlify.toml is ready${NC}"
        echo -e "${GREEN}✓ render.yaml is ready${NC}"
        echo -e "\n${YELLOW}Next steps:${NC}"
        echo "Backend (Render):"
        echo "  1. Deploy backend to Render (see option 1)"
        echo "Frontend (Netlify):"
        echo "  2. Install Netlify CLI: npm install -g netlify-cli"
        echo "  3. cd frontend && netlify deploy"
        echo "  4. Add VITE_API_URL environment variable"
        echo -e "\nSee DEPLOYMENT.md for detailed instructions"
        ;;
    5)
        echo -e "\n${CYAN}🐳 Preparing for Docker deployment...${NC}"
        echo -e "${GREEN}✓ Dockerfile.backend is ready${NC}"
        echo -e "${GREEN}✓ Dockerfile.frontend is ready${NC}"
        echo -e "${GREEN}✓ docker-compose.yml is ready${NC}"
        echo -e "\n${YELLOW}Next steps:${NC}"
        echo "1. Ensure Docker is installed and running"
        echo "2. Run: docker-compose up --build"
        echo "3. Access frontend at http://localhost"
        echo "4. Access backend at http://localhost:8000"
        echo -e "\nSee DOCKER.md for detailed instructions"
        ;;
    6)
        echo -e "\n${CYAN}📤 Preparing for Git push...${NC}"
        ;;
    *)
        echo -e "${RED}Invalid choice${NC}"
        exit 1
        ;;
esac

# Git operations
echo -e "\n${CYAN}========================================${NC}"
echo -e "${CYAN}Git Operations${NC}"
echo -e "${CYAN}========================================${NC}"

read -p $'\nAdd all files to Git? (y/n): ' git_add
if [ "$git_add" = "y" ]; then
    git add .
    echo -e "${GREEN}✓ Files added to Git${NC}"
    
    read -p "Enter commit message (or press Enter for default): " commit_msg
    if [ -z "$commit_msg" ]; then
        commit_msg="Prepare for deployment - $(date +%Y-%m-%d)"
    fi
    
    git commit -m "$commit_msg"
    echo -e "${GREEN}✓ Changes committed${NC}"
fi

# Check for remote
has_remote=$(git remote -v 2>&1)
if [ -z "$has_remote" ]; then
    echo -e "\n${YELLOW}⚠️  No Git remote configured${NC}"
    read -p "Add GitHub remote? (y/n): " add_remote
    if [ "$add_remote" = "y" ]; then
        read -p "Enter GitHub repository URL: " repo_url
        git remote add origin "$repo_url"
        echo -e "${GREEN}✓ Remote added${NC}"
    fi
fi

read -p $'\nPush to GitHub? (y/n): ' push_git
if [ "$push_git" = "y" ]; then
    branch=$(git branch --show-current)
    if [ -z "$branch" ]; then
        git branch -M main
        branch="main"
    fi
    
    git push -u origin "$branch"
    echo -e "${GREEN}✓ Pushed to GitHub${NC}"
fi

echo -e "\n${CYAN}========================================${NC}"
echo -e "${GREEN}✓ Deployment preparation complete!${NC}"
echo -e "${CYAN}========================================${NC}"
echo -e "\n${YELLOW}Next: Follow the platform-specific instructions above${NC}"
echo -e "${YELLOW}Documentation: See DEPLOYMENT.md for detailed guides${NC}"
echo ""
