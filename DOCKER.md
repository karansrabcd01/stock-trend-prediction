# Docker Quick Start Guide

## 🐳 Running with Docker

### Prerequisites
- Docker installed ([Get Docker](https://docs.docker.com/get-docker/))
- Docker Compose installed (included with Docker Desktop)

### Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/stock-trend-prediction.git
cd stock-trend-prediction

# 2. Build and run with Docker Compose
docker-compose up --build

# 3. Access the application
# Frontend: http://localhost
# Backend: http://localhost:8000
# API Docs: http://localhost:8000/docs
```

### Individual Services

#### Backend Only
```bash
docker build -f Dockerfile.backend -t stock-trend-api .
docker run -p 8000:8000 stock-trend-api
```

#### Frontend Only
```bash
docker build -f Dockerfile.frontend -t stock-trend-frontend \
  --build-arg VITE_API_URL=http://localhost:8000/api .
docker run -p 80:80 stock-trend-frontend
```

### Production Deployment

```bash
# Build for production
docker-compose -f docker-compose.yml up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down

# Stop and remove volumes
docker-compose down -v
```

### Environment Variables

Create a `.env` file in the root directory:

```env
# Backend
ENVIRONMENT=production
CORS_ORIGINS=http://localhost,https://yourdomain.com
PORT=8000

# Frontend
VITE_API_URL=http://localhost:8000/api
```

### Health Checks

```bash
# Check backend health
curl http://localhost:8000/api/health

# Check frontend health
curl http://localhost/health
```

### Troubleshooting

**Port already in use:**
```bash
# Change ports in docker-compose.yml
ports:
  - "8080:8000"  # Backend
  - "3000:80"    # Frontend
```

**Models not found:**
```bash
# Ensure models directory exists and contains:
# - optimized_stock_model.h5
# - best_model.h5
# - optimized_scaler.pkl
# - feature_columns.pkl
```

**Build fails:**
```bash
# Clean build
docker-compose down -v
docker-compose build --no-cache
docker-compose up
```
