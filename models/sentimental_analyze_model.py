import pickle

with open("models/sentiment_analyzer.pkl", 'rb') as f:
    sid_loaded = pickle.load(f)

# Initialize cumulative sentiment scores as a dictionary
cumulative_scores = {
    'pos': 0.0,
    'neg': 0.0,
    'neu': 0.0
}


def sentimental_analyze(user_input_lower):
    # Calculate sentiment score
    sentiment_score = sid_loaded.polarity_scores(user_input_lower)

    # Update cumulative sentiment scores
    cumulative_scores['pos'] += sentiment_score['pos']
    cumulative_scores['neg'] += sentiment_score['neg']
    cumulative_scores['neu'] += sentiment_score['neu']

    # Print sentiment scores
    print(f"Sentiment Scores - Positive: {sentiment_score['pos']}, Negative: {sentiment_score['neg']}, Neutral: {sentiment_score['neu']}")

    return sentiment_score, cumulative_scores

