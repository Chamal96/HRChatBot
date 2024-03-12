from chat_bot import initial_chat_bot, process_chat
from flask import Flask, render_template, request
from face_recognition import predict_emotion
from game_question import stress_by_questions
from meadia_pipe import capture_image
from models.chatterbot_ import chat_bot
import base64
import io
from PIL import Image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat_bot_one', methods=['POST'])
def chat_bot_one():
    try:
        print("Received a POST request.")
        # # Get the JSON body from the request
        json_data = request.json
        print(json_data["image"])
        base64_image = json_data["image"]

        # Decode base64 string into bytes
        # image_bytes = base64.b64decode(base64_image)

        # # Open bytes as an image
        # captured_image = Image.open(io.BytesIO(image_bytes))
        # # Convert the image to RGB mode if it has an alpha channel
        # if captured_image.mode == 'RGBA':
        #     captured_image = captured_image.convert('RGB')

        # Display image
        # captured_image.show()

        # # Capture an image
        # captured_image = capture_image(image)
        # print("Image captured.")

        # Predict emotion
        predicted_label = predict_emotion(base64_image)
        print(f"Predicted label: {predicted_label}")

        # Run the chatbot
        bot_response = initial_chat_bot(predicted_label)
        print(f"Bot response: {bot_response}")

        return bot_response
    except Exception as e:
        # Handle any other exceptions not caught by specific except blocks
        print("An error occurred:", e)


# Initialize a counter
user_input_count = 0


@app.route('/chat_bot_two', methods=['GET'])
def chat_bot_two():
    print("Received a GET request.")
    global user_input_count  # Access the global counter

    user_input = request.args.get('user_input', '')
    user_age = request.args.get('age', '')

    # Increment the user_input_count
    user_input_count += 1

    # bot_response = chat_bot(user_age, user_input)
    bot_response = process_chat(user_input, user_input_count, user_age)

    print(f"Bot response: {bot_response}")
    return bot_response


@app.route('/after_question', methods=['GET'])
def after_question():
    print("Received a GET request.")
    # global user_input_count  # Access the global counter

    user_input = int(request.args.get('score', ''))
    # user_age = request.args.get('age', '')

    # Increment the user_input_count
    # user_input_count += 1
    activity = stress_by_questions(user_input)
    # bot_response = process_chat(user_input, user_input_count, user_age)

    print(f"Bot response: {activity}")
    return activity


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
