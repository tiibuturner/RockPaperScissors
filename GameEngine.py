## Tiina Ylimäki

def GameAction (user_action, computer_action):
    if user_action == computer_action:
        print(f"Both chose {user_action}. It is a tie!")
        return "It is a tie!"
    elif user_action == "rock":
        if computer_action == "scissors":
            return "Rock beats scissors. You won!"
        else:
            return "Paper beats rock. You lost!"
    elif user_action == "paper":
        if computer_action == "rock":
            return "Paper beats rock. You won!"
        else:
            return "Scissors beats paper. You lost!"
    elif user_action == "scissors":
        if computer_action == "paper":
            return "Scissors beats paper. You won!"
        else:
            return "Rock beats scissors. You lost!"
