# 🚀 Stock Trend Prediction AI

<div align="center">

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.10+-blue)
![React](https://img.shields.io/badge/react-18.2-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-0.104-green)
![License](https://img.shields.io/badge/license-MIT-green)

**An advanced, production-ready full-stack AI application for intelligent stock trend prediction**

[Quick Start](#-quick-start) • [Features](#-features) • [API Usage](#-api-usage) • [Screenshots](#-screenshots)

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Quick Start](#-quick-start)
- [Project Structure](#-project-structure)
- [Running the Application](#-running-the-application)
- [Using the Application](#-using-the-application)
- [API Documentation](#-api-documentation)
- [Browser Exhibition](#-browser-exhibition)
- [Troubleshooting](#-troubleshooting)
- [Disclaimer](#-disclaimer)
- [License](#-license)

---

## 🎯 Overview

Stock Trend Prediction AI is a sophisticated full-stack application that leverages deep learning to predict stock market trends. The system provides intelligent insights, risk assessment, and actionable recommendations through an intuitive, modern web interface.

### **Key Capabilities**

- 📊 **Dual Input Modes**: Analyze stock charts (images) or numerical data (CSV)
- 🤖 **AI-Powered Predictions**: Deep learning models for trend classification
- 💡 **Intelligent Insights**: Context-aware recommendations and risk analysis
- 🎨 **Modern UI**: Beautiful, responsive interface with glassmorphism design
- ⚡ **Real-time Processing**: Fast predictions with optimized inference

---

## ✨ Features

### **Prediction Capabilities**

- ✅ **Image-Based Analysis**
  - Upload stock chart screenshots
  - CNN-based pattern recognition
  - Supports candlestick and line charts
  
- ✅ **Numeric Data Analysis**
  - CSV file upload
  - Technical indicator calculation (RSI, MA, volatility)
  - Time-series prediction

- ✅ **Trend Classification**
  - UP (Bullish)
  - DOWN (Bearish)
  - SIDEWAYS (Consolidation)

### **AI Features**

- 🎯 **Confidence Scoring**: Probability distribution for all classes
- 📊 **Risk Assessment**: Low/Medium/High risk levels
- 💬 **Market Sentiment**: Bullish/Bearish/Neutral analysis
- 💡 **Smart Recommendations**: Context-aware actionable advice
- 📈 **Technical Indicators**: Auto-calculated metrics

### **User Experience**

- 🎨 **Modern Design**: Glassmorphism with smooth animations
- 📱 **Responsive**: Works on desktop, tablet, and mobile
- 🖱️ **Drag & Drop**: Intuitive file upload
- ⚡ **Real-time Feedback**: Loading states and error handling
- 🎭 **Dark Theme**: Premium, eye-friendly interface

---

## 🛠️ Tech Stack

### **Backend**
- **Framework**: FastAPI 0.104
- **ML/AI**: TensorFlow 2.13, Keras
- **Data Processing**: Pandas, NumPy, scikit-learn
- **Image Processing**: Pillow, OpenCV
- **Server**: Uvicorn (ASGI)

### **Frontend**
- **Library**: React 18.2
- **Build Tool**: Vite 5.0
- **HTTP Client**: Axios
- **Animations**: Framer Motion
- **Icons**: Lucide React
- **Styling**: Custom CSS (Glassmorphism)

### **Models**
- **Image Model**: CNN for chart pattern recognition (7.5 MB)
- **Numeric Model**: DNN for time-series prediction (7.5 MB)
- **Preprocessing**: StandardScaler, feature engineering

---

## 🚀 Quick Start

### **Prerequisites**

- Python 3.10 or 3.11 (for TensorFlow support)
- Node.js 16+
- npm or yarn

### **Installation**

#### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/stock-trend-prediction.git
cd stock-trend-prediction
```

#### **2. Backend Setup**
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

#### **3. Frontend Setup**
```bash
cd frontend

# Install dependencies
npm install
```

---

## 📁 Project Structure

```
Stock-Trend-Prediction/
│
├── 📁 backend/                          # FastAPI Backend Application
│   ├── 📁 app/
│   │   ├── 📁 models/                   # Model management
│   │   ├── 📁 services/                 # Business logic
│   │   ├── 📁 routes/                   # API endpoints
│   │   └── config.py                    # Configuration
│   ├── main.py                          # Application entry point
│   ├── main_demo.py                     # Demo version
│   ├── requirements.txt                 # Python dependencies
│   └── .env                             # Environment variables
│
├── 📁 frontend/                         # React Frontend Application
│   ├── 📁 public/                       # Static assets
│   ├── 📁 src/
│   │   ├── 📁 components/               # React components
│   │   ├── 📁 services/                 # API integration
│   │   ├── 📁 styles/                   # CSS styles
│   │   ├── App.jsx                      # Main component
│   │   └── main.jsx                     # Entry point
│   ├── index.html                       # HTML template
│   ├── package.json                     # Node dependencies
│   └── vite.config.js                   # Vite configuration
│
├── 📁 models/                           # Trained ML Models
│   ├── optimized_stock_model.h5         # Numeric prediction model
│   ├── best_model.h5                    # Image prediction model
│   ├── optimized_scaler.pkl             # Feature scaler
│   └── feature_columns.pkl              # Feature definitions
│
├── 📁 notebooks/                        # Jupyter notebooks
│   └── Refine_Stock_trend.ipynb         # Model training
│
├── 📁 assets/                           # Images & sample data
│   ├── 📁 images/                       # Screenshots
│   └── 📁 sample_data/                  # Test data
│
├── README.md                            # This file
├── .gitignore                           # Git ignore rules
└── LICENSE                              # MIT License
```

---

## 🎮 Running the Application

### **Option 1: Using Two Terminals (Recommended)**

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate          # Windows
# source venv/bin/activate     # macOS/Linux
python main_demo.py            # or python main.py for production
```

**Terminal 2 - Frontend:**
```bash
cd frontend
npm run dev
```

### **Option 2: Using Startup Scripts (Windows)**
```bash
# Terminal 1 - Backend
cd backend
start_backend.bat

# Terminal 2 - Frontend
cd frontend
start_frontend.bat
```

### **Access the Application**

- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Docs**: http://localhost:8000/docs

---

## 🎨 Using the Application

### **Method 1: Image-Based Prediction**

1. Open http://localhost:5173 in your browser
2. Click on **"Chart Image"** button
3. Drag and drop or click to upload a stock chart image
4. Supported formats: JPG, PNG, BMP
5. Click **"Predict Trend"**
6. View comprehensive AI analysis with:
   - Trend prediction (UP/DOWN/SIDEWAYS)
   - Confidence score
   - Probability distribution
   - Risk assessment
   - Market sentiment
   - Actionable recommendations

### **Method 2: Numeric Data Prediction**

1. Click on **"Numeric Data"** button
2. Upload a CSV file with stock data
3. Required columns: `close`, `high`, `low`, `volume`
4. Optional columns: `date`, `open`
5. Click **"Predict Trend"**
6. View detailed insights with:
   - Trend prediction
   - Confidence metrics
   - Risk level (Low/Medium/High)
   - Technical indicators
   - Smart recommendations

### **Sample CSV Format**

Create a file named `sample_stock_data.csv`:

```csv
date,close,high,low,volume
2024-01-01,150.25,152.30,149.80,1000000
2024-01-02,151.50,153.00,150.00,1200000
2024-01-03,152.75,154.50,151.25,1100000
2024-01-04,151.00,153.25,150.50,1050000
2024-01-05,153.50,155.00,152.00,1300000
2024-01-08,154.25,156.00,153.00,1400000
2024-01-09,155.00,157.50,154.00,1500000
2024-01-10,156.75,158.00,155.50,1350000
```

---

## 📡 API Documentation

### **Base URL**
```
http://localhost:8000/api
```

### **1. Health Check**

**Endpoint:** `GET /api/health`

**Request:**
```bash
curl http://localhost:8000/api/health
```

**Response:**
```json
{
  "status": "healthy",
  "message": "Stock Trend Prediction API is running",
  "models_loaded": true,
  "available_endpoints": [
    "/api/predict/image",
    "/api/predict/numeric",
    "/health"
  ]
}
```

### **2. Image-Based Prediction**

**Endpoint:** `POST /api/predict/image`

**Request (cURL):**
```bash
curl -X POST http://localhost:8000/api/predict/image \
  -H "Content-Type: multipart/form-data" \
  -F "file=@chart.png"
```

**Request (Python):**
```python
import requests

url = "http://localhost:8000/api/predict/image"
files = {"file": open("chart.png", "rb")}

response = requests.post(url, files=files)
result = response.json()
print(result)
```

**Request (JavaScript):**
```javascript
const formData = new FormData();
formData.append('file', imageFile);

const response = await fetch('http://localhost:8000/api/predict/image', {
  method: 'POST',
  body: formData
});

const result = await response.json();
console.log(result);
```

**Response:**
```json
{
  "prediction": {
    "trend": "UP",
    "confidence": 87.34,
    "probabilities": {
      "DOWN": 4.21,
      "SIDEWAYS": 8.45,
      "UP": 87.34
    }
  },
  "analysis": {
    "risk_level": "Low",
    "sentiment": "Strongly Bullish - Clear upward momentum detected",
    "explanation": "Based on chart pattern analysis, the model predicts an upward trend with 87.3% confidence."
  },
  "insights": [
    "Primary prediction: UP (87.3% probability)",
    "Alternative scenario: SIDEWAYS (8.5% probability)",
    "Model shows high conviction in this prediction"
  ],
  "recommendations": [
    "✅ Consider this as a potential buying opportunity",
    "📈 Set stop-loss orders to protect against reversals",
    "📚 Always perform your own due diligence"
  ],
  "disclaimer": "This analysis is for educational purposes only..."
}
```

### **3. Numeric Data Prediction**

**Endpoint:** `POST /api/predict/numeric`

**Request (cURL):**
```bash
curl -X POST http://localhost:8000/api/predict/numeric \
  -H "Content-Type: multipart/form-data" \
  -F "file=@stock_data.csv"
```

**Request (Python):**
```python
import requests

url = "http://localhost:8000/api/predict/numeric"
files = {"file": open("stock_data.csv", "rb")}

response = requests.post(url, files=files)
result = response.json()
print(result)
```

**Response:**
```json
{
  "prediction": {
    "trend": "DOWN",
    "confidence": 72.18,
    "probabilities": {
      "DOWN": 72.18,
      "SIDEWAYS": 15.32,
      "UP": 12.50
    }
  },
  "analysis": {
    "risk_level": "Medium",
    "sentiment": "Moderately Bearish",
    "explanation": "Based on technical indicators, downward trend predicted with 72.2% confidence."
  },
  "insights": [
    "Primary prediction: DOWN (72.2% probability)",
    "High volatility detected (35.2%)",
    "RSI indicates oversold conditions"
  ],
  "recommendations": [
    "⚠️ Exercise caution - Consider reducing exposure",
    "🛡️ Set tight stop-losses if holding",
    "📊 Monitor for reversal signals"
  ]
}
```

### **Error Responses**

**400 Bad Request:**
```json
{
  "detail": "Invalid file format. Please upload a valid image or CSV file."
}
```

**503 Service Unavailable:**
```json
{
  "detail": "Models not loaded. Please try again later."
}
```

---

## 🌐 Browser Exhibition

### **Accessing the Application**

1. **Start both backend and frontend** as described in [Running the Application](#-running-the-application)

2. **Open your browser** and navigate to:
   ```
   http://localhost:5173
   ```

3. **You will see:**
   - Modern glassmorphism interface with dark theme
   - Header with "Stock Trend Prediction AI" title
   - API status indicator (green = online)
   - Two mode buttons: "Chart Image" and "Numeric Data"
   - File upload area with drag-and-drop support
   - "Predict Trend" button

### **Interactive API Documentation**

FastAPI provides automatic interactive API documentation:

**Swagger UI:**
```
http://localhost:8000/docs
```
- Interactive API testing
- Try out endpoints directly
- View request/response schemas

**ReDoc:**
```
http://localhost:8000/redoc
```
- Alternative documentation view
- Clean, organized layout
- Detailed schema information

### **Testing the Application**

1. **Health Check:**
   - Open: http://localhost:8000/api/health
   - Should show: `{"status": "healthy", "models_loaded": true}`

2. **Upload Test:**
   - Use sample images from `assets/images/`
   - Or use sample CSV from `assets/sample_data/`

3. **View Results:**
   - Results appear below the upload area
   - Animated cards with predictions
   - Color-coded trend indicators
   - Detailed analysis sections

### **Browser Compatibility**

Tested and working on:
- ✅ Chrome 90+
- ✅ Firefox 88+
- ✅ Edge 90+
- ✅ Safari 14+

---

## 🔧 Troubleshooting

### **Backend Issues**

**Problem:** `ModuleNotFoundError`
```bash
# Solution: Ensure virtual environment is activated
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Reinstall dependencies
pip install -r requirements.txt
```

**Problem:** `Port 8000 already in use`
```bash
# Solution: Kill the process or change port
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

**Problem:** `Models not found`
```bash
# Solution: Ensure models exist in the models/ directory
# Check: models/optimized_stock_model.h5
# Check: models/best_model.h5
```

### **Frontend Issues**

**Problem:** `npm install` fails
```bash
# Solution: Clear cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Problem:** `Port 5173 already in use`
```bash
# Solution: Vite will automatically suggest alternative port
# Or manually kill the process
```

**Problem:** API connection error
```bash
# Solution: Ensure backend is running
# Check: http://localhost:8000/api/health
# Verify CORS settings in backend/.env
```

### **Common Errors**

| Error | Solution |
|-------|----------|
| CORS Error | Update `CORS_ORIGINS` in backend/.env |
| File upload fails | Check file size and format |
| Prediction timeout | Ensure models are loaded correctly |
| Blank screen | Check browser console for errors |

---

## ⚠️ Disclaimer

**This application is for educational purposes only.**

- ❌ Not financial advice
- ❌ Not investment recommendations
- ✅ Always conduct your own research
- ✅ Consult qualified financial advisors
- ✅ Past performance ≠ future results
- ✅ Use at your own risk

**The predictions are based on historical patterns and may not reflect actual market conditions.**

---

## 🤝 Contributing

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

**Code Style:**
- Python: Follow PEP 8
- JavaScript: Use ES6+ features
- Write clear comments
- Add tests for new features

---

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- TensorFlow team for the ML framework
- FastAPI team for the web framework
- React team for the UI library
- The open-source community

---

## 📞 Support

For issues or questions:
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/stock-trend-prediction/issues)
- 📧 Email: your.email@example.com
- 📖 Docs: http://localhost:8000/docs

---

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

---

<div align="center">

**Built with ❤️ using modern web technologies and AI**

**Version 1.0.0** | **Last Updated: December 2024**

[⬆ Back to Top](#-stock-trend-prediction-ai)

</div>
