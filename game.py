#game.py


print("-------------------")
print("Welcome 'Player One' to my Rock-Paper-Scissors game...")
print("-------------------")

# asking the user for input

x = input("Please choose either 'rock', 'paper', or 'scissors':")

print(x)

# regular print
print("You chose: ", x)

# String concatination
print("You chose: " + x)

#String interpolation / format string usage
print(f"You chose: {x}")

exit()

#You chose: 'rock'
#The computer chose: 'paper'
#-------------------
#Oh, the computer won. It's ok.
#-------------------
#Thanks for playing. Please play again!

#print("Rock, Paper, Scissors, Shoot!")