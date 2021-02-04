#game.py


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# asking the user for input

user_choice = input("Please choose either 'rock', 'paper', or 'scissors':")


# regular print
# print("You chose:", user_choice)

# String concatination
#print("You chose: " + user_choice)

#String interpolation / format string usage
print(f"You chose: {user_choice}")

options = ["rock", "paper", "scissors"]
# Validate the user selection
if user_choice in options:
    pass
else:
# stop the program if the user choice is invalid
    print("User choice is not valid. Exiting program")
    exit()

# computer's choice:

#computer_choice = "paper"

# Computer Choice Method 1
#import random
#computer_choice = ['rock', 'paper', 'scissors']

# Computer Choice Method 2
import random
computer_choice = random.choice(options)

print(f"The computer chose: {computer_choice}")




# identifying who won

if user_choice == "rock":
    if computer_choice == "rock":
        print("Oh, it's a tie.")
    elif computer_choice == "paper":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "scissors":
        print("Oh, you won! Nice job.")
elif user_choice == "paper":
    if computer_choice == "rock":
        print("Oh, you won! Nice job.")
    elif computer_choice == "paper":
        print("Oh, it's a tie.")
    elif computer_choice == "scissors":
        print("Oh, the computer won. It's ok.")
elif user_choice == "scissors":
    if computer_choice == "rock":
        print("Oh, the computer won. It's ok.")
    elif computer_choice == "paper":
        print("Oh, you won! Nice job.")
    elif computer_choice == "scissors":
        print("Oh, it's a tie.")
else:
    print("OOPS SOMETHING WENT WRONG.")

#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!

#print("Rock, Paper, Scissors, Shoot!")