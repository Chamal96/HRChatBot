# import time
# import numpy as np
# import matplotlib.pyplot as plt
# from tensorflow.keras.models import load_model
# from PIL import Image
# from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
#
#
# def preprocess_image_for_mobilenet_v2(image):
#     # Ensure the image is in the range [0, 255]
#     image = np.clip(image, 0, 255).astype(np.uint8)
#
#     # Convert the NumPy array to PIL Image
#     pil_image = Image.fromarray(image)
#
#     # Resize the image to the required input size for MobileNetV2 (e.g., 224x224)
#     pil_image = pil_image.resize((96, 96))
#
#     # Convert the PIL Image to a NumPy array
#     img_array = np.array(pil_image)
#
#     # Preprocess the image for MobileNetV2 model
#     img_array = preprocess_input(img_array)
#
#     return img_array
#
#
# # label_to_text = {0: 'Surprise', 1: 'Fear', 2: 'Angry', 3: 'Neutral', 4: 'Sad', 5: 'Disgust', 6: 'Happy'}
# label_to_text = {5:'Surprise', 1:'Fear', 0:'Angry', 3:'Neutral', 4: 'Sad', 2: 'Happy'}
#
#
# def predict_emotion(captured_image):
#     # Load your trained model (replace 'YourModel.h5' with your actual model file)
#     model = load_model('models/best_model.h5')
#     # model = load_model('models/my_model.h5')
#
#     # Preprocess the image for prediction
#     image = preprocess_image_for_mobilenet_v2(
#         captured_image)  # You can use the previously defined preprocessing function
#
#     # Make predictions using the model
#     prediction = model.predict(np.expand_dims(image, axis=0))
#
#     # Get the predicted label
#     predicted_label = label_to_text[np.argmax(prediction)]
#
#     # Display the image
#     plt.imshow(image)
#     plt.axis('off')
#     plt.show()
#
#     # Output predicted label
#     print(f"Predicted: {predicted_label}")
#     display_time = 3
#
#     # Wait for a few seconds before clearing the output
#     time.sleep(display_time)
#     plt.close('all')  # Close the plot to clear the output
#
#     return predicted_label
import base64

from keras.preprocessing.image import img_to_array
import cv2
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
