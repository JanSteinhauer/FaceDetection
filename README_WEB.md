# Face Detection App 👤

A web-based face detection application that counts faces in images using AI.

## 🚀 Features

- Upload images (JPG, PNG)
- Automatic face detection with MTCNN
- **Auto-corrects image orientation** (EXIF-aware) 📸
- Adjustable confidence threshold (default: 0.50 for crowds)
- Visual results with red circles around faces
- Download annotated images
- Auto-rotation for best detection
- **Optimized for crowd detection** 👥

## 🏃 Run Locally

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Start the app:**
   ```bash
   streamlit run app.py
   ```

3. **Open your browser:** The app will automatically open at `http://localhost:8501`

## 📦 Deployment Options

### Option 1: Streamlit Community Cloud (Recommended - Free)

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Sign in with GitHub
4. Deploy from your repository
5. Your app will be live at `https://yourapp.streamlit.app`

**Pros:**
- ✅ 100% Free
- ✅ Easy setup (1-click deploy)
- ✅ Automatic updates from GitHub
- ✅ Built-in SSL/HTTPS
- ✅ No server management

**Cons:**
- ⚠️ Limited resources (1GB RAM)
- ⚠️ Apps sleep after inactivity

### Option 2: Hugging Face Spaces (Free)

1. Create account at [huggingface.co](https://huggingface.co)
2. Create new Space with Streamlit
3. Upload your files or connect GitHub
4. Deploy automatically

**Pros:**
- ✅ Free tier available
- ✅ Good for ML/AI apps
- ✅ GPU support (paid)

### Option 3: Railway (Free Tier)

1. Sign up at [railway.app](https://railway.app)
2. Connect GitHub repository
3. Deploy with auto-detection
4. Free tier: 500 hours/month

### Option 4: Render (Free Tier)

1. Sign up at [render.com](https://render.com)
2. Connect GitHub
3. Select "Web Service"
4. Configure: `streamlit run app.py`

### Option 5: Google Cloud Run (Pay-per-use)

For production workloads with more resources:

```bash
gcloud run deploy face-detector \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated
```

## 🎯 Recommended: Streamlit Community Cloud

For your use case, **Streamlit Community Cloud** is perfect because:
- It's completely free
- Designed specifically for Streamlit apps
- No Docker/config needed
- Auto-deploys from GitHub

## 📊 Confidence Threshold Guide

| Value | Use Case |
|-------|----------|
| 0.50-0.60 | Crowds, distant faces (default) |
| 0.70-0.80 | Group photos |
| 0.95+ | Portraits, clear faces only |

**Default is 0.50** - optimized for detecting faces in crowds and events.

## 🔧 Technical Details

- **Framework:** Streamlit
- **Detection:** MTCNN (Multi-task Cascaded Convolutional Networks)
- **Backend:** TensorFlow
- **Processing:** OpenCV

## 📝 Command Line Version

For batch processing, use the original CLI:

```bash
python face_detector.py photo.jpg 0.9
```

## 🐛 Troubleshooting

**App is slow?**
- Lower the image resolution before upload
- Use higher confidence threshold
- Consider upgrading to paid hosting for more resources

**"No faces detected"?**
- Lower the confidence threshold
- Ensure faces are clearly visible
- Check image orientation

## 📄 License

MIT License - Feel free to use and modify!
