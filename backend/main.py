"""
Main FastAPI application for Stock Trend Prediction
"""
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.config import settings
from app.models.model_manager import model_manager
from app.routes import predictions

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan events for startup and shutdown"""
    # Startup
    logger.info("Starting Stock Trend Prediction API...")
    logger.info(f"Loading models from: {settings.MODEL_DIR}")
    
    # Load models
    success = model_manager.load_models()
    if not success:
        logger.error("Failed to load models!")
    else:
        logger.info("✓ All models loaded successfully!")
    
    yield
    
    # Shutdown
    logger.info("Shutting down Stock Trend Prediction API...")

# Create FastAPI app
app = FastAPI(
    title=settings.APP_NAME,
    version=settings.VERSION,
    description="""
    🚀 **Advanced Stock Trend Prediction API**
    
    This API provides intelligent stock trend predictions using deep learning models.
    
    ## Features
    
    * 📊 **Image-based Prediction**: Upload stock chart images for trend analysis
    * 📈 **Numeric Data Prediction**: Upload CSV files with stock data
    * 🤖 **AI-Powered Insights**: Get comprehensive analysis and recommendations
    * ⚡ **Fast & Scalable**: Built with FastAPI for high performance
    
    ## Prediction Classes
    
    * **UP**: Bullish trend expected
    * **DOWN**: Bearish trend expected
    * **SIDEWAYS**: Consolidation/range-bound movement expected
    
    ## How to Use
    
    1. Choose your input type (image or numeric data)
    2. Upload your file
    3. Receive instant predictions with detailed insights
    
    ⚠️ **Disclaimer**: This is for educational purposes only. Not financial advice.
    """,
    lifespan=lifespan,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    predictions.router,
    prefix="/api",
    tags=["Predictions"]
)

@app.get("/")
async def root():
    """Root endpoint"""
    return {
        "message": "Welcome to Stock Trend Prediction API",
        "version": settings.VERSION,
        "docs": "/docs",
        "health": "/api/health"
    }

@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    logger.error(f"Unhandled exception: {str(exc)}")
    return JSONResponse(
        status_code=500,
        content={
            "error": "Internal server error",
            "detail": str(exc)
        }
    )

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host=settings.HOST,
        port=settings.PORT,
        reload=True
    )
