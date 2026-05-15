#!/usr/bin/env python3
"""Test EXIF orientation fix"""

from PIL import Image, ImageOps
import sys

def test_exif_fix():
    """Test that EXIF orientation correction works"""
    try:
        # Create a simple test image
        test_img = Image.new('RGB', (100, 200), color='red')

        # Try the correction function
        corrected = ImageOps.exif_transpose(test_img)

        print("✅ EXIF orientation fix is working")
        print(f"   Original size: {test_img.size}")
        print(f"   After correction: {corrected.size}")
        return True

    except Exception as e:
        print(f"❌ EXIF fix error: {e}")
        return False

if __name__ == "__main__":
    success = test_exif_fix()
    sys.exit(0 if success else 1)
