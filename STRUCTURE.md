# 📁 Project Structure - Stock Trend Prediction AI

This document provides a comprehensive overview of the project's directory structure, optimized for deployment.

---

## 🌳 Directory Tree

```
Stock-Trend-Prediction/
│
├── 📁 backend/                          # Backend API (FastAPI)
│   ├── 📁 app/
│   │   ├── 📁 models/                   # Model management
│   │   │   ├── __init__.py
│   │   │   └── model_manager.py         # Model loading & inference
│   │   ├── 📁 services/                 # Business logic
│   │   │   ├── __init__.py
│   │   │   ├── image_service.py         # Image processing
│   │   │   ├── numeric_service.py       # CSV data processing
│   │   │   └── prediction_service.py    # Prediction logic
│   │   ├── 📁 routes/                   # API endpoints
│   │   │   ├── __init__.py
│   │   │   └── predictions.py           # Prediction routes
│   │   ├── 📁 utils/                    # Utility functions
│   │   │   ├── __init__.py
│   │   │   └── helpers.py               # Helper functions
│   │   ├── __init__.py
│   │   └── config.py                    # Configuration settings
│   ├── main.py                          # Application entry point
│   ├── main_demo.py                     # Demo version
│   ├── requirements.txt                 # Python dependencies
│   ├── .env                             # Environment variables (local)
│   └── .env.example                     # Environment template
│
├── 📁 frontend/                         # Frontend Application (React + Vite)
│   ├── 📁 public/                       # Static assets
│   │   └── vite.svg                     # Vite logo
│   ├── 📁 src/
│   │   ├── 📁 components/               # React components
│   │   │   ├── Header.jsx               # App header
│   │   │   ├── UploadArea.jsx           # File upload component
│   │   │   ├── PredictionResults.jsx    # Results display
│   │   │   └── ModeSelector.jsx         # Image/CSV mode toggle
│   │   ├── 📁 services/                 # API integration
│   │   │   └── api.js                   # API client
│   │   ├── 📁 styles/                   # CSS styles
│   │   │   ├── App.css                  # Main styles
│   │   │   └── index.css                # Global styles
│   │   ├── 📁 utils/                    # Utility functions
│   │   │   └── helpers.js               # Helper functions
│   │   ├── App.jsx                      # Main component
│   │   └── main.jsx                     # Entry point
│   ├── index.html                       # HTML template
│   ├── package.json                     # Node dependencies
│   ├── package-lock.json                # Dependency lock file
│   ├── vite.config.js                   # Vite configuration
│   └── .env.example                     # Environment template
│
├── 📁 models/                           # Trained ML Models
│   ├── optimized_stock_model.h5         # Numeric prediction model (7.5 MB)
│   ├── best_model.h5                    # Image prediction model (7.5 MB)
│   ├── optimized_scaler.pkl             # Feature scaler
│   └── feature_columns.pkl              # Feature definitions
│
├── 📁 notebooks/                        # Jupyter Notebooks
│   └── Refine_Stock_trend.ipynb         # Model training notebook
│
├── 📁 assets/                           # Project Assets
│   └── 📁 images/                       # Screenshots & images
│       ├── demo_screenshot.png
│       └── architecture_diagram.png
│
├── 📁 docs/                             # Additional Documentation
│   └── 📁 api/                          # API documentation
│       └── endpoints.md
│
├── 📄 Deployment Configuration Files
├── .dockerignore                        # Docker ignore rules
├── Dockerfile.backend                   # Backend Docker image
├── Dockerfile.frontend                  # Frontend Docker image
├── docker-compose.yml                   # Docker Compose config
├── nginx.conf                           # Nginx configuration
├── render.yaml                          # Render.com blueprint
├── vercel.json                          # Vercel configuration
├── netlify.toml                         # Netlify configuration
├── railway.json                         # Railway.app configuration
├── Procfile                             # Heroku/Railway process file
├── runtime.txt                          # Python runtime version
│
├── 📄 Documentation Files
├── README.md                            # Main documentation
├── DEPLOYMENT.md                        # Deployment guide
├── DOCKER.md                            # Docker guide
├── PROJECT_REPORT.md                    # Detailed project report
├── EXECUTIVE_SUMMARY.md                 # Executive summary
├── PRESENTATION_SLIDES.md               # Presentation content
├── REPORT_INDEX.md                      # Report index
├── SCREENSHOTS_DEMO_GUIDE.md            # Demo guide
│
├── 📄 Configuration Files
├── .gitignore                           # Git ignore rules
├── .gitattributes                       # Git attributes (optional)
├── LICENSE                              # MIT License
│
└── 📄 Project Metadata
    └── STRUCTURE.md                     # This file
```

---

## 📦 Key Directories

### **Backend (`/backend`)**
- **Purpose**: FastAPI-based REST API for predictions
- **Technology**: Python 3.11, FastAPI, TensorFlow
- **Entry Point**: `main.py` or `main_demo.py`
- **Key Files**:
  - `requirements.txt`: Python dependencies
  - `.env`: Environment variables (not in Git)
  - `app/config.py`: Configuration management

### **Frontend (`/frontend`)**
- **Purpose**: React-based web interface
- **Technology**: React 18, Vite 5, Axios
- **Entry Point**: `src/main.jsx`
- **Build Output**: `dist/` (generated)
- **Key Files**:
  - `package.json`: Node dependencies
  - `vite.config.js`: Build configuration
  - `src/App.jsx`: Main component

### **Models (`/models`)**
- **Purpose**: Trained machine learning models
- **Size**: ~15 MB total
- **Files**:
  - `optimized_stock_model.h5`: DNN for numeric data
  - `best_model.h5`: CNN for chart images
  - `optimized_scaler.pkl`: StandardScaler
  - `feature_columns.pkl`: Feature metadata

### **Notebooks (`/notebooks`)**
- **Purpose**: Model training and experimentation
- **Technology**: Jupyter Notebook
- **Note**: Not required for deployment

### **Assets (`/assets`)**
- **Purpose**: Images, screenshots, sample data
- **Note**: Not required for deployment

---

## 🚀 Deployment Structure

### **For Render.com**
```
Project Root
├── backend/          → Web Service (Python)
├── frontend/         → Static Site
├── models/           → Mounted as volume
└── render.yaml       → Blueprint configuration
```

### **For Docker**
```
Project Root
├── Dockerfile.backend    → Backend image
├── Dockerfile.frontend   → Frontend image
├── docker-compose.yml    → Orchestration
└── nginx.conf            → Frontend server config
```

### **For Vercel**
```
Project Root
├── backend/          → Serverless Functions
├── frontend/         → Static Site
└── vercel.json       → Configuration
```

### **For Netlify + Render**
```
Netlify:
├── frontend/         → Static Site
└── netlify.toml      → Configuration

Render:
├── backend/          → Web Service
└── models/           → Mounted volume
```

---

## 📝 File Purposes

### **Configuration Files**

| File | Purpose | Required For |
|------|---------|--------------|
| `.env` | Environment variables | Local development |
| `.env.example` | Environment template | Documentation |
| `requirements.txt` | Python dependencies | Backend deployment |
| `package.json` | Node dependencies | Frontend deployment |
| `vite.config.js` | Vite build settings | Frontend build |

### **Deployment Files**

| File | Purpose | Platform |
|------|---------|----------|
| `render.yaml` | Service configuration | Render.com |
| `vercel.json` | Deployment config | Vercel |
| `netlify.toml` | Build settings | Netlify |
| `railway.json` | Service config | Railway.app |
| `Procfile` | Process definition | Heroku/Railway |
| `runtime.txt` | Python version | Multiple |
| `Dockerfile.backend` | Backend container | Docker |
| `Dockerfile.frontend` | Frontend container | Docker |
| `docker-compose.yml` | Multi-container | Docker Compose |
| `nginx.conf` | Web server config | Docker/Nginx |

### **Documentation Files**

| File | Purpose | Audience |
|------|---------|----------|
| `README.md` | Main documentation | All users |
| `DEPLOYMENT.md` | Deployment guide | DevOps |
| `DOCKER.md` | Docker guide | Docker users |
| `PROJECT_REPORT.md` | Detailed report | Academic/Business |
| `EXECUTIVE_SUMMARY.md` | High-level overview | Executives |
| `STRUCTURE.md` | This file | Developers |

---

## 🔧 Build Artifacts

### **Backend Build**
```
backend/
├── __pycache__/      # Python bytecode (ignored)
└── *.pyc             # Compiled Python (ignored)
```

### **Frontend Build**
```
frontend/
├── node_modules/     # Dependencies (ignored)
├── dist/             # Production build (generated)
└── .vite/            # Vite cache (ignored)
```

---

## 🚫 Ignored Files

See `.gitignore` for complete list. Key exclusions:

- **Python**: `__pycache__/`, `*.pyc`, `venv/`
- **Node**: `node_modules/`, `dist/`
- **Environment**: `.env`, `.env.local`
- **IDE**: `.vscode/`, `.idea/`
- **OS**: `.DS_Store`, `Thumbs.db`
- **Deployment**: `.vercel`, `.netlify`, `.railway`

---

## 📊 File Sizes

| Directory | Approximate Size | Notes |
|-----------|-----------------|-------|
| `backend/` | ~5 MB | Without venv |
| `frontend/` | ~2 MB | Without node_modules |
| `models/` | ~15 MB | ML model files |
| `notebooks/` | ~1 MB | Jupyter notebooks |
| `assets/` | ~5 MB | Images & screenshots |
| **Total** | **~28 MB** | Excluding dependencies |

With dependencies:
- `backend/venv/`: ~500 MB
- `frontend/node_modules/`: ~200 MB

---

## 🔐 Security Notes

### **Never Commit**
- `.env` files with secrets
- API keys or tokens
- Database credentials
- SSL certificates (`.pem`, `.key`)
- Service account files

### **Use Environment Variables For**
- API URLs
- Database connections
- Third-party API keys
- Feature flags
- CORS origins

---

## 🎯 Deployment Checklist

Before deploying, ensure:

- [ ] All `.env.example` files are updated
- [ ] Models are in `models/` directory
- [ ] `requirements.txt` is complete
- [ ] `package.json` dependencies are locked
- [ ] `.gitignore` excludes sensitive files
- [ ] README.md has deployment instructions
- [ ] API endpoints are documented
- [ ] CORS origins are configured
- [ ] Health check endpoints work
- [ ] Build scripts are tested locally

---

## 📞 Support

For questions about project structure:
- See `README.md` for general info
- See `DEPLOYMENT.md` for deployment
- See `DOCKER.md` for containerization
- Check GitHub Issues for known problems

---

**Last Updated**: December 2024  
**Version**: 1.0.0  
**Maintained By**: Development Team
