import time
import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import load_model
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input


def preprocess_image_for_mobilenet_v2(image):
    # Ensure the image is in the range [0, 255]
    image = np.clip(image, 0, 255).astype(np.uint8)

    # Convert the NumPy array to PIL Image
    pil_image = Image.fromarray(image)

    # Resize the image to the required input size for MobileNetV2 (e.g., 224x224)
    pil_image = pil_image.resize((96, 96))

    # Convert the PIL Image to a NumPy array
    img_array = np.array(pil_image)

    # Preprocess the image for MobileNetV2 model
    img_array = preprocess_input(img_array)

    return img_array


label_to_text = {0: 'Surprise', 1: 'Fear', 2: 'Angry', 3: 'Neutral', 4: 'Sad', 5: 'Disgust', 6: 'Happy'}


def predict_emotion(captured_image):
    # Load your trained model (replace 'YourModel.h5' with your actual model file)
    model = load_model('my_model.h5')

    # Preprocess the image for prediction
    image = preprocess_image_for_mobilenet_v2(
        captured_image)  # You can use the previously defined preprocessing function

    # Make predictions using the model
    prediction = model.predict(np.expand_dims(image, axis=0))

    # Get the predicted label
    predicted_label = label_to_text[np.argmax(prediction)]

    # Display the image
    plt.imshow(image)
    plt.axis('off')
    plt.show()

    # Output predicted label
    print(f"Predicted: {predicted_label}")
    display_time = 3

    # Wait for a few seconds before clearing the output
    time.sleep(display_time)
    plt.close('all')  # Close the plot to clear the output

    return predicted_label
