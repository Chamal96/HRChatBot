def calculate_stress(cumulative_neg_score):
    # You can customize this function based on your specific requirements
    if cumulative_neg_score > 0.5:  # Adjust the threshold as needed
        stress_level = "High"
    elif cumulative_neg_score > 0.3:
        stress_level = "Moderate"
    else:
        stress_level = "Low"

    return stress_level


# # Simulate multiple chat interactions
#



