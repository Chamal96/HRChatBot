from solutions import recommend_activity


def stress_by_questions(score):
    if score < 25:
        stress_level = "Low"
        mode = "Nice 😍"
    elif score < 50:
        stress_level = "Moderate"
        mode = "Pretty Good 🙂"
    else:
        stress_level = "High"
        mode = "So Stressful 👀"

    activity = recommend_activity(stress_level)
    recommendation = f"You looked {mode} dear, what if you try {activity}"
    return recommendation
