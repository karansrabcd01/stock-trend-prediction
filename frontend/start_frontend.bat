@echo off
echo ========================================
echo   Stock Trend Prediction AI
echo   Frontend Startup Script
echo ========================================
echo.

cd /d "%~dp0"

echo [1/3] Checking Node.js...
node --version
if errorlevel 1 (
    echo ERROR: Node.js not found! Please install Node.js 16+
    pause
    exit /b 1
)

echo.
echo [2/3] Checking npm...
npm --version
if errorlevel 1 (
    echo ERROR: npm not found!
    pause
    exit /b 1
)

echo.
echo [3/3] Installing/Checking dependencies...
if not exist "node_modules\" (
    echo Installing dependencies...
    npm install
    if errorlevel 1 (
        echo ERROR: Failed to install dependencies
        pause
        exit /b 1
    )
) else (
    echo Dependencies already installed
)

echo.
echo ========================================
echo   Starting Frontend Server...
echo ========================================
echo.
echo Frontend will run on: http://localhost:5173
echo.
echo Press Ctrl+C to stop the server
echo.

npm run dev

pause
