import pickle
import random
from scipy.spatial import distance
from sklearn.feature_extraction.text import CountVectorizer

# Define age paths and conversation starters
age_paths_initial = {
    "18-28": [
        "What's your daily routine like?",
        "What are some healthy habits you've incorporated into your lifestyle?",
        "How do you manage stress and maintain mental well-being during busy times?",
        "Have you set any health or wellness goals for yourself recently?",
        "How do you maintain a balanced diet despite a busy schedule?",
        "How do you ensure you get enough restful sleep?",
        "How do you feel about your current salary?",
        "What's your opinion on the level of transparency around salary and compensation in our workplace?",
        "Have you ever negotiated for a salary increase or additional benefits? How did it go?",
        "What factors do you consider when evaluating the competitiveness of your salary and benefits package?",
        "How do you feel about discussing salary and compensation with colleagues or peers?",
        "How do you approach asking for a raise or promotion in your current job?",
        "What are some of your biggest dreams or aspirations in life?",
        "How do you plan to pursue your dreams while managing other responsibilities?"
        "How did you and your partner meet?",
        "Have you and your partner been doing anything fun together lately?",
        "What do you value most in your relationships, whether it's with a partner, family, or friends?",
        "How do you navigate conflicts or disagreements in your relationships?",
        "Are there any relationship goals you're currently working towards?",
        "What are some of the key qualities you value in a partner or spouse?",
        "How has being married influenced your perspective on work-life balance and personal fulfillment?",
        "What are some challenges you've faced as a married individual in the workplace, and how have you overcome them?"
    ],
    "29-45": [
        # Salary
        "How do you feel about the issue of equal pay in our workplace?",
        "Do you feel that you are being paid fairly for the work you do compared to your male counterparts?",
        "Do you think it's fair for men and women to earn different salaries for doing the same job?",
        "Have you ever talked to your boss about how much you get paid?",

        # Family
        "How do you balance your work responsibilities with your family commitments?",
        "What challenges do you face in balancing your career and family life?",
        "Have you ever had to take time off work to care for a family member?",
        "What strategies do you use to manage family responsibilities during busy work periods?",
        "How do you manage to spend quality time with your family despite your busy work schedule?",
        "Have you ever had to adjust your work schedule to accommodate family needs?",

        # Health
        "How do you prioritize your health while managing work responsibilities?",
        "What are some ways you cope with stress in the workplace?",
        "How do you ensure you stay hydrated throughout the workday?",
        "What strategies do you use to incorporate physical activity into your daily routine?",
        "How do you maintain a balanced diet despite a busy work schedule?",
        "What do you do to ensure you get enough restful sleep at night?",
        "How do you manage to prioritize your mental health while at work?",
        "What preventive measures do you take to maintain your overall health and well-being?",

        # Investment
        "Do you currently have any investments or savings plans in place?",
        "How do you approach making investment decisions?",
        "What are some factors you consider when deciding where to invest your money?",
        "How do you balance investing for the future with other financial priorities?",
        "Have you ever faced challenges or setbacks with your investments, and how did you overcome them?",

        # Leisure
        "How do you like to unwind and relax after a busy day at work?",
        "What are some of your favorite hobbies or activities outside of work?",
        "How do you make time for leisure activities amidst your work and family responsibilities?",
        "Have you ever tried any new leisure activities or hobbies recently?",
        "How do leisure activities contribute to your overall well-being and work-life balance?",

        # Job Upgrade
        "Have you ever considered pursuing a job upgrade or advancing in your career?",
        "What factors would you consider when deciding whether to pursue a job upgrade?",
        "How do you plan to prepare yourself for a potential job upgrade or promotion?",
        "Have you ever faced challenges or obstacles in pursuing a job upgrade, and how did you overcome them?",
        "How do you envision your career progressing in the next few years?",
        "Have you ever received feedback or recognition that has motivated you to pursue a job upgrade?",
        "How do you handle the fear of failure or self-doubt when considering pursuing a job upgrade?"
    ],
    "46-55": [
        # Health and Wellness
        "How do you prioritize your health and well-being while managing work responsibilities?",
        "What strategies do you use to manage stress in the workplace?",
        "How do you ensure you maintain a balanced diet despite the demands of your job?",
        "What steps do you take to prioritize your mental health and well-being?",
        "How do you incorporate physical activity into your daily routine despite a busy work schedule?",

        # Technology
        "How comfortable are you with using technology in your daily work tasks?",
        "What are some specific ways technology has changed the way you work over the years?",
        "Have you ever faced challenges or frustrations when learning to use new technology at work?",
        "How do you stay updated on the latest technology trends and tools relevant to your field?",
        "What advice would you give to other employees in your age group who may feel intimidated by technology in the workplace?",

        # Children
        "Do you have children? (Yes/No)",
        "How do you balance your work responsibilities with your role as a parent?",
        "What challenges do you face as a working parent, and how do you overcome them?",
        "How has being a parent influenced your approach to work and your career choices?",
        "Have you ever had to take time off work to care for your children?",
        "What strategies do you use to stay connected with your children despite your busy work schedule?",

        # Salary
        "How satisfied are you with your current salary and compensation package?",
        "Have you ever negotiated for a salary increase or promotion in your current job?",
        "What strategies do you use to prepare for salary negotiations?",
        "What advice would you give to younger employees who are navigating salary negotiations in their careers?",
        "How do you feel about the transparency of salary and compensation within your organization?",
        "What factors do you think should be considered when determining salary and compensation for employees?",
        "Have you ever encountered challenges or obstacles related to salary or compensation in your career?"
    ]
}


# Define function to randomly choose a chat starter based on age
def random_choice_chat(age):
    if age in age_paths_initial:
        print(age)
        return random.choice(age_paths_initial[age])
    else:
        return "Age group not found in initial paths."


def random_choice_chat_fix():
    return "Well 🙂.  What is in your mind\nabout working place✍️, Salary💰, Personal life🫠, Health🏋️‍♂️ etc 👀"


import pandas as pd
import json
from sklearn.feature_extraction.text import CountVectorizer
from scipy.spatial import distance
import pickle


def open_file_according_to_age(age):
    print(age)
    # Load the dataset
    with open(f'data/chat/chat_{age}.json') as json_file:
        data = json.load(json_file)

    data = data['intents']

    # Convert the JSON data into a DataFrame
    rows = []
    for i in data:
        intent = i['intent']
        for t, r in zip(i['text'], i['responses']):
            row = {'intent': intent, 'text': t, 'response': r}
            rows.append(row)
    dataset = pd.DataFrame(rows)

    return dataset


# Define cosine distance function
def cosine_distance_countvectorizer_method(s1, s2):
    all_sentences = [s1, s2]
    vectorizer = CountVectorizer()
    all_sentences_to_vector = vectorizer.fit_transform(all_sentences)
    text_to_vector_v1 = all_sentences_to_vector.toarray()[0].tolist()
    text_to_vector_v2 = all_sentences_to_vector.toarray()[1].tolist()
    cosine = distance.cosine(text_to_vector_v1, text_to_vector_v2)
    return round((1 - cosine), 2)


# Function to respond to user input
def chat_bot(age, text):
    dataset = open_file_according_to_age(age)
    maximum = float('-inf')
    response = ""
    closest = ""
    for i in dataset.iterrows():
        sim = cosine_distance_countvectorizer_method(text, i[1]['text'])
        if sim > maximum:
            maximum = sim
            response = i[1]['response']
            closest = i[1]['text']
    return response
