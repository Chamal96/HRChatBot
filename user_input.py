# Initialize an empty dictionary
Q_and_A_dict = {}

bye_responses = [
    "See you later",
    "Have a nice day",
    "Bye! Come back again soon."
]


def q_and_a(bot_response, user_input):
    while True:
        if any(bot_response.lower() == response.lower() for response in bye_responses):
            print(f"Email has been sent to HR {Q_and_A_dict}")
            break
        else:
            Q_and_A_dict[bot_response] = user_input
            return
