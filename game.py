#game.py

import os
import random

# Getting the load_dotenv() function and then invoking it
# The following two lines of code came from Professor Rossetti's slack message:
from dotenv import load_dotenv
load_dotenv()

USER_NAME = os.getenv("USER_NAME", default = "Player One")

# Print welcome message
print("-------------------")
print(f"Welcome {USER_NAME} to my Rock-Paper-Scissors game!")
print("-------------------")

# Asking the user for input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")
print(f"You chose: {user_choice}")

# Validate the user selection
options = ["rock", "paper", "scissors"]
if user_choice in options:
    pass
else:
# stop the program if the user choice is invalid
    print("User choice is not valid. Exiting program")
    exit()

# Computer's choice:
computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")



# Identifying who won
# If statements were adapted from Professor Rossetti's slack message

if user_choice == "rock":
    if computer_choice == "rock":
        print("It's a tie.")
    elif computer_choice == "paper":
        print("The computer won. Better luck next time!")
    elif computer_choice == "scissors":
        print("You won! Congrats.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("You won! Congrats.")
    elif computer_choice == "paper":
        print("It's a tie.")
    elif computer_choice == "scissors":
        print("The computer won. Better luck next time!")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("The computer won. Better luck next time!")
    elif computer_choice == "paper":
        print("You won! Congratss.")
    elif computer_choice == "scissors":
        print("It's a tie.")
else:
    print("SOMETHING IS WRONG.")


print("Thank you for playing. Please play again!")