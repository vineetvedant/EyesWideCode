import cv2
from deepface import DeepFace
import time
from openpyxl import Workbook  # Example using Openpyxl
import winsound  # Import winsound for buzzer

# Load face cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Start capturing video
cap = cv2.VideoCapture(0)

# Settings
maximum_time = 15  # Seconds

# Track TIME
starting_time = time.time()
on_screen_time = 0
off_screen_time = 0
total_time = 0

max_on_screen_time = 0
max_off_screen_time = 0

# Create an Excel sheet
wb = Workbook()
sheet = wb.active

previous_off_screen_time = 0

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Convert grayscale frame to RGB format
    rgb_frame = cv2.cvtColor(gray_frame, cv2.COLOR_GRAY2RGB)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Check if face is detected
    if len(faces) > 0:
        print("Face looking at the screen")
        on_screen_time += 1
        total_time += 1
    else:
        print("NO FACE")
        off_screen_time += 1
        total_time += 1

    # Calculate time in hh.mm.ss format
    on_screen_time_hh = int(on_screen_time // 3600)
    on_screen_time_mm = int((on_screen_time % 3600) // 60)
    on_screen_time_ss = int(on_screen_time % 60)

    off_screen_time_hh = int(off_screen_time // 3600)
    off_screen_time_mm = int((off_screen_time % 3600) // 60)
    off_screen_time_ss = int(off_screen_time % 60)

    # Update max on-screen time and max off-screen time
    if on_screen_time > max_on_screen_time:
        max_on_screen_time = on_screen_time
    if off_screen_time > max_off_screen_time:
        max_off_screen_time = off_screen_time

    # Check for buzzer sound
    if off_screen_time - previous_off_screen_time >= 30:
        print("BUZZER SOUND!")
        winsound.Beep(2500, 1000)  # 2500 Hz frequency, 1000 ms duration
        previous_off_screen_time = off_screen_time

    # Display timer on screen
    cv2.putText(frame, f"On-Screen Time: {on_screen_time_hh:02d}:{on_screen_time_mm:02d}:{on_screen_time_ss:02d}", (10, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    cv2.putText(frame, f"Off-Screen Time: {off_screen_time_hh:02d}:{off_screen_time_mm:02d}:{off_screen_time_ss:02d}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)

    # Emotion Detection Section
    for (x, y, w, h) in faces:
        # Extract the face ROI (Region of Interest)
        face_roi = rgb_frame[y:y + h, x:x + w]

        # Perform emotion analysis on the face ROI
        try:
            result = DeepFace.analyze(face_roi, actions=['emotion'], enforce_detection=False)

            # Determine the dominant emotion
            emotion = result[0]['dominant_emotion']

            # Display the predicted emotion on the right side of the screen
            frame_width = frame.shape[1]
            emotion_text_width = cv2.getTextSize(emotion, cv2.FONT_HERSHEY_SIMPLEX, 1.5, 3)[0][0]
            text_x = frame_width - emotion_text_width - 10
            cv2.putText(frame, emotion, (text_x, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 3)

        except:
            pass  # Handle potential errors in DeepFace analysis

    # Display the resulting frame
    cv2.imshow('Real-time Emotion Detection', frame)

    # Press 'q' to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Store max on-screen time and max off-screen time in Excel sheet
sheet['A1'] = "Max On-Screen Time"
sheet['B1'] = f"{max_on_screen_time_hh:02d}:{max_on_screen_time_mm:02d}:{max_on_screen_time_ss:02d}"

sheet['A2'] = "Max Off-Screen Time"
sheet['B2'] = f"{max_off_screen_time_hh:02d}:{max_off_screen_time_mm:02d}:{max_off_screen_time_ss:02d}"

# Save the Excel sheet
wb.save("timer_data.xlsx")

# Release the capture and close all windows
cap.release()
cv2.destroyAllWindows() 