import React from 'react';
import { TrendingUp, TrendingDown, Minus, AlertTriangle, Lightbulb, Info } from 'lucide-react';
import './PredictionResults.css';

const PredictionResults = ({ results }) => {
    if (!results) return null;

    const { prediction, analysis, insights, recommendations, disclaimer } = results;

    const getTrendIcon = (trend) => {
        switch (trend) {
            case 'UP':
                return <TrendingUp size={32} />;
            case 'DOWN':
                return <TrendingDown size={32} />;
            case 'SIDEWAYS':
                return <Minus size={32} />;
            default:
                return null;
        }
    };

    const getTrendClass = (trend) => {
        return trend.toLowerCase();
    };

    return (
        <div className="prediction-results fade-in">
            {/* Main Prediction Card */}
            <div className={`prediction-card glass-card trend-${getTrendClass(prediction.trend)}`}>
                <div className="trend-header">
                    <div className="trend-icon">
                        {getTrendIcon(prediction.trend)}
                    </div>
                    <div className="trend-info">
                        <h2>Predicted Trend</h2>
                        <div className={`trend-badge badge-${getTrendClass(prediction.trend)}`}>
                            {prediction.trend}
                        </div>
                    </div>
                </div>

                <div className="confidence-section">
                    <div className="confidence-label">
                        <span>Confidence Score</span>
                        <span className="confidence-value">{prediction.confidence}%</span>
                    </div>
                    <div className="confidence-bar">
                        <div
                            className="confidence-fill"
                            style={{ width: `${prediction.confidence}%` }}
                        />
                    </div>
                </div>

                <div className="probabilities">
                    <h3>Probability Distribution</h3>
                    <div className="prob-grid">
                        {Object.entries(prediction.probabilities).map(([trend, prob]) => (
                            <div key={trend} className="prob-item">
                                <div className="prob-header">
                                    <span className={`prob-label badge-${trend.toLowerCase()}`}>
                                        {trend}
                                    </span>
                                    <span className="prob-value">{prob}%</span>
                                </div>
                                <div className="prob-bar">
                                    <div
                                        className={`prob-fill prob-fill-${trend.toLowerCase()}`}
                                        style={{ width: `${prob}%` }}
                                    />
                                </div>
                            </div>
                        ))}
                    </div>
                </div>
            </div>

            {/* Analysis Card */}
            <div className="analysis-card glass-card">
                <h3>
                    <Info size={20} />
                    Market Analysis
                </h3>

                <div className="analysis-grid">
                    <div className="analysis-item">
                        <span className="analysis-label">Risk Level</span>
                        <span className={`risk-badge risk-${analysis.risk_level.toLowerCase()}`}>
                            {analysis.risk_level}
                        </span>
                    </div>

                    <div className="analysis-item">
                        <span className="analysis-label">Market Sentiment</span>
                        <span className="sentiment-text">{analysis.sentiment}</span>
                    </div>
                </div>

                <div className="explanation">
                    <p>{analysis.explanation}</p>
                </div>
            </div>

            {/* Insights Card */}
            <div className="insights-card glass-card">
                <h3>
                    <Lightbulb size={20} />
                    Key Insights
                </h3>
                <ul className="insights-list">
                    {insights.map((insight, index) => (
                        <li key={index} className="insight-item">
                            <span className="insight-bullet">•</span>
                            <span>{insight}</span>
                        </li>
                    ))}
                </ul>
            </div>

            {/* Recommendations Card */}
            <div className="recommendations-card glass-card">
                <h3>
                    <AlertTriangle size={20} />
                    Recommendations
                </h3>
                <ul className="recommendations-list">
                    {recommendations.map((rec, index) => {
                        // Determine icon based on content
                        let icon = '•';
                        if (rec.toLowerCase().includes('demo')) icon = '⚠️';
                        else if (rec.toLowerCase().includes('tensorflow') || rec.toLowerCase().includes('real')) icon = '📊';
                        else if (rec.toLowerCase().includes('diligence') || rec.toLowerCase().includes('research')) icon = '📚';
                        else if (rec.toLowerCase().includes('invest') || rec.toLowerCase().includes('afford')) icon = '💼';
                        else if (rec.toLowerCase().includes('consider') || rec.toLowerCase().includes('opportunity')) icon = '✅';
                        else if (rec.toLowerCase().includes('caution') || rec.toLowerCase().includes('avoid')) icon = '⚠️';
                        else if (rec.toLowerCase().includes('stop-loss') || rec.toLowerCase().includes('protect')) icon = '📈';
                        else if (rec.toLowerCase().includes('wait') || rec.toLowerCase().includes('monitor')) icon = '👀';
                        else if (rec.toLowerCase().includes('risk')) icon = '🚨';

                        return (
                            <li key={index} className="recommendation-item">
                                <span className="rec-icon">{icon}</span>
                                <span>{rec}</span>
                            </li>
                        );
                    })}
                </ul>
            </div>

            {/* Disclaimer */}
            <div className="disclaimer glass-card">
                <p>{disclaimer}</p>
            </div>
        </div>
    );
};

export default PredictionResults;
