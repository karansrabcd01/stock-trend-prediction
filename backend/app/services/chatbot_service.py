"""
Intelligent chatbot service for stock trend insights and recommendations
"""
import logging
from typing import Dict, List
import numpy as np

from app.config import settings

logger = logging.getLogger(__name__)

class ChatbotService:
    """Generates intelligent insights and recommendations"""
    
    @staticmethod
    def generate_insights(
        trend: str,
        confidence: float,
        probabilities: np.ndarray,
        risk_metrics: Dict = None,
        prediction_type: str = "image"
    ) -> Dict:
        """
        Generate comprehensive insights and recommendations
        
        Args:
            trend: Predicted trend (UP/DOWN/SIDEWAYS)
            confidence: Confidence score
            probabilities: Class probabilities
            risk_metrics: Optional risk metrics from numeric data
            prediction_type: Type of prediction (image/numeric)
            
        Returns:
            Dictionary containing insights, recommendations, and analysis
        """
        
        # Determine risk level
        risk_level = ChatbotService._calculate_risk_level(confidence, risk_metrics)
        
        # Generate market sentiment
        sentiment = ChatbotService._generate_sentiment(trend, confidence, probabilities)
        
        # Generate explanation
        explanation = ChatbotService._generate_explanation(trend, confidence, prediction_type)
        
        # Generate recommendations
        recommendations = ChatbotService._generate_recommendations(trend, confidence, risk_level)
        
        # Generate key insights
        key_insights = ChatbotService._generate_key_insights(trend, probabilities, risk_metrics)
        
        return {
            "prediction": {
                "trend": trend,
                "confidence": round(confidence * 100, 2),
                "probabilities": {
                    "DOWN": round(float(probabilities[0]) * 100, 2),
                    "SIDEWAYS": round(float(probabilities[1]) * 100, 2),
                    "UP": round(float(probabilities[2]) * 100, 2)
                }
            },
            "analysis": {
                "risk_level": risk_level,
                "sentiment": sentiment,
                "explanation": explanation
            },
            "insights": key_insights,
            "recommendations": recommendations,
            "disclaimer": "This analysis is for educational purposes only and should not be considered as financial advice. Always conduct your own research and consult with a qualified financial advisor before making investment decisions."
        }
    
    @staticmethod
    def _calculate_risk_level(confidence: float, risk_metrics: Dict = None) -> str:
        """Determine risk level based on confidence and metrics"""
        
        # Base risk on confidence
        if confidence >= 0.8:
            base_risk = "Low"
        elif confidence >= 0.6:
            base_risk = "Medium"
        else:
            base_risk = "High"
        
        # Adjust based on volatility if available
        if risk_metrics and 'volatility' in risk_metrics:
            volatility = risk_metrics['volatility']
            if volatility > 0.4:  # High volatility
                if base_risk == "Low":
                    base_risk = "Medium"
                elif base_risk == "Medium":
                    base_risk = "High"
        
        return base_risk
    
    @staticmethod
    def _generate_sentiment(trend: str, confidence: float, probabilities: np.ndarray) -> str:
        """Generate market sentiment description"""
        
        prob_dict = {
            "DOWN": float(probabilities[0]),
            "SIDEWAYS": float(probabilities[1]),
            "UP": float(probabilities[2])
        }
        
        # Check if probabilities are close (uncertain market)
        max_prob = max(prob_dict.values())
        second_max = sorted(prob_dict.values())[-2]
        
        if max_prob - second_max < 0.15:
            return "Mixed - Market showing uncertainty with competing signals"
        
        if trend == "UP":
            if confidence >= 0.8:
                return "Strongly Bullish - Clear upward momentum detected"
            elif confidence >= 0.6:
                return "Moderately Bullish - Positive trend with some caution"
            else:
                return "Cautiously Bullish - Weak upward signals"
        
        elif trend == "DOWN":
            if confidence >= 0.8:
                return "Strongly Bearish - Clear downward pressure detected"
            elif confidence >= 0.6:
                return "Moderately Bearish - Negative trend with some uncertainty"
            else:
                return "Cautiously Bearish - Weak downward signals"
        
        else:  # SIDEWAYS
            if confidence >= 0.7:
                return "Neutral - Strong consolidation pattern"
            else:
                return "Uncertain - No clear directional bias"
    
    @staticmethod
    def _generate_explanation(trend: str, confidence: float, prediction_type: str) -> str:
        """Generate human-readable explanation"""
        
        source = "chart pattern analysis" if prediction_type == "image" else "technical indicators and historical data"
        
        explanations = {
            "UP": f"Based on {source}, the model predicts an upward trend with {confidence*100:.1f}% confidence. "
                  f"This suggests potential bullish momentum in the near term.",
            
            "DOWN": f"Based on {source}, the model predicts a downward trend with {confidence*100:.1f}% confidence. "
                    f"This indicates potential bearish pressure in the near term.",
            
            "SIDEWAYS": f"Based on {source}, the model predicts sideways movement with {confidence*100:.1f}% confidence. "
                        f"This suggests the stock may consolidate or trade in a range."
        }
        
        return explanations.get(trend, "Unable to generate explanation")
    
    @staticmethod
    def _generate_recommendations(trend: str, confidence: float, risk_level: str) -> List[str]:
        """Generate actionable recommendations"""
        
        recommendations = []
        
        # Confidence-based recommendations
        if confidence < 0.6:
            recommendations.append("⚠️ Low confidence prediction - Wait for clearer signals before taking action")
            recommendations.append("📊 Monitor the stock closely for confirmation of the trend")
        
        # Trend-based recommendations
        if trend == "UP":
            if confidence >= 0.7:
                recommendations.append("✅ Consider this as a potential buying opportunity (with proper risk management)")
                recommendations.append("📈 Set stop-loss orders to protect against sudden reversals")
            else:
                recommendations.append("⏳ Wait for stronger confirmation before entering positions")
        
        elif trend == "DOWN":
            if confidence >= 0.7:
                recommendations.append("⚠️ Exercise caution - Consider reducing exposure or avoiding new positions")
                recommendations.append("🛡️ If holding, consider setting tight stop-losses")
            else:
                recommendations.append("👀 Monitor for potential reversal signals")
        
        else:  # SIDEWAYS
            recommendations.append("📊 Range-bound trading strategy may be appropriate")
            recommendations.append("⏳ Wait for a clear breakout before taking directional positions")
        
        # Risk-based recommendations
        if risk_level == "High":
            recommendations.append("🚨 High risk detected - Use smaller position sizes")
            recommendations.append("💡 Consider diversifying to manage risk")
        
        # General recommendations
        recommendations.append("📚 Always perform your own due diligence")
        recommendations.append("💼 Never invest more than you can afford to lose")
        
        return recommendations
    
    @staticmethod
    def _generate_key_insights(trend: str, probabilities: np.ndarray, risk_metrics: Dict = None) -> List[str]:
        """Generate key insights from the analysis"""
        
        insights = []
        
        # Probability insights
        prob_dict = {
            "DOWN": float(probabilities[0]),
            "SIDEWAYS": float(probabilities[1]),
            "UP": float(probabilities[2])
        }
        
        sorted_probs = sorted(prob_dict.items(), key=lambda x: x[1], reverse=True)
        
        insights.append(f"Primary prediction: {sorted_probs[0][0]} ({sorted_probs[0][1]*100:.1f}% probability)")
        insights.append(f"Alternative scenario: {sorted_probs[1][0]} ({sorted_probs[1][1]*100:.1f}% probability)")
        
        # Confidence insight
        max_prob = sorted_probs[0][1]
        if max_prob >= 0.8:
            insights.append("Model shows high conviction in this prediction")
        elif max_prob < 0.5:
            insights.append("Model shows low conviction - market may be at an inflection point")
        
        # Risk metrics insights
        if risk_metrics:
            if 'volatility' in risk_metrics:
                vol = risk_metrics['volatility']
                if vol > 0.3:
                    insights.append(f"High volatility detected ({vol*100:.1f}%) - expect larger price swings")
                elif vol < 0.15:
                    insights.append(f"Low volatility ({vol*100:.1f}%) - relatively stable price action")
            
            if 'max_drawdown' in risk_metrics:
                dd = risk_metrics['max_drawdown']
                if dd < -0.2:
                    insights.append(f"Significant drawdown observed ({dd*100:.1f}%) - recovery potential exists")
        
        return insights

chatbot_service = ChatbotService()
