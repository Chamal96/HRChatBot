from chat_bot import initial_chat_bot, process_chat
from flask import Flask, render_template, request, jsonify
from face_recognition import predict_emotion
from meadia_pipe import capture_image

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat_bot_one', methods=['POST'])
def chat_bot_one():
    print("Received a POST request.")

    # Capture an image
    captured_image = capture_image()
    print("Image captured.")

    # Predict emotion
    predicted_label = predict_emotion(captured_image)
    print(f"Predicted label: {predicted_label}")

    # Run the chatbot
    bot_response = initial_chat_bot(predicted_label)
    print(f"Bot response: {bot_response}")
    return bot_response


# Initialize a counter
user_input_count = 0


@app.route('/chat_bot_two', methods=['GET'])
def chat_bot_two():
    print("Received a POST request.")
    global user_input_count  # Access the global counter

    user_input = request.args.get('user_input', '')

    # Increment the user_input_count
    user_input_count += 1

    bot_response = process_chat(user_input, user_input_count)

    print(f"Bot response: {bot_response}")
    return bot_response


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
