def calculate_stress(neg_score):
    # You can customize this function based on your specific requirements
    if neg_score > 0.5:  # Adjust the threshold as needed
        stress_level = "High"
    elif neg_score > 0.3:
        stress_level = "Moderate"
    else:
        stress_level = "Low"

    return stress_level


# Sample usage
neg_score = 0.6  # Replace this with the actual negative sentiment score
stress_level = calculate_stress(neg_score)
print(f"Stress Level: {stress_level}")
