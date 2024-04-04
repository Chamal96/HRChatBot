from flask import Flask, request, jsonify
import json
from models.chatterbot_ import random_choice_chat, random_choice_chat_fix, chat_bot
from models.sentimental_analyze_model import sentimental_analyze
from solutions import calculate_stress, recommend_activity
from user_input import q_and_a

app = Flask(__name__)


def initial_chat_bot(predicted_label):
    # Simple conversation loop
    initial_response = f"Hi! I'm Amiga.🙂\nYou seem like {predicted_label}\nLet me ask some questions from you?"
    print(initial_response)
    return jsonify({'response': initial_response})  # Returning a JSON response


def process_chat(user_input, user_input_count, age):
    print(user_input_count)
    # Number of interactions to consider before calculating stress
    interactions_threshold = 10
    random_Q_count = 5

    # Convert to lowercase
    user_input_lower = user_input.lower()

    s, cumulative_scores = sentimental_analyze(user_input_lower)
    print(cumulative_scores)

    if user_input_count < random_Q_count:
        respons = random_choice_chat(age)
        print(respons)
        return jsonify({'response': respons})

    if user_input_count == random_Q_count:
        respons = random_choice_chat_fix()
        print(respons)
        return jsonify({'response': respons})

    # Check if it's time to calculate stress
    if user_input_count % interactions_threshold == 0:
        # Calculate stress level every `interactions_threshold` chats
        stress_level = calculate_stress(cumulative_scores)
        print(f"Stress Level after {user_input_count} chats: {stress_level}")

        # Provide recommendation after calculating stress level
        recommendation = recommend_activity(stress_level)
        response = f"Dear😊, what if you\n{recommendation}🫠"
        print(f"Dear what if you {recommendation}")
        q_and_a(response, user_input)
        return jsonify({'response': response})

    else:
        # Use the user input in the chatbot function
        response = chat_bot(age, user_input_lower)
        print(f"Amiga: {response}")
        q_and_a(response, user_input)
        return jsonify({'response': response})
