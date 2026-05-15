# Face Detector

A Python script that detects faces in images, counts them, and draws red circles around each detected face.

## Features

- Detects faces using MTCNN (Multi-task Cascaded Convolutional Networks)
- Handles rotated images automatically
- Draws red circles around detected faces
- Outputs annotated image with face count

## Requirements

- Python 3.8+
- macOS, Linux, or Windows

## Installation

1. Clone or download this repository:
   ```bash
   cd CountPeople
   ```

2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

3. Activate the virtual environment:
   ```bash
   # macOS/Linux
   source venv/bin/activate

   # Windows
   venv\Scripts\activate
   ```

4. Install dependencies:
   ```bash
   pip install opencv-python mtcnn tensorflow
   ```

## Usage

1. Activate the virtual environment (if not already active):
   ```bash
   source venv/bin/activate
   ```

2. Run the script with an image:
   ```bash
   python face_detector.py <image_path> [confidence]
   ```

   **Parameters:**
   - `image_path` - Path to the input image (required)
   - `confidence` - Minimum detection confidence, 0.0-1.0 (optional, default: 0.9)

3. Examples:
   ```bash
   # Basic usage
   python face_detector.py photo.jpg

   # Lower confidence for more detections
   python face_detector.py crowd.jpg 0.5

   # Higher confidence for fewer false positives
   python face_detector.py portrait.jpg 0.95
   ```

4. Output:
   - The script prints the number of faces detected
   - An annotated image is saved as `<original_name>_faces_detected.jpg`

## Confidence Threshold Guide

| Value | Use Case |
|-------|----------|
| 0.95+ | Portraits, clear faces |
| 0.9   | Default, balanced |
| 0.7-0.8 | Group photos |
| 0.5-0.6 | Crowds, distant faces |

Lower values detect more faces but may include false positives.

## Example Output

```
$ python face_detector.py event_photo.jpg 0.8
Initializing face detector...
Detecting faces...
Faces detected: 55
Output saved to: event_photo_faces_detected.jpg
```
