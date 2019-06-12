# game.py

import random


print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS
user_choice = input("Please select one of the following options: ROCK, PAPER, or SCISSORS")
     
print("YOUR CHOICE IS: " + user_choice)

# VALIDATE INPUTS



if user_choice not in ["ROCK", "PAPER", "SCISSORS"]:
    print("INVALID SELECTION, PLEASE TRY AGAIN")
    exit()


# GENERATE COMPUTER SELECTION

computer_choice = random.choice(["ROCK", "PAPER", "SCISSORS"])

print("COMPUTER CHOICE: " + computer_choice)

# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES