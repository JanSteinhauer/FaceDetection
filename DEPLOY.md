# Quick Deploy Guide for Streamlit Community Cloud

## Prerequisites
- GitHub account
- This code pushed to a GitHub repository

## Steps

1. **Push to GitHub:**
   ```bash
   git add .
   git commit -m "Add Streamlit web interface"
   git push origin main
   ```

2. **Deploy:**
   - Go to https://share.streamlit.io
   - Click "New app"
   - Select your repository
   - Main file: `app.py`
   - Click "Deploy"

3. **Done!** Your app will be live at:
   ```
   https://[your-username]-countpeople-[app-name].streamlit.app
   ```

## First Time Setup

If you haven't used Streamlit Cloud before:
1. Sign in with GitHub at https://share.streamlit.io
2. Authorize Streamlit to access your repositories
3. That's it!

## Auto-Updates

Any time you push to your GitHub repository, your app will automatically redeploy with the changes.

## Resource Limits (Free Tier)

- 1 GB RAM
- 1 CPU core
- Apps sleep after 7 days of inactivity
- Unlimited viewers

Perfect for personal projects and demos!

## Alternative: Test Locally First

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open in your browser at http://localhost:8501
