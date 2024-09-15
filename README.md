# EyesWideCode
 Real-Time Emotion Insights &amp; Focus Clock
Real-Time Emotion Detection and Screen Time Tracker
!Emotion Detection <!-- Replace with an actual screenshot or relevant image -->

# Real-Time Emotion Detection and Screen Time Tracker

![Emotion Detection](https://cdn.dribbble.com/users/252149/screenshots/2589640/6deg_emotions.gif)

## Project Overview
The **Real-Time Emotion Detection and Screen Time Tracker** is a Python application that combines two powerful features:

1. **Emotion Detection**: It analyzes faces captured by your webcam and predicts the dominant emotion (e.g., happy, sad, surprised) using `DeepFace`.
2. **Screen Time Tracking**: It tracks how much time you spend looking at the screen (on-screen time) versus away from it (off-screen time).

## Features
### Emotion Analysis:
- Detects faces in real-time.
- Predicts the dominant emotion for each detected face.
- Displays the emotion on the screen.

### Screen Time Tracking:
- Calculates on-screen and off-screen time.
- Alerts with a buzzer sound if off-screen time exceeds a threshold.
- Records maximum on-screen and off-screen times in an Excel sheet (`timer_data.xlsx`).


### Results :
Real-time emotion detection is displayed on the screen.
Maximum on-screen and off-screen times are saved in timer_data.xlsx.



 #### Example Use Cases :
Screen Time Monitoring: Keep track of your screen time during work or study sessions.
Emotion Tracking: Understand emotional reactions during video calls or online meetings.

## How It Works

### Dependencies
To run this project, you'll need the following Python libraries:
- `OpenCV` (cv2)
- `DeepFace`
- `Openpyxl`

You can install these using the following command:
```bash
pip install opencv-python deepface openpyxl




