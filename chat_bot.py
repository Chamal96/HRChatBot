from flask import Flask, request, jsonify
import json
import pandas as pd
import random
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from stress_calculator import calculate_stress, recommend_activity

app = Flask(__name__)

analyzer = SentimentIntensityAnalyzer()
tfidf = TfidfVectorizer()
lemmatizer = WordNetLemmatizer()

# Define a dictionary to map age ranges to file paths
age_paths = {
    "18-28": 'data/chat/chat18-28.txt',
    "29-45": 'data/chat/chat29-45.txt',
    "46-55": 'data/chat/chat46-55.txt'
}

def chat_according_to_age(age):
    # Check if the age range is valid
    if age not in age_paths:
        return "Invalid age range"

    # Get the file path based on the age range
    path = age_paths[age]
    print(path)

    # Read the data from the file
    df = pd.read_csv(path, names=('Query', 'Response'), sep='=')

    # Apply sentiment analysis to the queries
    df['rating'] = df['Query'].apply(analyzer.polarity_scores)
    df = pd.concat([df.drop(['rating'], axis=1), df['rating'].apply(pd.Series)], axis=1)

    # Compute TF-IDF features
    factors = tfidf.fit_transform(df['Query']).toarray()

    return factors, df



def chatbot(query, age):
    factors, df = chat_according_to_age(age)
    # step:-1 clean
    query = lemmatizer.lemmatize(query)
    # step:-2 word embedding - transform
    query_vector = tfidf.transform([query]).toarray()
    # step-3: cosine similarity
    similar_score = 1 - cosine_distances(factors, query_vector)
    index = similar_score.argmax()  # take max index position
    # searching or matching question
    matching_question = df.loc[index]['Query']
    response = df.loc[index]['Response']
    pos_score = df.loc[index]['pos']
    neg_score = df.loc[index]['neg']
    neu_score = df.loc[index]['neu']
    confidence = similar_score[index][0]
    chat_dict = {'match': matching_question,
                 'reply': response,
                 'score': confidence,
                 'pos': pos_score,
                 'neg': neg_score,
                 'neu': neu_score}
    return chat_dict


def initial_chat_bot(predicted_label):
    # Simple conversation loop
    initial_response = f"Aurora: Hi! I'm Aurora. You seem like {predicted_label}. Tell me why is that!!!"
    print(initial_response)
    return jsonify({'response': initial_response})  # Returning a JSON response


def process_chat(user_input, user_input_count, age):
    print(user_input_count)
    # Load data from JSON file
    with open('data/chat/mental.json', 'r') as file:
        data1 = json.load(file)

    # Create a dictionary to map user inputs to lists of responses
    response_dict = {}
    for intent in data1['intents']:
        for pattern in intent['patterns']:
            response_dict[pattern.lower()] = intent['responses']

    # List of goodbye patterns
    goodbye_patterns = ["bye", "see you later", "goodbye", "au revoir", "sayonara", "ok bye", "bye then",
                        "fare thee well"]

    # Initialize cumulative negative sentiment score
    cumulative_neg_score = 0.0

    # Number of interactions to consider before calculating stress
    interactions_threshold = 5

    user_input_lower = user_input.lower()
    response = chatbot(user_input_lower, age)
    print(response)
    print(response['neg'])

    # # Update cumulative negative sentiment score
    cumulative_neg_score += response['neg']
    #
    print(f"Sentiment Scores - Positive: {response['pos']}, Negative: {response['neg']}, Neutral: {response['neu']}")

    # Check if it's time to calculate stress
    if user_input_count % interactions_threshold == 0:
        # Calculate stress level every `interactions_threshold` chats
        stress_level = calculate_stress(cumulative_neg_score)
        print(f"Stress Level (after {user_input_count} chats): {stress_level}")

        # Provide recommendation after calculating stress level
        recommendation = recommend_activity(stress_level)
        response = f"Aurora: Dear what if you {recommendation}"
        print(f"Aurora: Dear what if you {recommendation}")
        return jsonify({'response': response}, {'response': response})

    # Check if the user input is in the list of goodbye patterns
    if user_input_lower in goodbye_patterns:
        response_1 = f"Aurora: Goodbye! I hope we will meet again soon."
        print(response_1)
        return jsonify({'response': response_1})

    elif user_input_lower in response_dict:
        # If user input corresponds to the response dictionary, print a random response
        responses = response_dict[user_input_lower]
        response = random.choice(responses)
        print(f"Aurora: {response}")
        return jsonify({'response': response})

    else:
        # Use the user input in the chatbot function
        response = chatbot(user_input_lower, age)
        print(f"Aurora: {response}")
        return jsonify({'response': response})


