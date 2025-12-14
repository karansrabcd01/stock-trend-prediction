"""
Pydantic models for API request/response validation
"""
from typing import Dict, List, Optional
from pydantic import BaseModel, Field

class PredictionResponse(BaseModel):
    """Response model for predictions"""
    trend: str = Field(..., description="Predicted trend: UP, DOWN, or SIDEWAYS")
    confidence: float = Field(..., description="Confidence score (0-100)")
    probabilities: Dict[str, float] = Field(..., description="Probabilities for each class")

class AnalysisResponse(BaseModel):
    """Response model for analysis"""
    risk_level: str = Field(..., description="Risk level: Low, Medium, or High")
    sentiment: str = Field(..., description="Market sentiment description")
    explanation: str = Field(..., description="Human-readable explanation")

class InsightsResponse(BaseModel):
    """Complete response with insights"""
    prediction: PredictionResponse
    analysis: AnalysisResponse
    insights: List[str] = Field(..., description="Key insights from the analysis")
    recommendations: List[str] = Field(..., description="Actionable recommendations")
    disclaimer: str = Field(..., description="Legal disclaimer")

class HealthResponse(BaseModel):
    """Health check response"""
    status: str
    message: str
    models_loaded: bool
    available_endpoints: List[str]

class ErrorResponse(BaseModel):
    """Error response model"""
    error: str
    detail: Optional[str] = None
    status_code: int
