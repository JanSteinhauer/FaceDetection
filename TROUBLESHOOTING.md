# 🐛 Troubleshooting Guide

## Common Issues & Solutions

### ❌ `ModuleNotFoundError: No module named 'pkg_resources'`

**Solution:** Install correct setuptools version
```bash
source .venv/bin/activate
pip install setuptools==69.5.1
```

**Fixed in:** `requirements.txt` (already includes `setuptools==69.5.1`)

---

### ❌ `TypeError: ImageMixin.image() got an unexpected keyword argument 'use_container_width'`

**Cause:** Old Streamlit version (< 1.33.0)

**Solution:** Upgrade Streamlit
```bash
source .venv/bin/activate
pip install --upgrade 'streamlit>=1.33.0'
```

**Fixed in:** `requirements.txt` (now uses `streamlit>=1.33.0`)

---

### ❌ CORS Warning Message

**Symptom:**
```
Warning: the config option 'server.enableCORS=false' is not compatible 
with 'server.enableXsrfProtection=true'
```

**Solution:** Already fixed in `.streamlit/config.toml`

---

### ❌ App Won't Start

**Check dependencies:**
```bash
source .venv/bin/activate
python test_imports.py
```

**Reinstall everything:**
```bash
rm -rf .venv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

### ❌ "No faces detected" Even With Clear Faces

**Solutions:**

1. **Lower confidence threshold** (try 0.5 - 0.7) - Default is now 0.5
2. **Check image quality** - Make sure faces are visible
3. **Try different image format** - Convert to JPG if using PNG
4. **Check image size** - Very large images may need resizing

---

### ❌ Image Displayed Upside Down or Rotated

**Solution:** Fixed! The app now automatically corrects image orientation using EXIF data.

The `get_corrected_orientation()` function handles:
- Photos from phones (portrait/landscape)
- Camera images with rotation metadata
- Images with EXIF orientation tags

Both the original and detected images will display in the correct orientation.

---

### ❌ App is Slow / Hangs

**Causes & Solutions:**

1. **First run:** MTCNN downloads model files (~1MB)
   - Wait a minute, it only happens once

2. **Large images:** Resize before upload
   ```bash
   # Use ImageMagick to resize
   convert large.jpg -resize 1920x1080 smaller.jpg
   ```

3. **Low memory:** Close other apps

---

### ❌ Virtual Environment Issues

**macOS/Linux:**
```bash
# Deactivate current venv
deactivate

# Remove old venv
rm -rf .venv venv

# Create fresh venv
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

**Windows:**
```bash
# Deactivate
deactivate

# Remove old venv
rmdir /s .venv

# Create fresh venv
python -m venv .venv
.venv\Scripts\activate
pip install --upgrade pip
pip install -r requirements.txt
```

---

### ❌ Port 8501 Already in Use

**Solution:** Kill existing Streamlit process

**macOS/Linux:**
```bash
lsof -ti:8501 | xargs kill -9
```

**Windows:**
```bash
netstat -ano | findstr :8501
taskkill /PID <PID> /F
```

Or use a different port:
```bash
streamlit run app.py --server.port 8502
```

---

### ❌ TensorFlow Warnings

**Symptom:** Lots of TensorFlow logging

**Solution:** Already suppressed via:
```python
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
```

Warnings are normal and don't affect functionality.

---

### ❌ Deployment Issues

#### Streamlit Cloud Deployment Fails

1. **Check requirements.txt** is in root directory
2. **Verify all files are pushed** to GitHub
3. **Check logs** in Streamlit Cloud dashboard
4. **Ensure Python version** in settings (3.8-3.12)

#### App Crashes After Deployment

1. **Memory limit exceeded:**
   - Free tier has 1GB RAM
   - Try reducing image sizes
   - Consider Hugging Face Spaces (16GB free)

2. **Missing files:**
   - Ensure all `.py` files are in repo
   - Check `.gitignore` isn't excluding needed files

---

## 🆘 Still Having Issues?

### Quick Reset:
```bash
# Full clean reinstall
rm -rf .venv __pycache__
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
./start.sh
```

### Get Help:

1. **Check test script:**
   ```bash
   python test_imports.py
   ```

2. **Verify Python version:**
   ```bash
   python --version  # Should be 3.8+
   ```

3. **Check disk space:**
   ```bash
   df -h  # macOS/Linux
   ```

4. **Review error logs carefully** - They usually tell you exactly what's wrong!

---

## ✅ Everything Working?

If all tests pass, run:
```bash
./start.sh
```

Your app should open at `http://localhost:8501` 🎉
