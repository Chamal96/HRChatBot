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
        return random.choice(["Try deep breathing exercises.", "Listen to calming music.", "Take a short walk."])
    elif stress_level == "Moderate":
        return random.choice(
            ["Read a book or listen to an audiobook.", "Do some light stretching.", "Practice mindfulness meditation."])
    else:
        return random.choice(["Enjoy a healthy snack.", "Watch a relaxing video.", "Take a break and hydrate."])
