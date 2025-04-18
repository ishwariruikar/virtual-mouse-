# 🖱 AI Virtual Mouse

A gesture-controlled *AI Virtual Mouse* built with *Python, **OpenCV, and **MediaPipe* that replaces the traditional physical mouse with real-time hand tracking using a webcam. This project is aimed at promoting touchless human-computer interaction — an ideal alternative in accessibility-focused, pandemic-aware, or futuristic use cases.

Developed as part of the *final year BBA(CA)* academic project (2023–2024), this system demonstrates impressive *97.37% accuracy* and is suitable for real-world usage with standard hardware.

## 🧠 Project Objective

To control all standard mouse functions — cursor movement, left/right click, drag, etc. — using just hand gestures, without needing to physically touch any device.

## 🔍 Features

- ✋ Real-time hand tracking using webcam
- 🎯 Accurate gesture detection using *MediaPipe*
- 🖱 Supports left-click, right-click, drag, and cursor movement
- ⚙ Implemented using *Python, **OpenCV, **NumPy, **AutoPy*
- 💡 Color and gesture recognition with HSV filtering and morphological operations
- 👤 Accessibility-friendly: usable by individuals with limited mobility
- 🛡 Touch-free: helps reduce infection spread in public device usage (COVID-19 safe)
- 💻 Runs on a single CPU with optimized real-time performance

## 🏗 System Architecture

### 🔧 Hardware Requirements

- Webcam (built-in or external)
- Standard desktop/laptop with:
  - Intel Core2Duo or above
  - 4 GB RAM
  - 320 GB HDD
  - 14” display (or larger)

### 💻 Software Stack

| Component        | Technology Used           |
|------------------|---------------------------|
| Programming Lang | Python                    |
| Libraries        | OpenCV, MediaPipe, NumPy, AutoPy |
| OS               | Windows 10 (64-bit)       |
| IDE              | Visual Studio / VS Code   |

## 🗂 Modules and Workflow

1. *Calibration Phase*  
   - Detect and store color HSV values for tracking.

2. *Recognition Phase*  
   - Real-time image capture
   - HSV filtering and binary thresholding
   - Morphological transformations
   - Blob and contour detection
   - Mapping gestures to mouse actions

3. *Mouse Actions Execution*  
   - Coordinate acquisition
   - Execute left-click, right-click, drag, and move based on gesture logic

## 🎯 Accuracy

- System tested on multiple lighting conditions and hand sizes
- Achieved an overall *97.37% accuracy*
- Performs well in real-time even on standard CPUs

## 📌 Limitations

- Performance may drop in poor lighting
- Accuracy of right-click and drag operations could be improved
- Limited detection distance due to webcam range

## 📈 Future Improvements

- Enhanced fingertip detection for more reliable dragging
- Add multi-hand support
- Custom gesture mapping
- Mobile compatibility (camera-based control on phones/tablets)
- Machine learning models for adaptive gesture recognition

## 🏁 Conclusion

This AI Virtual Mouse project demonstrates how computer vision and machine learning can be combined to create practical, touchless, and accessible alternatives to conventional input devices. With further refinement, it could serve as a foundation for assistive tech, smart interfaces, and futuristic HCI systems.

