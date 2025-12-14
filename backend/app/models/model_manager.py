"""
Model loader and manager for stock trend prediction models
"""
import pickle
import logging
from pathlib import Path
from typing import Optional, Tuple
import tensorflow as tf
from tensorflow import keras
import numpy as np

from app.config import settings

logger = logging.getLogger(__name__)

class ModelManager:
    """Manages loading and caching of ML models"""
    
    def __init__(self):
        self.numeric_model: Optional[keras.Model] = None
        self.image_model: Optional[keras.Model] = None
        self.scaler: Optional[object] = None
        self.feature_columns: Optional[list] = None
        self._models_loaded = False
    
    def load_models(self) -> bool:
        """Load all required models and preprocessors"""
        try:
            logger.info("Loading models...")
            logger.info(f"Model directory: {settings.MODEL_DIR}")
            logger.info(f"Model directory exists: {Path(settings.MODEL_DIR).exists()}")
            
            models_loaded_count = 0
            
            # Load numeric prediction model
            if Path(settings.MODEL_PATH).exists():
                try:
                    self.numeric_model = keras.models.load_model(settings.MODEL_PATH)
                    logger.info(f"✓ Loaded numeric model from {settings.MODEL_PATH}")
                    models_loaded_count += 1
                except Exception as e:
                    logger.error(f"Failed to load numeric model: {str(e)}")
            else:
                logger.warning(f"Numeric model not found at {settings.MODEL_PATH}")
            
            # Load image prediction model
            if Path(settings.IMAGE_MODEL_PATH).exists():
                try:
                    self.image_model = keras.models.load_model(settings.IMAGE_MODEL_PATH)
                    logger.info(f"✓ Loaded image model from {settings.IMAGE_MODEL_PATH}")
                    models_loaded_count += 1
                except Exception as e:
                    logger.error(f"Failed to load image model: {str(e)}")
            else:
                logger.warning(f"Image model not found at {settings.IMAGE_MODEL_PATH}")
            
            # Load scaler
            if Path(settings.SCALER_PATH).exists():
                try:
                    with open(settings.SCALER_PATH, 'rb') as f:
                        self.scaler = pickle.load(f)
                    logger.info(f"✓ Loaded scaler from {settings.SCALER_PATH}")
                except Exception as e:
                    logger.error(f"Failed to load scaler: {str(e)}")
            else:
                logger.warning(f"Scaler not found at {settings.SCALER_PATH}")
            
            # Load feature columns
            if Path(settings.FEATURE_COLUMNS_PATH).exists():
                try:
                    with open(settings.FEATURE_COLUMNS_PATH, 'rb') as f:
                        self.feature_columns = pickle.load(f)
                    logger.info(f"✓ Loaded feature columns from {settings.FEATURE_COLUMNS_PATH}")
                except Exception as e:
                    logger.error(f"Failed to load feature columns: {str(e)}")
            else:
                logger.warning(f"Feature columns not found at {settings.FEATURE_COLUMNS_PATH}")
            
            # Only mark as loaded if at least the image model is available
            if self.image_model is not None:
                self._models_loaded = True
                logger.info(f"✓ Models loaded successfully! ({models_loaded_count} models)")
                return True
            else:
                logger.error("❌ Critical: No models could be loaded!")
                self._models_loaded = False
                return False
            
        except Exception as e:
            logger.error(f"Error loading models: {str(e)}")
            self._models_loaded = False
            return False
    
    def predict_from_numeric(self, features: np.ndarray) -> Tuple[str, float, np.ndarray]:
        """
        Make prediction from numeric features
        
        Args:
            features: Preprocessed feature array
            
        Returns:
            Tuple of (predicted_trend, confidence, probabilities)
        """
        if not self.numeric_model:
            raise ValueError("Numeric model not loaded")
        
        # Make prediction
        probabilities = self.numeric_model.predict(features, verbose=0)[0]
        predicted_class = int(np.argmax(probabilities))
        confidence = float(probabilities[predicted_class])
        trend = settings.TREND_CLASSES[predicted_class]
        
        return trend, confidence, probabilities
    
    def predict_from_image(self, image_array: np.ndarray) -> Tuple[str, float, np.ndarray]:
        """
        Make prediction from image
        
        Args:
            image_array: Preprocessed image array
            
        Returns:
            Tuple of (predicted_trend, confidence, probabilities)
        """
        if not self.image_model:
            raise ValueError("Image model not loaded")
        
        # Make prediction
        probabilities = self.image_model.predict(image_array, verbose=0)[0]
        predicted_class = int(np.argmax(probabilities))
        confidence = float(probabilities[predicted_class])
        trend = settings.TREND_CLASSES[predicted_class]
        
        return trend, confidence, probabilities
    
    def is_ready(self) -> bool:
        """Check if models are loaded and ready"""
        return self._models_loaded

# Global model manager instance
model_manager = ModelManager()
