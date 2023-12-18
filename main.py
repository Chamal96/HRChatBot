from face_recognition import predict_emotion
from meadia_pipe import capture_image
from chat_bot import chat_bot

# Call the function to capture an image
captured_image = capture_image()

predicted_label = predict_emotion(captured_image)
# print(predicted_label)

bot = chat_bot(predicted_label)