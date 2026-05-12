# Contour-Based Object Detection using OpenCV

## Overview
This project performs real-time object detection using traditional Computer Vision techniques in OpenCV.  
It detects objects based on contours and draws bounding boxes around them.

Users can dynamically adjust:
- Canny edge thresholds
- Gaussian blur parameters
- Minimum detectable contour area
- Frame size

using OpenCV trackbars.

---

## Technologies Used
- Python
- OpenCV
- NumPy

---

## Features
- Real-time webcam object detection
- Contour-based detection
- Adjustable thresholds using trackbars
- Bounding box visualization
- Noise filtering using minimum contour area

---

## How It Works
1. Capture webcam frame
2. Convert image to grayscale
3. Apply Gaussian Blur
4. Detect edges using Canny
5. Dilate edges
6. Find contours
7. Filter contours by area
8. Draw bounding boxes around detected objects

---

## Requirements

```txt
opencv-python
numpy
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Run the Project

```bash
python object_detection.py
```

Press `q` to quit.

---

## Trackbar Controls

| Trackbar | Purpose |
|---|---|
| Size | Resize frame |
| sigma_X | Gaussian blur sigma X |
| sigma_Y | Gaussian blur sigma Y |
| Threshold 1 | Lower Canny threshold |
| Threshold 2 | Upper Canny threshold |
| MinArea | Minimum contour area |

---

## OpenCV Functions Used
- `cv2.GaussianBlur()`
- `cv2.Canny()`
- `cv2.findContours()`
- `cv2.contourArea()`
- `cv2.boundingRect()`
- `cv2.rectangle()`

---

## Future Improvements
- Shape detection
- Object tracking
- FPS counter
- Save output video

