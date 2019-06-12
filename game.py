# game.py

print("Rock, Paper, Scissors, Shoot!")

# CAPTURE INPUTS
user_choice = input("Please select one of the following options: ROCK, PAPER, or SCISSORS")
     
print("YOUR CHOICE IS: " + user_choice)

# VALIDATE INPUTS



if user_choice in ["ROCK", "PAPER", "SCISSORS"]:
    print("VALID")
else:
    print("INVALID SELECTION, PLEASE TRY AGAIN")
    exit()


# GENERATE COMPUTER SELECTION

print("GENERATING...")

# DETERMINE THE WINNER

# DISPLAY FINAL OUTPUTS / OUTCOMES