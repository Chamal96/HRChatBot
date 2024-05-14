import base64

from keras.preprocessing.image import img_to_array
import cv2 # OpenCV
import numpy as np
from tensorflow.keras.models import model_from_json

model = model_from_json(open("models/model.json", "r").read())
model.load_weights('models/best_model.h5')
face_haar_cascade = cv2.CascadeClassifier('models/haarcascade_frontalface_default.xml')


# image_path = "../depositphotos_192398186-stock-photo-beautiful-angry-woman-makeup-white.jpg"


def predict_emotion(captured_image_base64):
    captured_image_bytes = base64.b64decode(captured_image_base64)
    nparr = np.frombuffer(captured_image_bytes, np.uint8)
    captured_image = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    gray_image = cv2.cvtColor(captured_image, cv2.COLOR_BGR2GRAY)
    faces_detected = face_haar_cascade.detectMultiScale(gray_image)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(captured_image, (x, y), (x + w, y + h), (255, 0, 0), 2)

        roi_gray = gray_image[y:y + h, x:x + w]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        image_pixels = img_to_array(roi_gray)
        image_pixels = np.expand_dims(image_pixels, axis=0)

        predictions = model.predict(image_pixels)
        max_index = np.argmax(predictions[0])

        emotion_detection = ('angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral')
        emotion_prediction = emotion_detection[max_index]
        print(emotion_prediction)

        cv2.putText(captured_image, emotion_prediction, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0),
                    2)

    # resize_image = cv2.resize(captured_image, (1000, 700))
    # cv2.imshow('Emotion Detector', resize_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    return emotion_prediction
