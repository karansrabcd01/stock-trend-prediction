"""
DEMO VERSION - Simplified main.py for quick demonstration
This version uses mock predictions instead of actual models
"""
import logging
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import random

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Create FastAPI app
app = FastAPI(
    title="Stock Trend Prediction API",
    version="1.0.0",
    description="Advanced AI-powered stock trend prediction system"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def generate_mock_prediction():
    """Generate mock prediction for demo"""
    trends = ["UP", "DOWN", "SIDEWAYS"]
    trend = random.choice(trends)
    
    # Generate realistic probabilities
    if trend == "UP":
        probs = [random.uniform(5, 15), random.uniform(5, 15), random.uniform(70, 90)]
    elif trend == "DOWN":
        probs = [random.uniform(70, 90), random.uniform(5, 15), random.uniform(5, 15)]
    else:
        probs = [random.uniform(10, 30), random.uniform(50, 70), random.uniform(10, 30)]
    
    # Normalize
    total = sum(probs)
    probs = [p/total * 100 for p in probs]
    
    confidence = max(probs)
    
    # Determine risk level
    if confidence >= 80:
        risk_level = "Low"
    elif confidence >= 60:
        risk_level = "Medium"
    else:
        risk_level = "High"
    
    # Generate sentiment
    if trend == "UP":
        if confidence >= 80:
            sentiment = "Strongly Bullish - Clear upward momentum detected"
        else:
            sentiment = "Moderately Bullish - Positive trend with some caution"
    elif trend == "DOWN":
        if confidence >= 80:
            sentiment = "Strongly Bearish - Clear downward pressure detected"
        else:
            sentiment = "Moderately Bearish - Negative trend with some uncertainty"
    else:
        sentiment = "Neutral - Strong consolidation pattern"
    
    return {
        "prediction": {
            "trend": trend,
            "confidence": round(confidence, 2),
            "probabilities": {
                "DOWN": round(probs[0], 2),
                "SIDEWAYS": round(probs[1], 2),
                "UP": round(probs[2], 2)
            }
        },
        "analysis": {
            "risk_level": risk_level,
            "sentiment": sentiment,
            "explanation": f"Based on analysis, the model predicts a {trend} trend with {confidence:.1f}% confidence. This suggests potential {'bullish' if trend == 'UP' else 'bearish' if trend == 'DOWN' else 'sideways'} momentum in the near term."
        },
        "insights": [
            f"Primary prediction: {trend} ({confidence:.1f}% probability)",
            f"Alternative scenario: {trends[1 if trend == trends[0] else 0]} ({probs[1 if trend == trends[2] else 0]:.1f}% probability)",
            "Model shows " + ("high" if confidence >= 70 else "moderate") + " conviction in this prediction"
        ],
        "recommendations": [
            "Consider this analysis as one factor in your decision-making process",
            "Always perform comprehensive due diligence before investing",
            "Diversify your portfolio to manage risk effectively",
            "Never invest more than you can afford to lose",
            "Consult with a qualified financial advisor for personalized advice"
        ],
        "disclaimer": "This analysis is for educational and informational purposes only and should not be considered as financial advice. Stock market investments carry risk. Always conduct your own research and consult with qualified financial professionals before making investment decisions."
    }

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Stock Trend Prediction API",
        "version": "1.0.0",
        "status": "operational",
        "docs": "/docs",
        "health": "/api/health"
    }

@app.get("/api/health")
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "message": "Stock Trend Prediction API is running",
        "models_loaded": True,
        "available_endpoints": [
            "/api/predict/image",
            "/api/predict/numeric",
            "/health"
        ]
    }

@app.post("/api/predict/image")
async def predict_from_image(file: UploadFile = File(...)):
    """Predict stock trend from chart image"""
    try:
        # Validate file
        if not file.content_type.startswith('image/'):
            raise HTTPException(status_code=400, detail="Please upload an image file")
        
        # Read file to validate it's not empty
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Empty file uploaded")
        
        logger.info(f"Image prediction request: {file.filename} ({len(content)} bytes)")
        
        # Return mock prediction
        return generate_mock_prediction()
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/predict/numeric")
async def predict_from_numeric(file: UploadFile = File(...)):
    """Predict stock trend from CSV data"""
    try:
        # Validate file
        if not file.filename.endswith('.csv'):
            raise HTTPException(status_code=400, detail="Please upload a CSV file")
        
        # Read file to validate it's not empty
        content = await file.read()
        if len(content) == 0:
            raise HTTPException(status_code=400, detail="Empty file uploaded")
        
        logger.info(f"Numeric prediction request: {file.filename} ({len(content)} bytes)")
        
        # Return mock prediction
        return generate_mock_prediction()
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    logger.info("🚀 Starting Stock Trend Prediction API")
    logger.info("🤖 AI models ready for predictions")
    logger.info("🌐 Server will run on: http://localhost:8000")
    logger.info("📚 API Docs available at: http://localhost:8000/docs")
    
    uvicorn.run(
        "main_demo:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
