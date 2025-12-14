"""
Image preprocessing service for stock chart analysis
"""
import io
import logging
from typing import Tuple
import numpy as np
from PIL import Image
import cv2

from app.config import settings

logger = logging.getLogger(__name__)

class ImageProcessor:
    """Handles image preprocessing for model input"""
    
    @staticmethod
    def validate_image(file_content: bytes) -> bool:
        """Validate image file"""
        try:
            # Check file size
            size_mb = len(file_content) / (1024 * 1024)
            if size_mb > settings.MAX_IMAGE_SIZE_MB:
                raise ValueError(f"Image size ({size_mb:.2f}MB) exceeds maximum allowed ({settings.MAX_IMAGE_SIZE_MB}MB)")
            
            # Try to open image
            Image.open(io.BytesIO(file_content))
            return True
            
        except Exception as e:
            logger.error(f"Image validation failed: {str(e)}")
            return False
    
    @staticmethod
    def preprocess_image(file_content: bytes) -> np.ndarray:
        """
        Preprocess image for model prediction
        
        Args:
            file_content: Raw image bytes
            
        Returns:
            Preprocessed image array ready for model input
        """
        try:
            # Load image
            image = Image.open(io.BytesIO(file_content))
            
            # Convert to RGB if necessary
            if image.mode != 'RGB':
                image = image.convert('RGB')
            
            # Resize to model input size
            image = image.resize(settings.IMAGE_SIZE)
            
            # Convert to numpy array
            img_array = np.array(image)
            
            # Normalize pixel values to [0, 1]
            img_array = img_array.astype('float32') / 255.0
            
            # Add batch dimension
            img_array = np.expand_dims(img_array, axis=0)
            
            logger.info(f"Image preprocessed successfully. Shape: {img_array.shape}")
            return img_array
            
        except Exception as e:
            logger.error(f"Image preprocessing failed: {str(e)}")
            raise ValueError(f"Failed to preprocess image: {str(e)}")
    
    @staticmethod
    def extract_features_from_image(file_content: bytes) -> dict:
        """
        Extract additional features from chart image (optional enhancement)
        
        Args:
            file_content: Raw image bytes
            
        Returns:
            Dictionary of extracted features
        """
        try:
            # Load image
            image = Image.open(io.BytesIO(file_content))
            img_array = np.array(image)
            
            # Convert to grayscale for analysis
            gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
            
            # Extract basic statistics
            features = {
                'mean_intensity': float(np.mean(gray)),
                'std_intensity': float(np.std(gray)),
                'min_intensity': float(np.min(gray)),
                'max_intensity': float(np.max(gray)),
                'image_shape': img_array.shape
            }
            
            return features
            
        except Exception as e:
            logger.warning(f"Feature extraction failed: {str(e)}")
            return {}

image_processor = ImageProcessor()
