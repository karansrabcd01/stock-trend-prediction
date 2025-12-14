# 🚀 Deployment Guide - Stock Trend Prediction AI

This guide covers deploying your Stock Trend Prediction AI application to various free hosting platforms.

---

## 📋 Table of Contents

- [Prerequisites](#prerequisites)
- [Platform Comparison](#platform-comparison)
- [Option 1: Render.com (Recommended)](#option-1-rendercom-recommended)
- [Option 2: Railway.app](#option-2-railwayapp)
- [Option 3: Vercel + Render](#option-3-vercel--render)
- [Option 4: Netlify + Render](#option-4-netlify--render)
- [Environment Variables](#environment-variables)
- [Post-Deployment](#post-deployment)
- [Troubleshooting](#troubleshooting)

---

## 🎯 Prerequisites

Before deploying, ensure you have:

- ✅ GitHub account (to push your code)
- ✅ Git installed locally
- ✅ Account on your chosen platform (Render/Railway/Vercel/Netlify)
- ✅ All dependencies listed in `requirements.txt` and `package.json`

---

## 🔍 Platform Comparison

| Platform | Backend | Frontend | Free Tier | Best For |
|----------|---------|----------|-----------|----------|
| **Render** | ✅ | ✅ | 750 hrs/month | Full-stack apps |
| **Railway** | ✅ | ✅ | $5 credit/month | Quick deployment |
| **Vercel** | ⚠️ Serverless | ✅ | Unlimited | Frontend + API |
| **Netlify** | ❌ | ✅ | Unlimited | Frontend only |

**Recommendation**: Use **Render.com** for the easiest full-stack deployment.

---

## 🎨 Option 1: Render.com (Recommended)

### **Why Render?**
- ✅ Free tier with 750 hours/month
- ✅ Supports both backend and frontend
- ✅ Auto-deploy from GitHub
- ✅ Built-in SSL certificates
- ✅ Easy environment variable management

### **Step-by-Step Deployment**

#### **1. Prepare Your Repository**

```bash
# Initialize git (if not already done)
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit - ready for deployment"

# Create GitHub repository and push
git remote add origin https://github.com/YOUR_USERNAME/stock-trend-prediction.git
git branch -M main
git push -u origin main
```

#### **2. Deploy Backend API**

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub repository
4. Configure:
   - **Name**: `stock-trend-api`
   - **Region**: Choose closest to you
   - **Branch**: `main`
   - **Root Directory**: `backend`
   - **Runtime**: `Python 3`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Plan**: `Free`

5. Add Environment Variables:
   ```
   PYTHON_VERSION=3.11.0
   ENVIRONMENT=production
   CORS_ORIGINS=*
   ```

6. Click **"Create Web Service"**
7. Wait for deployment (5-10 minutes)
8. **Copy your API URL**: `https://stock-trend-api-xxxx.onrender.com`

#### **3. Deploy Frontend**

1. Click **"New +"** → **"Static Site"**
2. Connect same GitHub repository
3. Configure:
   - **Name**: `stock-trend-frontend`
   - **Branch**: `main`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Publish Directory**: `dist`

4. Add Environment Variable:
   ```
   VITE_API_URL=https://stock-trend-api-xxxx.onrender.com/api
   ```
   *(Replace with your actual backend URL from step 2)*

5. Click **"Create Static Site"**
6. Wait for deployment (3-5 minutes)
7. **Your app is live!** 🎉

#### **4. Using render.yaml (Alternative)**

For automated deployment, use the included `render.yaml`:

1. Go to Render Dashboard
2. Click **"New +"** → **"Blueprint"**
3. Connect your repository
4. Render will auto-detect `render.yaml`
5. Update environment variables
6. Click **"Apply"**

---

## 🚂 Option 2: Railway.app

### **Step-by-Step Deployment**

#### **1. Deploy Backend**

```bash
# Install Railway CLI
npm install -g @railway/cli

# Login
railway login

# Initialize project
railway init

# Deploy backend
cd backend
railway up

# Get backend URL
railway domain
```

#### **2. Deploy Frontend**

1. Go to [Railway Dashboard](https://railway.app/dashboard)
2. Create new project
3. Deploy from GitHub
4. Select `frontend` directory
5. Add environment variable:
   ```
   VITE_API_URL=https://your-backend.railway.app/api
   ```

---

## ⚡ Option 3: Vercel + Render

**Best for**: Serverless backend with optimized frontend

### **Deploy Backend on Render**
Follow [Option 1 - Step 2](#2-deploy-backend-api)

### **Deploy Frontend on Vercel**

```bash
# Install Vercel CLI
npm install -g vercel

# Navigate to frontend
cd frontend

# Deploy
vercel

# Follow prompts:
# - Set up and deploy? Yes
# - Which scope? Your account
# - Link to existing project? No
# - Project name? stock-trend-frontend
# - Directory? ./
# - Override settings? No

# Add environment variable
vercel env add VITE_API_URL production
# Enter: https://your-backend.onrender.com/api

# Redeploy with env vars
vercel --prod
```

---

## 🌐 Option 4: Netlify + Render

**Best for**: Static frontend with separate backend

### **Deploy Backend on Render**
Follow [Option 1 - Step 2](#2-deploy-backend-api)

### **Deploy Frontend on Netlify**

#### **Method 1: Netlify CLI**

```bash
# Install Netlify CLI
npm install -g netlify-cli

# Navigate to frontend
cd frontend

# Build the app
npm run build

# Deploy
netlify deploy

# Follow prompts, then deploy to production:
netlify deploy --prod
```

#### **Method 2: Netlify Dashboard**

1. Go to [Netlify Dashboard](https://app.netlify.com/)
2. Click **"Add new site"** → **"Import an existing project"**
3. Connect GitHub repository
4. Configure:
   - **Base directory**: `frontend`
   - **Build command**: `npm run build`
   - **Publish directory**: `frontend/dist`
5. Add environment variable:
   ```
   VITE_API_URL=https://your-backend.onrender.com/api
   ```
6. Click **"Deploy site"**

---

## 🔐 Environment Variables

### **Backend Environment Variables**

Create these on your hosting platform:

```env
# Required
PYTHON_VERSION=3.11.0
ENVIRONMENT=production

# CORS (adjust based on your frontend URL)
CORS_ORIGINS=https://your-frontend-url.com,https://www.your-frontend-url.com

# Optional
LOG_LEVEL=INFO
MAX_UPLOAD_SIZE=10485760
```

### **Frontend Environment Variables**

```env
# Required - Your backend API URL
VITE_API_URL=https://your-backend-url.com/api

# Optional
VITE_APP_NAME=Stock Trend Prediction AI
VITE_APP_VERSION=1.0.0
```

---

## 📝 Post-Deployment Checklist

After deployment, verify:

- [ ] Backend health check: `https://your-backend-url.com/api/health`
- [ ] API documentation: `https://your-backend-url.com/docs`
- [ ] Frontend loads correctly
- [ ] Image upload works
- [ ] CSV upload works
- [ ] Predictions are generated
- [ ] No CORS errors in browser console
- [ ] SSL certificate is active (https://)

### **Test Your Deployment**

```bash
# Test backend health
curl https://your-backend-url.com/api/health

# Expected response:
# {"status":"healthy","models_loaded":true}

# Test image prediction (with a test image)
curl -X POST https://your-backend-url.com/api/predict/image \
  -F "file=@test_chart.png"
```

---

## 🐛 Troubleshooting

### **Common Issues**

#### **1. CORS Errors**

**Problem**: Frontend can't connect to backend

**Solution**:
```python
# In backend/.env or platform environment variables
CORS_ORIGINS=https://your-frontend-url.com
```

#### **2. Models Not Loading**

**Problem**: `Models not found` error

**Solution**:
- Ensure `models/` directory is committed to Git
- Check file sizes (some platforms have limits)
- Verify paths in `backend/main.py`

#### **3. Build Failures**

**Problem**: Deployment fails during build

**Solution**:
```bash
# Check Python version
PYTHON_VERSION=3.11.0

# Verify requirements.txt has all dependencies
# Test locally first:
pip install -r backend/requirements.txt
```

#### **4. Frontend Environment Variables Not Working**

**Problem**: API calls go to wrong URL

**Solution**:
- Rebuild after adding env vars
- Check Vite requires `VITE_` prefix
- Verify in browser: `console.log(import.meta.env.VITE_API_URL)`

#### **5. Port Issues**

**Problem**: App not starting on correct port

**Solution**:
```python
# Ensure your backend uses $PORT from environment
import os
port = int(os.getenv("PORT", 8000))
```

#### **6. File Upload Size Limits**

**Problem**: Large files fail to upload

**Solution**:
- Render: 10MB limit on free tier
- Vercel: 4.5MB for serverless functions
- Railway: 100MB limit

---

## 🔄 Continuous Deployment

### **Auto-Deploy on Git Push**

All platforms support automatic deployment:

1. **Render**: Auto-deploys on push to `main` branch
2. **Railway**: Auto-deploys on push
3. **Vercel**: Auto-deploys on push
4. **Netlify**: Auto-deploys on push

### **Manual Deployment**

```bash
# Render
git push origin main  # Auto-deploys

# Railway
railway up

# Vercel
vercel --prod

# Netlify
netlify deploy --prod
```

---

## 📊 Monitoring

### **Check Deployment Status**

- **Render**: Dashboard → Your Service → Logs
- **Railway**: Dashboard → Your Project → Deployments
- **Vercel**: Dashboard → Your Project → Deployments
- **Netlify**: Dashboard → Your Site → Deploys

### **View Logs**

```bash
# Railway
railway logs

# Vercel
vercel logs

# Netlify
netlify logs
```

---

## 💡 Best Practices

1. **Use Environment Variables**: Never hardcode URLs or secrets
2. **Enable HTTPS**: All platforms provide free SSL
3. **Set Up Monitoring**: Use platform analytics
4. **Regular Updates**: Keep dependencies updated
5. **Backup Models**: Store models in cloud storage for large files
6. **Use CDN**: For faster asset delivery
7. **Optimize Images**: Compress before deployment
8. **Error Tracking**: Implement Sentry or similar

---

## 🎯 Recommended Setup

For the best free deployment:

1. **Backend**: Render.com (750 hrs/month free)
2. **Frontend**: Netlify (unlimited free)
3. **Models**: Git LFS or cloud storage
4. **Monitoring**: Render built-in logs
5. **Domain**: Netlify custom domain (free)

---

## 📞 Support

If you encounter issues:

1. Check platform status pages
2. Review deployment logs
3. Test locally first
4. Verify environment variables
5. Check GitHub Issues

---

## 🎉 Success!

Once deployed, your app will be accessible at:

- **Frontend**: `https://your-app.netlify.app`
- **Backend**: `https://your-api.onrender.com`
- **API Docs**: `https://your-api.onrender.com/docs`

Share your deployed app with the world! 🚀

---

**Last Updated**: December 2024  
**Version**: 1.0.0
