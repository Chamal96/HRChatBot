import random


def calculate_stress(cumulative_neg_score):
    # You can customize this function based on your specific requirements
    if cumulative_neg_score > 0.6:  # Adjust the threshold as needed
        stress_level = "High"
    elif cumulative_neg_score > 0.3:
        stress_level = "Moderate"
    else:
        stress_level = "Low"
    return stress_level


def recommend_activity(stress_level):
    if stress_level == "High":
        return random.choice([
            "Try deep breathing exercises.",
            "Listen to calming music. Click here https://www.youtube.com/results?search_query=calm+music",
            "Take a short walk.",
            "Write down your thoughts in a journal to express and process your emotions.",
            "Consider talking to a friend or family member about what's on your mind."
        ])

    elif stress_level == "Moderate":
        return random.choice([
            "Read a book or listen to an audiobook. Click here https://www.youtube.com/results?search_query=audiobooks",
            "Do some light stretching.",
            "Practice mindfulness meditation.",
            "Engage in a creative activity, such as drawing or writing.",
            "Take a break to enjoy a cup of herbal tea."
        ])

    else:
        return random.choice([
            "Enjoy a healthy snack.",
            "Watch a relaxing video. Click here https://www.youtube.com/results?search_query=Watch+a+relaxing+video",
            "Take a break and hydrate.",
            "Go for a walk in nature or spend time in a nearby park.",
            "Listen to a podcast or audio content on a topic that interests you."
        ])
