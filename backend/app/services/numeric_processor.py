"""
Numeric data preprocessing service for stock trend prediction
"""
import io
import logging
from typing import Dict, List, Tuple
import numpy as np
import pandas as pd

from app.config import settings
from app.models.model_manager import model_manager

logger = logging.getLogger(__name__)

class NumericProcessor:
    """Handles numeric data preprocessing for model input"""
    
    @staticmethod
    def validate_csv(file_content: bytes) -> bool:
        """Validate CSV file"""
        try:
            # Check file size
            size_mb = len(file_content) / (1024 * 1024)
            if size_mb > settings.MAX_CSV_SIZE_MB:
                raise ValueError(f"CSV size ({size_mb:.2f}MB) exceeds maximum allowed ({settings.MAX_CSV_SIZE_MB}MB)")
            
            # Try to read CSV
            df = pd.read_csv(io.BytesIO(file_content))
            
            # Check for required columns (case-insensitive)
            df.columns = df.columns.str.lower()
            missing_cols = set(settings.REQUIRED_CSV_COLUMNS) - set(df.columns)
            
            if missing_cols:
                raise ValueError(f"Missing required columns: {missing_cols}")
            
            return True
            
        except Exception as e:
            logger.error(f"CSV validation failed: {str(e)}")
            return False
    
    @staticmethod
    def preprocess_csv(file_content: bytes) -> Tuple[np.ndarray, pd.DataFrame]:
        """
        Preprocess CSV data for model prediction
        
        Args:
            file_content: Raw CSV bytes
            
        Returns:
            Tuple of (preprocessed_features, original_dataframe)
        """
        try:
            # Read CSV
            df = pd.read_csv(io.BytesIO(file_content))
            df.columns = df.columns.str.lower()
            
            # Calculate technical indicators
            df = NumericProcessor._calculate_features(df)
            
            # Prepare features for model
            if model_manager.feature_columns:
                # Use only the features the model was trained on
                available_features = [col for col in model_manager.feature_columns if col in df.columns]
                features_df = df[available_features].copy()
            else:
                # Use all numeric columns
                features_df = df.select_dtypes(include=[np.number]).copy()
            
            # Handle missing values
            features_df = features_df.fillna(features_df.mean())
            
            # Scale features
            if model_manager.scaler:
                features_scaled = model_manager.scaler.transform(features_df)
            else:
                features_scaled = features_df.values
            
            # Take the last row for prediction (most recent data)
            features_array = features_scaled[-1:].reshape(1, -1)
            
            logger.info(f"CSV preprocessed successfully. Shape: {features_array.shape}")
            return features_array, df
            
        except Exception as e:
            logger.error(f"CSV preprocessing failed: {str(e)}")
            raise ValueError(f"Failed to preprocess CSV: {str(e)}")
    
    @staticmethod
    def _calculate_features(df: pd.DataFrame) -> pd.DataFrame:
        """Calculate technical indicators and features"""
        try:
            # Price-based features
            if 'close' in df.columns:
                df['returns'] = df['close'].pct_change()
                df['log_returns'] = np.log(df['close'] / df['close'].shift(1))
                
                # Moving averages
                df['ma_5'] = df['close'].rolling(window=5).mean()
                df['ma_10'] = df['close'].rolling(window=10).mean()
                df['ma_20'] = df['close'].rolling(window=20).mean()
                
                # Volatility
                df['volatility_5'] = df['returns'].rolling(window=5).std()
                df['volatility_10'] = df['returns'].rolling(window=10).std()
            
            # High-Low range
            if 'high' in df.columns and 'low' in df.columns:
                df['hl_range'] = df['high'] - df['low']
                df['hl_pct'] = (df['high'] - df['low']) / df['close']
            
            # Volume features
            if 'volume' in df.columns:
                df['volume_ma_5'] = df['volume'].rolling(window=5).mean()
                df['volume_ratio'] = df['volume'] / df['volume_ma_5']
            
            # RSI (Relative Strength Index)
            if 'close' in df.columns:
                df['rsi'] = NumericProcessor._calculate_rsi(df['close'])
            
            return df
            
        except Exception as e:
            logger.warning(f"Feature calculation warning: {str(e)}")
            return df
    
    @staticmethod
    def _calculate_rsi(prices: pd.Series, period: int = 14) -> pd.Series:
        """Calculate Relative Strength Index"""
        delta = prices.diff()
        gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
        loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
        rs = gain / loss
        rsi = 100 - (100 / (1 + rs))
        return rsi
    
    @staticmethod
    def calculate_risk_metrics(df: pd.DataFrame) -> Dict[str, float]:
        """Calculate risk metrics from price data"""
        try:
            metrics = {}
            
            if 'close' in df.columns:
                returns = df['close'].pct_change().dropna()
                
                metrics['volatility'] = float(returns.std() * np.sqrt(252))  # Annualized
                metrics['sharpe_ratio'] = float(returns.mean() / returns.std() * np.sqrt(252)) if returns.std() > 0 else 0
                metrics['max_drawdown'] = float((df['close'] / df['close'].cummax() - 1).min())
                metrics['current_price'] = float(df['close'].iloc[-1])
                metrics['price_change_pct'] = float(returns.iloc[-1] * 100)
            
            return metrics
            
        except Exception as e:
            logger.warning(f"Risk metrics calculation failed: {str(e)}")
            return {}

numeric_processor = NumericProcessor()
