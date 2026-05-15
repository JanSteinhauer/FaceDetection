#!/usr/bin/env python3
"""
Face Detection Script using MTCNN
Excellent at detecting faces of various sizes in crowded scenes.
"""

import cv2
import sys
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

from mtcnn import MTCNN


def rotate_image(image, angle):
    """Rotate image by given angle (90, 180, 270)."""
    if angle == 90:
        return cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    elif angle == 180:
        return cv2.rotate(image, cv2.ROTATE_180)
    elif angle == 270:
        return cv2.rotate(image, cv2.ROTATE_90_COUNTERCLOCKWISE)
    return image


def detect_faces_mtcnn(image, detector, min_confidence=0.9):
    """Detect faces using MTCNN."""
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    faces = detector.detect_faces(rgb_image)
    return [(f['box'], f['confidence']) for f in faces if f['confidence'] >= min_confidence]


def find_best_orientation(image, detector, min_confidence):
    """Try different rotations and return the one with most face detections."""
    best_faces = []
    best_angle = 0
    best_image = image

    for angle in [0, 90, 180, 270]:
        rotated = rotate_image(image, angle) if angle > 0 else image
        faces = detect_faces_mtcnn(rotated, detector, min_confidence)

        if len(faces) > len(best_faces):
            best_faces = faces
            best_angle = angle
            best_image = rotated

    if best_angle != 0:
        print(f"Image was rotated {best_angle}° for best detection")

    return best_image, best_faces


def detect_faces(image_path, min_confidence=0.9):
    """
    Detect faces in an image using MTCNN, draw red circles around them.

    Args:
        image_path: Path to the input image
        min_confidence: Minimum confidence for detection (default: 0.9)

    Returns:
        Number of faces detected, output path
    """
    if not os.path.exists(image_path):
        print(f"Error: Image file '{image_path}' not found.")
        sys.exit(1)

    image = cv2.imread(image_path)
    if image is None:
        print(f"Error: Could not read image '{image_path}'.")
        sys.exit(1)

    print("Initializing face detector...")
    detector = MTCNN()

    print("Detecting faces...")
    image, faces = find_best_orientation(image, detector, min_confidence)

    for (box, conf) in faces:
        x, y, w, h = box
        center_x = x + w // 2
        center_y = y + h // 2
        radius = max(w, h) // 2
        cv2.circle(image, (center_x, center_y), radius, (0, 0, 255), 4)

    base_name = os.path.splitext(image_path)[0]
    output_path = f"{base_name}_faces_detected.jpg"
    cv2.imwrite(output_path, image)

    return len(faces), output_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python face_detector.py <image_path> [min_confidence]")
        print("Example: python face_detector.py photo.jpg 0.8")
        print("Lower confidence = more faces detected (default: 0.9)")
        sys.exit(1)

    image_path = sys.argv[1]
    confidence = float(sys.argv[2]) if len(sys.argv) > 2 else 0.9

    face_count, output_path = detect_faces(image_path, confidence)

    print(f"Faces detected: {face_count}")
    print(f"Output saved to: {output_path}")


if __name__ == "__main__":
    main()
