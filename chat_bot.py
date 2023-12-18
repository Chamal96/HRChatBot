import json
import pandas as pd
import random
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_distances

from nltk.sentiment.vader import SentimentIntensityAnalyzer

analyzer = SentimentIntensityAnalyzer()
df = pd.read_csv('data/chat.txt', names=('Query', 'Response'), sep=('\t'))
Text = df['Query']
df['rating'] = Text.apply(analyzer.polarity_scores)
df = pd.concat([df.drop(['rating'], axis=1), df['rating'].apply(pd.Series)], axis=1)

tfidf = TfidfVectorizer()
lemmatizer = WordNetLemmatizer()
factors = tfidf.fit_transform(df['Query']).toarray()


def chatbot(query):
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
                 'response': response,
                 'score': confidence,
                 'pos': pos_score,
                 'neg': neg_score,
                 'neu': neu_score}
    return response, pos_score, neg_score, neu_score


def chat_bot(predicted_label):
    # Load data from JSON file
    with open('mental.json', 'r') as file:
        data = json.load(file)

    # Create a dictionary to map user inputs to lists of responses
    response_dict = {}
    for intent in data['intents']:
        for pattern in intent['patterns']:
            response_dict[pattern.lower()] = intent['responses']

    # List of goodbye patterns
    goodbye_patterns = ["bye", "see you later", "goodbye", "au revoir", "sayonara", "ok bye", "bye then",
                        "fare thee well"]

    # Simple conversation loop
    print(f"Aurora: Hi! I'm Aurora. You seems like {predicted_label}. Tell me why is that!!!")

    while True:
        user_input = input("You: ")
        user_input_lower = user_input.lower()
        response, pos_score, neg_score, neu_score = chatbot(user_input_lower)
        print(f"Sentiment Scores - Positive: {pos_score}, Negative: {neg_score}, Neutral: {neu_score}")

        # Check if the user input is in the list of goodbye patterns
        if user_input_lower in goodbye_patterns:
            print("Aurora: Goodbye! I hope we will meet again soon.")
            break
        elif user_input_lower in response_dict:
            # If user input corresponds to the response dictionary, print a random response
            responses = response_dict[user_input_lower]
            response = random.choice(responses)
            print(f"Aurora: {response}")
        else:
            # Use the user input in the chatbot function
            response, pos_score, neg_score, neu_score = chatbot(user_input_lower)
            print(f"Aurora: {response}")
