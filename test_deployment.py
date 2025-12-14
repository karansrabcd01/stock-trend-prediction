"""
Quick test script to verify model loading works correctly
Run this before deploying to Render
"""
import sys
from pathlib import Path

# Add backend to path
backend_path = Path(__file__).parent / "backend"
sys.path.insert(0, str(backend_path))

def test_model_loading():
    """Test if models load correctly"""
    print("=" * 60)
    print("🧪 Testing Model Loading")
    print("=" * 60)
    
    try:
        from app.config import settings
        from app.models.model_manager import model_manager
        
        # Test 1: Check model directory
        print(f"\n1️⃣ Model Directory Check:")
        print(f"   Path: {settings.MODEL_DIR}")
        print(f"   Exists: {Path(settings.MODEL_DIR).exists()}")
        
        if Path(settings.MODEL_DIR).exists():
            print(f"   ✅ Model directory found!")
            
            # List files
            model_files = list(Path(settings.MODEL_DIR).glob("*"))
            print(f"\n   Files in directory:")
            for f in model_files:
                print(f"   - {f.name} ({f.stat().st_size / 1024 / 1024:.2f} MB)")
        else:
            print(f"   ❌ Model directory not found!")
            return False
        
        # Test 2: Load models
        print(f"\n2️⃣ Loading Models:")
        success = model_manager.load_models()
        
        if success:
            print(f"   ✅ Models loaded successfully!")
        else:
            print(f"   ❌ Model loading failed!")
            return False
        
        # Test 3: Check model readiness
        print(f"\n3️⃣ Model Readiness Check:")
        is_ready = model_manager.is_ready()
        print(f"   Ready: {is_ready}")
        
        if is_ready:
            print(f"   ✅ Models are ready for predictions!")
        else:
            print(f"   ❌ Models not ready!")
            return False
        
        # Test 4: Check individual models
        print(f"\n4️⃣ Individual Model Status:")
        print(f"   Image Model: {'✅ Loaded' if model_manager.image_model else '❌ Not loaded'}")
        print(f"   Numeric Model: {'✅ Loaded' if model_manager.numeric_model else '❌ Not loaded'}")
        print(f"   Scaler: {'✅ Loaded' if model_manager.scaler else '❌ Not loaded'}")
        print(f"   Feature Columns: {'✅ Loaded' if model_manager.feature_columns else '❌ Not loaded'}")
        
        print("\n" + "=" * 60)
        print("✅ ALL TESTS PASSED!")
        print("=" * 60)
        print("\n🚀 Ready to deploy to Render!")
        return True
        
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

def test_dependencies():
    """Test if all dependencies are installed"""
    print("\n" + "=" * 60)
    print("📦 Testing Dependencies")
    print("=" * 60)
    
    required_packages = [
        "fastapi",
        "uvicorn",
        "tensorflow",
        "numpy",
        "pandas",
        "PIL",
        "sklearn",
        "pydantic",
        "dotenv",
        "cv2"
    ]
    
    missing = []
    for package in required_packages:
        try:
            if package == "PIL":
                __import__("PIL")
            elif package == "sklearn":
                __import__("sklearn")
            elif package == "dotenv":
                __import__("dotenv")
            elif package == "cv2":
                __import__("cv2")
            else:
                __import__(package)
            print(f"   ✅ {package}")
        except ImportError:
            print(f"   ❌ {package} - NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n❌ Missing packages: {', '.join(missing)}")
        print(f"\nInstall with:")
        print(f"   pip install -r backend/requirements.txt")
        return False
    else:
        print(f"\n✅ All dependencies installed!")
        return True

if __name__ == "__main__":
    print("\n🔍 Stock Trend Prediction - Pre-Deployment Test\n")
    
    # Test dependencies first
    deps_ok = test_dependencies()
    
    if not deps_ok:
        print("\n⚠️  Please install dependencies before testing models")
        sys.exit(1)
    
    # Test model loading
    models_ok = test_model_loading()
    
    if models_ok:
        print("\n✅ All checks passed! Safe to deploy.")
        sys.exit(0)
    else:
        print("\n❌ Some checks failed. Please fix before deploying.")
        sys.exit(1)
