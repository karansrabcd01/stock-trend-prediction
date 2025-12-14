import React, { useState, useEffect } from 'react';
import { BarChart3, Sparkles, Activity } from 'lucide-react';
import FileUpload from './components/FileUpload';
import PredictionResults from './components/PredictionResults';
import { stockPredictionAPI } from './services/api';
import './styles/index.css';
import './App.css';

function App() {
    const [predictionType, setPredictionType] = useState('image');
    const [selectedFile, setSelectedFile] = useState(null);
    const [isLoading, setIsLoading] = useState(false);
    const [results, setResults] = useState(null);
    const [error, setError] = useState(null);
    const [apiStatus, setApiStatus] = useState('checking');

    useEffect(() => {
        checkAPIHealth();
    }, []);

    const checkAPIHealth = async () => {
        try {
            await stockPredictionAPI.healthCheck();
            setApiStatus('healthy');
        } catch (err) {
            setApiStatus('unhealthy');
            console.error('API health check failed:', err);
        }
    };

    const handlePredictionTypeChange = (type) => {
        setPredictionType(type);
        setSelectedFile(null);
        setResults(null);
        setError(null);
    };

    const handleFileSelect = (file) => {
        setSelectedFile(file);
        setError(null);
    };

    const handlePredict = async () => {
        if (!selectedFile) {
            setError('Please select a file first');
            return;
        }

        setIsLoading(true);
        setError(null);
        setResults(null);

        try {
            let response;

            if (predictionType === 'image') {
                response = await stockPredictionAPI.predictFromImage(selectedFile);
            } else {
                response = await stockPredictionAPI.predictFromNumeric(selectedFile);
            }

            setResults(response);
        } catch (err) {
            console.error('Prediction error:', err);
            setError(
                err.response?.data?.detail ||
                err.message ||
                'Failed to get prediction. Please try again.'
            );
        } finally {
            setIsLoading(false);
        }
    };

    return (
        <div className="app">
            {/* Header */}
            <header className="app-header">
                <div className="container">
                    <div className="header-content">
                        <div className="logo">
                            <BarChart3 size={40} />
                            <h1>Stock Trend AI</h1>
                        </div>
                        <div className={`api-status status-${apiStatus}`}>
                            <Activity size={16} />
                            <span>{apiStatus === 'healthy' ? 'API Online' : 'API Offline'}</span>
                        </div>
                    </div>
                    <p className="tagline">
                        <Sparkles size={20} />
                        Advanced AI-Powered Stock Trend Prediction
                    </p>
                </div>
            </header>

            {/* Main Content */}
            <main className="main-content">
                <div className="container">
                    {/* Prediction Type Selector */}
                    <div className="type-selector glass-card">
                        <h2>Choose Prediction Method</h2>
                        <div className="type-buttons">
                            <button
                                className={`type-btn ${predictionType === 'image' ? 'active' : ''}`}
                                onClick={() => handlePredictionTypeChange('image')}
                                disabled={isLoading}
                            >
                                <BarChart3 size={24} />
                                <div>
                                    <h3>Chart Image</h3>
                                    <p>Upload stock chart screenshot</p>
                                </div>
                            </button>
                            <button
                                className={`type-btn ${predictionType === 'numeric' ? 'active' : ''}`}
                                onClick={() => handlePredictionTypeChange('numeric')}
                                disabled={isLoading}
                            >
                                <Activity size={24} />
                                <div>
                                    <h3>Numeric Data</h3>
                                    <p>Upload CSV with stock data</p>
                                </div>
                            </button>
                        </div>
                    </div>

                    {/* File Upload */}
                    <div className="upload-section glass-card">
                        <FileUpload
                            onFileSelect={handleFileSelect}
                            predictionType={predictionType}
                            isLoading={isLoading}
                        />

                        {/* Predict Button */}
                        {selectedFile && (
                            <button
                                className="btn btn-primary predict-btn"
                                onClick={handlePredict}
                                disabled={isLoading}
                            >
                                {isLoading ? (
                                    <>
                                        <div className="loading-spinner" />
                                        <span>Analyzing...</span>
                                    </>
                                ) : (
                                    <>
                                        <Sparkles size={20} />
                                        <span>Predict Trend</span>
                                    </>
                                )}
                            </button>
                        )}

                        {/* Error Message */}
                        {error && (
                            <div className="error-message fade-in">
                                <p>{error}</p>
                            </div>
                        )}
                    </div>

                    {/* Results */}
                    {results && <PredictionResults results={results} />}
                </div>
            </main>

            {/* Footer */}
            <footer className="app-footer">
                <div className="container">
                    <p>
                        Built with ❤️ using React, FastAPI, and TensorFlow
                    </p>
                    <p className="footer-disclaimer">
                        Educational purposes only • Not financial advice
                    </p>
                </div>
            </footer>
        </div>
    );
}

export default App;
