## Tiina Ylimäki

import random
import GameEngine

user_action = input("Choose (rock, paper, scissors): ")
possible_actions = ["rock", "paper", "scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")

print (GameEngine.GameAction (user_action, computer_action))