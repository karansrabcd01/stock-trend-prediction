"""
API routes for stock trend prediction
"""
import logging
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse

from app.models.schemas import InsightsResponse, HealthResponse, ErrorResponse
from app.models.model_manager import model_manager
from app.services.image_processor import image_processor
from app.services.numeric_processor import numeric_processor
from app.services.chatbot_service import chatbot_service

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/health", response_model=HealthResponse)
async def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy" if model_manager.is_ready() else "unhealthy",
        "message": "Stock Trend Prediction API is running",
        "models_loaded": model_manager.is_ready(),
        "available_endpoints": [
            "/api/predict/image",
            "/api/predict/numeric",
            "/health"
        ]
    }

@router.post("/predict/image", response_model=InsightsResponse)
async def predict_from_image(
    file: UploadFile = File(..., description="Stock chart image (candlestick/line chart)")
):
    """
    Predict stock trend from chart image
    
    - **file**: Upload a stock chart image (JPG, PNG, BMP)
    - Returns comprehensive analysis with trend prediction, confidence, and recommendations
    """
    try:
        # Validate model is loaded
        if not model_manager.is_ready():
            raise HTTPException(
                status_code=503,
                detail="Models not loaded. Please try again later."
            )
        
        # Read file content
        file_content = await file.read()
        
        # Validate image
        if not image_processor.validate_image(file_content):
            raise HTTPException(
                status_code=400,
                detail="Invalid image file. Please upload a valid image (JPG, PNG, BMP)."
            )
        
        # Preprocess image
        image_array = image_processor.preprocess_image(file_content)
        
        # Make prediction
        trend, confidence, probabilities = model_manager.predict_from_image(image_array)
        
        # Generate insights
        insights = chatbot_service.generate_insights(
            trend=trend,
            confidence=confidence,
            probabilities=probabilities,
            prediction_type="image"
        )
        
        logger.info(f"Image prediction successful: {trend} ({confidence*100:.2f}%)")
        return insights
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Image prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )

@router.post("/predict/numeric", response_model=InsightsResponse)
async def predict_from_numeric(
    file: UploadFile = File(..., description="CSV file with stock data (close, high, low, volume)")
):
    """
    Predict stock trend from numeric data (CSV)
    
    - **file**: Upload a CSV file with columns: close, high, low, volume
    - Returns comprehensive analysis with trend prediction, confidence, and recommendations
    """
    try:
        # Validate model is loaded
        if not model_manager.is_ready():
            raise HTTPException(
                status_code=503,
                detail="Models not loaded. Please try again later."
            )
        
        # Read file content
        file_content = await file.read()
        
        # Validate CSV
        if not numeric_processor.validate_csv(file_content):
            raise HTTPException(
                status_code=400,
                detail="Invalid CSV file. Please ensure it contains required columns: close, high, low, volume"
            )
        
        # Preprocess CSV
        features_array, df = numeric_processor.preprocess_csv(file_content)
        
        # Calculate risk metrics
        risk_metrics = numeric_processor.calculate_risk_metrics(df)
        
        # Make prediction
        trend, confidence, probabilities = model_manager.predict_from_numeric(features_array)
        
        # Generate insights
        insights = chatbot_service.generate_insights(
            trend=trend,
            confidence=confidence,
            probabilities=probabilities,
            risk_metrics=risk_metrics,
            prediction_type="numeric"
        )
        
        logger.info(f"Numeric prediction successful: {trend} ({confidence*100:.2f}%)")
        return insights
        
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Numeric prediction error: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail=f"Prediction failed: {str(e)}"
        )
