def calculate_stress(cumulative_score):
    pos = cumulative_score["pos"]
    neg = cumulative_score["neg"]
    neu = cumulative_score["neu"]
    print(pos)
    print(neu)
    print(neg)

    # # You can customize this function based on your specific requirements
    # if neg > 0.6:  # Adjust the threshold as needed
    #     stress_level = "High"
    # elif neg > 0.3:
    #     stress_level = "Moderate"
    # else:
    #     stress_level = "Low"

    return stress_level

# Initialize cumulative sentiment scores as a dictionary
cumulative_scores = {
    'pos': 0.0,
    'neg': 0.0,
    'neu': 0.0
}
# Update cumulative sentiment scores
cumulative_scores['neg'] += 0.5

# Calculate stress level
stress_level = calculate_stress(cumulative_scores)
print("Stress Level:", stress_level)
