import cv2
import mediapipe as mp
import time

import json


def capture_image():
    # Initialize MediaPipe Face Detection
    mp_face_detection = mp.solutions.face_detection
    face_detection = mp_face_detection.FaceDetection(min_detection_confidence=0.3)

    # Open a webcam
    cap = cv2.VideoCapture(0)  # 0 corresponds to the default camera (you may need to change this)

    # Set a timer for 3 seconds
    start_time = time.time()
    capture_time = 3  # in seconds

    while cap.isOpened():
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame.")
            break

        # Convert BGR to RGB
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Perform face detection
        results = face_detection.process(frame_rgb)

        # Draw bounding boxes around faces
        if results.detections:
            for detection in results.detections:
                bboxC = detection.location_data.relative_bounding_box
                ih, iw, _ = frame.shape
                bbox = int(bboxC.xmin * iw), int(bboxC.ymin * ih), \
                    int(bboxC.width * iw), int(bboxC.height * ih)
                cv2.rectangle(frame, bbox, (255, 0, 255), 2)

        # Display the frame with bounding boxes
        cv2.imshow('Face Detection', frame)

        # Check if 3 seconds have passed
        elapsed_time = time.time() - start_time
        if elapsed_time >= capture_time:
            # Release the webcam and close all OpenCV windows
            cap.release()
            cv2.destroyAllWindows()

            # Return the captured image
            return frame

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
