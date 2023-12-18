# def calculate_stress(neg_score):
#     # You can customize this function based on your specific requirements
#     if neg_score > 0.5:  # Adjust the threshold as needed
#         stress_level = "High"
#     elif neg_score > 0.3:
#         stress_level = "Moderate"
#     else:
#         stress_level = "Low"
#
#     return stress_level
#
#
# # Sample usage
# neg_score = 0.6  # Replace this with the actual negative sentiment score
# stress_level = calculate_stress(neg_score)
# print(f"Stress Level: {stress_level}")


from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
df = pd.read_csv("data/Stress.csv")
not_used_cols = ['subreddit','post_id','sentence_range','confidence','social_timestamp']
df1 = df.drop(not_used_cols,axis=1)
df1.sample(3)
MIN_DF = 1
tf = TfidfVectorizer(min_df=MIN_DF)
tf_df = tf.fit_transform(df1['processed_text'])
tf_df = pd.DataFrame(tf_df.toarray(),columns=tf.get_feature_names_out())
model = LogisticRegression().fit(tf_df,df1['label'])

model.score(tf_df,df1['label'])
def predictor(text):
    # processed = textPocess(text)
    embedded_words = tf.transform([text])
    res = model.predict(embedded_words)
    if res[0] == 1:
        res = "this person is in stress"
    else:
        res = "this person is not in stress"
    return res