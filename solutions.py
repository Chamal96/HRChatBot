import random


def calculate_stress(cumulative_score):
    pos = cumulative_score["pos"]
    neg = cumulative_score["neg"]
    neu = cumulative_score["neu"]

    # You can customize this function based on your specific requirements
    if int(neg) > 0.6:  # Adjust the threshold as needed
        stress_level = "High"
    elif int(neg) > 0.3:
        stress_level = "Moderate"
    else:
        stress_level = "Low"

    # Reset cumulative scores to 0.0
    cumulative_score['pos'] = 0.0
    cumulative_score['neg'] = 0.0
    cumulative_score['neu'] = 0.0

    return stress_level


def recommend_activity(stress_level):
    if stress_level == "High":
        return random.choice([
            "Get deep breathing exercises. Inhale slowly through your nose, allowing your belly to rise, and then exhale slowly through your mouth.",
            "Listen to calming music. Click here https://www.youtube.com/results?search_query=calm+music",
            "Take a short walk.",
            "Try progressive muscle relaxation. Start by tensing the muscles in your body, one group at a time, and then slowly release the tension while focusing on the sensation of relaxation."
            "Write down your thoughts in a journal to express and process your emotions.",
            "Consider talking to a friend or family member about what's on your mind.",
            "Practice progressive muscle relaxation techniques.",
            "Take a warm bath with soothing essential oils.",
            "Try visualization exercises to imagine yourself in a peaceful place.",
            "try taking deep breaths. Inhale slowly through your nose, allowing your belly to rise, and then exhale slowly through your mouth. Repeat this several times to help calm your mind and body."
        ])

    elif stress_level == "Moderate":
        return random.choice([
            "Read a book or listen to an audiobook. Click here https://www.youtube.com/results?search_query=audiobooks",
            "Do some light stretching.",
            "Practice mindfulness meditation.",
            "Engage in a creative activity, such as drawing or writing.",
            "Take a break to enjoy a cup of herbal tea.",
            "Go for a bike ride or a jog around your neighborhood.",
            "Attend a yoga class or follow a yoga tutorial online.",
            "Spend time with pets or animals, as they can help reduce stress levels.",
            "Practice deep breathing exercises for relaxation.",
            "Attend a support group or therapy session to discuss your stressors."
        ])

    else:
        return random.choice([
            "Enjoy a healthy snack.",
            "Watch a relaxing video. Click here https://www.youtube.com/results?search_query=Watch+a+relaxing+video",
            "Take a break and hydrate.",
            "Go for a walk in nature or spend time in a nearby park.",
            "Listen to a podcast or audio content on a topic that interests you.",
            "Practice gratitude by writing down things you're thankful for.",
            "Engage in a hobby or activity that brings you joy.",
            "Plan a day trip or outing to explore a new area.",
            "Spend quality time with friends or family members.",
            "Practice positive affirmations to boost your mood."
        ])
