#!/usr/bin/env python3
"""Quick test to verify all imports work"""

import sys
import os

print("Testing imports...")

try:
    import pkg_resources
    print("✅ pkg_resources")
except ImportError as e:
    print(f"❌ pkg_resources: {e}")
    sys.exit(1)

try:
    import streamlit
    print("✅ streamlit")
except ImportError as e:
    print(f"❌ streamlit: {e}")
    sys.exit(1)

try:
    import cv2
    print("✅ opencv")
except ImportError as e:
    print(f"❌ opencv: {e}")
    sys.exit(1)

try:
    from mtcnn import MTCNN
    print("✅ mtcnn")
except ImportError as e:
    print(f"❌ mtcnn: {e}")
    sys.exit(1)

try:
    import tensorflow
    print("✅ tensorflow")
except ImportError as e:
    print(f"❌ tensorflow: {e}")
    sys.exit(1)

print("\n🎉 All dependencies installed correctly!")
print("Run: streamlit run app.py")
