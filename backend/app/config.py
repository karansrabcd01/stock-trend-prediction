"""
Configuration settings for the Stock Trend Prediction API
"""
import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

class Settings:
    """Application settings"""
    
    # API Settings
    APP_NAME: str = "Stock Trend Prediction API"
    VERSION: str = "1.0.0"
    HOST: str = os.getenv("HOST", "0.0.0.0")
    PORT: int = int(os.getenv("PORT", 8000))
    
    # CORS Settings
    CORS_ORIGINS: list = os.getenv(
        "CORS_ORIGINS", 
        "http://localhost:5173,http://localhost:3000"
    ).split(",")
    
    # Model Paths
    BASE_DIR: Path = Path(__file__).parent.parent
    MODEL_DIR: Path = BASE_DIR.parent / "models"
    
    MODEL_PATH: str = str(MODEL_DIR / "optimized_stock_model.h5")
    SCALER_PATH: str = str(MODEL_DIR / "optimized_scaler.pkl")
    FEATURE_COLUMNS_PATH: str = str(MODEL_DIR / "feature_columns.pkl")
    IMAGE_MODEL_PATH: str = str(MODEL_DIR / "best_model.h5")
    
    # Prediction Settings
    TREND_CLASSES: list = ["DOWN", "SIDEWAYS", "UP"]
    CONFIDENCE_THRESHOLD: float = 0.6
    
    # Image Processing Settings
    IMAGE_SIZE: tuple = (224, 224)
    MAX_IMAGE_SIZE_MB: int = 10
    ALLOWED_IMAGE_EXTENSIONS: set = {".jpg", ".jpeg", ".png", ".bmp"}
    
    # CSV Processing Settings
    MAX_CSV_SIZE_MB: int = 5
    REQUIRED_CSV_COLUMNS: list = ["close", "high", "low", "volume"]
    
    class Config:
        case_sensitive = True

settings = Settings()
