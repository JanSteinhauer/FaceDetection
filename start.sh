#!/bin/bash
# Quick start script for the Streamlit app

echo "🚀 Starting Face Detection Web App by Jan Steinhauer..."
echo ""

# Check if virtual environment exists
if [ ! -d ".venv" ]; then
    echo "Creating virtual environment..."
    python3 -m venv .venv
fi

# Activate virtual environment
source .venv/bin/activate

# Install dependencies if needed
echo "Installing dependencies..."
pip install -q -r requirements.txt

# Test imports
echo "Testing dependencies..."
python test_imports.py
if [ $? -ne 0 ]; then
    echo ""
    echo "❌ Dependency error. Please check the error above."
    exit 1
fi

# Start Streamlit
echo ""
echo "✅ Starting app at http://localhost:8501"
echo "Press Ctrl+C to stop the server"
echo ""

streamlit run app.py
