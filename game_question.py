from solutions import recommend_activity
import json


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
    recommendation = {
        "stress_level": stress_level,
        "mode": mode,
        "activity": activity
    }
    return json.dumps(recommendation)
