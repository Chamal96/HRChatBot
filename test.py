# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.naive_bayes import MultinomialNB
# from sklearn.pipeline import make_pipeline
#
# # Sample data for training
# training_data = [
#     ("What is your name?", "intro"),
#     ("How are you?", "greeting"),
#     ("Tell me a joke", "humor"),
#     ("What is the capital of France?", "geography"),
#     # Add more examples based on your use case
# ]
#
#
# # Tokenization and stemming
# def process_text(text):
#     tokens = word_tokenize(text)
#     stemmer = PorterStemmer()
#     stemmed_tokens = [stemmer.stem(token.lower()) for token in tokens]
#     return " ".join(stemmed_tokens)
#
#
# # Prepare training data
# X_train = [process_text(text) for text, intent in training_data]
# y_train = [intent for text, intent in training_data]
#
# # Create a pipeline with TF-IDF vectorizer and Naive Bayes classifier
# model = make_pipeline(TfidfVectorizer(), MultinomialNB())
# model.fit(X_train, y_train)
#
#
# # Function to predict intent
# def predict_intent(text):
#     processed_text = process_text(text)
#     intent = model.predict([processed_text])[0]
#     return intent
#
#
# def chat_bot():
#     # Simple conversation loop
#     print("Chatbot: Hi! I'm your chatbot. Ask me anything or say goodbye to exit.")
#
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "goodbye":
#             print("Chatbot: Goodbye! Have a great day.")
#             break
#
#         intent = predict_intent(user_input)
#         print(f"Chatbot: Intent - {intent}")
