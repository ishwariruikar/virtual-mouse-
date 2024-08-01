import cv2
import numpy as np
import mediapipe as mp
import screen_brightness_control as sbc

mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation
mp_hands = mp.solutions.hands

cap = cv2.VideoCapture(0)

with mp_selfie_segmentation.SelfieSegmentation() as selfie_segmentation:
  with mp_hands.Hands(
      model_complexity=0,
      min_detection_confidence=0.5,
      min_tracking_confidence=0.5) as hands:
    while cap.isOpened():
      success, image = cap.read()
      if not success:
        print("Ignoring empty camera frame.")
        continue

      # Flip the image horizontally for a later selfie-view display, and convert
      # the BGR image to RGB.
      image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)
      results = hands.process(image)

      # Process the image with selfie_segmentation
      results_segmentation = selfie_segmentation.process(image)

      if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
          mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

          # Calculate the distance between thumb tip and pinky tip
          thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
          pinky_tip = hand_landmarks.landmark[mp_hands.HandLandmark.PINKY_TIP]
          distance = np.sqrt((thumb_tip.x - pinky_tip.x)**2 + (thumb_tip.y - pinky_tip.y)**2)

          # Map the distance to volume range
          volume = int(distance * 100)

          # Set the volume
          sbc.set_volume(volume)

      # Draw the segmentation mask on the image
      if results_segmentation.segmentation_mask is not None:
        condition = cv2.merge([results_segmentation.segmentation_mask,
                               results_segmentation.segmentation_mask,
                               results_segmentation.segmentation_mask])
        image = cv2.add(image, condition)

      cv2.imshow('MediaPipe Hands', image)
      if cv2.waitKey(5) & 0xFF == 27:
        break

cap.release()

import screen_brightness_control as sbc

# Set the volume to 50%
sbc.set_volume(50)

# Get the current volume
current_volume = sbc.get_volume()
print(current_volume)

# Set the volume to maximum
sbc.set_volume(100)

# Get the current volume
current_volume = sbc.get_volume()
print(current_volume)