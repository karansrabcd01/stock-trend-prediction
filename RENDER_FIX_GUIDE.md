# 🚀 Render Deployment Fix Guide

## Problem Summary

Your Stock Trend Prediction API was returning a **503 error** with the message:
```json
{
  "detail": "Models not loaded. Please try again later."
}
```

## Root Causes Identified

1. **OpenCV System Dependencies**: `opencv-python` requires GUI libraries not available on Render
2. **Model Path Mismatch**: The config wasn't correctly locating the models directory on Render
3. **Silent Model Loading Failures**: The code marked models as loaded even when they failed
4. **Working Directory Issues**: The start command was changing directories, breaking relative paths

## Fixes Applied

### 1. Updated Dependencies (`backend/requirements.txt`)
✅ **Changed**: `opencv-python` → `opencv-python-headless`
- Headless version doesn't require GUI system libraries
- Works perfectly on cloud platforms like Render

✅ **Pinned versions** for consistency:
```
tensorflow-cpu==2.15.0
numpy==1.24.3
pandas==2.0.3
Pillow==10.1.0
scikit-learn==1.3.2
opencv-python-headless==4.8.1.78
```

### 2. Enhanced Model Path Detection (`backend/app/config.py`)
✅ **Added intelligent path detection** with multiple fallbacks:
1. Local development: `../models`
2. Render deployment: `/opt/render/project/src/models`
3. Alternative: `{cwd}/models`
4. Backend directory: `backend/models`

### 3. Improved Model Loading (`backend/app/models/model_manager.py`)
✅ **Better error handling**:
- Each model loads in a try-catch block
- Detailed logging for debugging
- Only marks as "loaded" if at least the image model succeeds
- Prevents false positives

✅ **Enhanced logging**:
```python
logger.info(f"Model directory: {settings.MODEL_DIR}")
logger.info(f"Model directory exists: {Path(settings.MODEL_DIR).exists()}")
logger.info(f"✓ Models loaded successfully! ({models_loaded_count} models)")
```

### 4. Fixed Render Configuration (`render.yaml`)
✅ **Updated start command**:
```yaml
# Before: "cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT"
# After:  "uvicorn backend.main:app --host 0.0.0.0 --port $PORT"
```

✅ **Added PYTHONPATH**:
```yaml
- key: PYTHONPATH
  value: /opt/render/project/src
```

## Deployment Steps

### Option 1: Redeploy via Blueprint (Recommended)

1. **Commit the changes**:
   ```bash
   git add .
   git commit -m "fix: Resolve model loading issues for Render deployment"
   git push origin main
   ```

2. **Trigger redeploy on Render**:
   - Go to your Render dashboard
   - Find your `stock-trend-api` service
   - Click "Manual Deploy" → "Deploy latest commit"

3. **Monitor the logs**:
   - Watch for: `✓ Models loaded successfully!`
   - Check the model count in logs

### Option 2: Fresh Blueprint Deployment

1. **Delete the existing service** (if needed)
2. **Create new Blueprint**:
   - Go to Render Dashboard → "New" → "Blueprint"
   - Connect your repository
   - Select `render.yaml`
   - Click "Apply"

## Verification Steps

### 1. Check Health Endpoint
```bash
curl https://stock-trend-api.onrender.com/api/health
```

**Expected Response**:
```json
{
  "status": "healthy",
  "message": "Stock Trend Prediction API is running",
  "models_loaded": true,
  "available_endpoints": [
    "/api/predict/image",
    "/api/predict/numeric",
    "/health"
  ]
}
```

### 2. Test Image Prediction
```bash
curl -X POST "https://stock-trend-api.onrender.com/api/predict/image" \
  -H "accept: application/json" \
  -H "Content-Type: multipart/form-data" \
  -F "file=@your_chart.png"
```

### 3. Check Logs on Render
Look for these success messages:
```
✓ Loaded numeric model from /opt/render/project/src/models/optimized_stock_model.h5
✓ Loaded image model from /opt/render/project/src/models/best_model.h5
✓ Loaded scaler from /opt/render/project/src/models/optimized_scaler.pkl
✓ Loaded feature columns from /opt/render/project/src/models/feature_columns.pkl
✓ Models loaded successfully! (2 models)
```

## Troubleshooting

### If models still don't load:

1. **Check if models are in Git**:
   ```bash
   git ls-files models/
   ```
   Should show:
   - `models/best_model.h5`
   - `models/optimized_stock_model.h5`
   - `models/optimized_scaler.pkl`
   - `models/feature_columns.pkl`

2. **Verify model files aren't gitignored**:
   - Check `.gitignore` - lines 115-116 should be commented:
   ```
   # *.h5
   # *.pkl
   ```

3. **Check Render build logs**:
   - Look for "Installing dependencies from backend/requirements.txt"
   - Ensure TensorFlow installs successfully

4. **Increase Render instance size** (if needed):
   - Free tier might struggle with TensorFlow
   - Consider upgrading to Starter plan ($7/month)

### If you get memory errors:

The model files are ~7.5MB each. If Render's free tier runs out of memory:

1. **Use model compression**:
   ```python
   # In your training script
   model.save('model.h5', save_format='h5', compression='gzip')
   ```

2. **Consider model quantization**:
   - Reduce model size by 4x
   - Minimal accuracy loss

3. **Upgrade to paid tier**:
   - More memory and CPU
   - Better for production use

## Expected Behavior After Fix

✅ **Health endpoint returns**: `"models_loaded": true`  
✅ **Image predictions work** without 503 errors  
✅ **Logs show successful model loading**  
✅ **API responds within 2-3 seconds**  

## Frontend Update

Once the backend is working, update your frontend API URL:

**In `frontend/src/config.js`** (or wherever your API URL is):
```javascript
const API_URL = "https://stock-trend-api.onrender.com";
```

## Next Steps

1. ✅ Commit and push the fixes
2. ✅ Redeploy on Render
3. ✅ Verify health endpoint
4. ✅ Test with a sample image
5. ✅ Update frontend API URL
6. ✅ Deploy frontend to Netlify/Vercel

## Additional Resources

- [Render Docs - Python Apps](https://render.com/docs/deploy-fastapi)
- [TensorFlow on Render](https://render.com/docs/tensorflow)
- [Debugging Render Deployments](https://render.com/docs/troubleshooting-deploys)

---

**Need Help?** Check the Render logs for detailed error messages. The enhanced logging will show exactly where the model loading fails.
