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
    
    # Determine model directory with multiple fallback options
    @staticmethod
    def _get_model_dir():
        """Get the models directory path with fallback options"""
        base_dir = Path(__file__).parent.parent
        
        # Option 1: Local development - models in parent directory
        local_models = base_dir.parent / "models"
        if local_models.exists():
            return local_models
        
        # Option 2: Render deployment - models in project root
        render_models_1 = Path("/opt/render/project/src/models")
        if render_models_1.exists():
            return render_models_1
        
        # Option 3: Alternative Render path
        render_models_2 = Path.cwd() / "models"
        if render_models_2.exists():
            return render_models_2
        
        # Option 4: Models in backend directory
        backend_models = base_dir / "models"
        if backend_models.exists():
            return backend_models
        
        # Default fallback
        return local_models
    
    MODEL_DIR: Path = _get_model_dir.__func__()
    
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
