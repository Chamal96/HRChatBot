# # Question and answer
# q = "What is the longest river in Sri Lanka?"
# a = {"a": "Mahaweli",
#      "b": "Walawe",
#      "c": "Nilwala"}
#
# # Correct answer
# correct_answer = "a"
#
# # Marks mapping
# marks_mapping = {"a": 5,  # Assign 5 marks for the correct answer
#                  "b": 0,  # Assign 0 marks for the incorrect answers
#                  "c": 0}
#
# # Get the user's selection (assuming the user's selection is stored in a variable called user_selection)
# user_selection = input("Your answer (a, b, c): ")
#
# # Check if the user's selection is correct and assign marks accordingly
# if user_selection == correct_answer:
#     marks = marks_mapping[user_selection]
#     print(f"Correct! You earned {marks} marks.")
# else:
#     print("Incorrect. You earned 0 marks.")

# List of questions and answers
questions = [
    {
        "question": "What is the longest river in Sri Lanka?",
        "options": {"a": "Mahaweli", "b": "Walawe", "c": "Nilwala"},
        "correct_answer": "a"
    },
    {
        "question": "Which is the capital city of France?",
        "options": {"a": "Berlin", "b": "Madrid", "c": "Paris"},
        "correct_answer": "c"
    },
    {
        "question": "Which is the capital city of Sri Lanka?",
        "options": {"a": "Kotte", "b": "Colombo", "c": "Badulla"},
        "correct_answer": "a"
    }
]

# Initialize total marks
total_marks = 0

# Iterate through each question
for i, question in enumerate(questions, start=1):
    print(f"\nQuestion {i}: {question['question']}")
    print("Options:")
    for option, answer in question['options'].items():
        print(f"{option}: {answer}")

    # Get user's selection
    user_selection = input("Your answer (a, b, c): ")

    # Check if the user's selection is correct and update total marks
    if user_selection == question['correct_answer']:
        total_marks += 5  # Adjust the marks as needed
        print("Correct! You earned 5 marks.")
    else:
        print("Incorrect. You earned 0 marks for this question.")

# Display total marks
print(f"\nTotal Marks: {total_marks}")
