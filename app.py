#!/usr/bin/env python3
"""
Streamlit Face Detection Web App
Upload an image and detect faces with adjustable confidence.
"""

import streamlit as st
import cv2
import numpy as np
from PIL import Image
import os
import tempfile

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from mtcnn import MTCNN
from face_detector import rotate_image, detect_faces_mtcnn, find_best_orientation


@st.cache_resource
def load_detector():
    """Load and cache the MTCNN detector."""
    return MTCNN()


def get_corrected_orientation(image):
    """Get the correctly oriented image based on EXIF data."""
    try:
        # Try to get EXIF orientation data
        from PIL import ImageOps
        return ImageOps.exif_transpose(image)
    except:
        return image


def process_image(image, min_confidence):
    """Process the uploaded image and return annotated image with face count."""
    img_array = np.array(image)
    img_bgr = cv2.cvtColor(img_array, cv2.COLOR_RGB2BGR)

    detector = load_detector()

    with st.spinner("Detecting faces..."):
        oriented_image, faces = find_best_orientation(img_bgr, detector, min_confidence)

    for (box, conf) in faces:
        x, y, w, h = box
        center_x = x + w // 2
        center_y = y + h // 2
        radius = max(w, h) // 2
        cv2.circle(oriented_image, (center_x, center_y), radius, (0, 0, 255), 4)

    result_rgb = cv2.cvtColor(oriented_image, cv2.COLOR_BGR2RGB)
    return result_rgb, len(faces), faces


def main():
    st.set_page_config(
        page_title="Face Detection - Jan Steinhauer",
        page_icon="👤",
        layout="wide"
    )

    st.title("👤 Face Detection by Jan Steinhauer")
    st.markdown("Upload an image to detect and count faces using AI")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("Upload Image")
        uploaded_file = st.file_uploader(
            "Choose an image...",
            type=["jpg", "jpeg", "png"],
            help="Supported formats: JPG, JPEG, PNG"
        )

        confidence = st.slider(
            "Detection Confidence",
            min_value=0.5,
            max_value=0.99,
            value=0.5,
            step=0.05,
            help="Lower = more faces detected (but more false positives)"
        )

        st.info("**Confidence Guide:**\n"
                "- 0.95+: Portraits, clear faces only\n"
                "- 0.70-0.80: Group photos\n"
                "- 0.50-0.60: Crowds, distant faces (default)")

    with col2:
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            # Fix orientation based on EXIF data
            image = get_corrected_orientation(image)

            st.subheader("Original Image")
            st.image(image, use_container_width=True)

            if st.button("🔍 Detect Faces", type="primary", use_container_width=True):
                result_image, face_count, faces = process_image(image, confidence)

                st.subheader("Detection Results")

                if face_count > 0:
                    st.success(f"✅ **{face_count}** face(s) detected!")
                else:
                    st.warning("⚠️ No faces detected. Try lowering the confidence threshold.")

                st.image(result_image, use_container_width=True)

                result_pil = Image.fromarray(result_image)
                buf = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
                result_pil.save(buf.name, format="JPEG")

                with open(buf.name, "rb") as f:
                    st.download_button(
                        label="⬇️ Download Result",
                        data=f,
                        file_name=f"{uploaded_file.name.split('.')[0]}_faces_detected.jpg",
                        mime="image/jpeg",
                        use_container_width=True
                    )

                os.unlink(buf.name)

                with st.expander("📊 Detection Details"):
                    for i, (box, conf) in enumerate(faces, 1):
                        x, y, w, h = box
                        st.write(f"**Face {i}:** Position ({x}, {y}), Size {w}×{h}, Confidence {conf:.2%}")

    st.markdown("---")
    st.markdown(
        '<div style="text-align: center; color: #666;">'
        'Built by Jan Steinhauer • Powered by Streamlit & MTCNN'
        '</div>',
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
