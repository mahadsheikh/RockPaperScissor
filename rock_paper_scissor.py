import random

user_win = 0
comp_wins = 0
options = ["rock","paper","scissor"]

while True:
    user_input = input("Type Rock/Paper/Scissor or Q to quit  : ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        print("Invalid Option selected")
        continue
    else:
        pick = options[random.randint(0,2)] # 0 is rock 1 is paper and 2 is scissor
        print("Computer Picked = ",pick)
        if user_input.lower() == 'rock' and pick == "scissor":
            print("You Won")
            user_win += 1
        elif user_input.lower() == 'paper' and pick == "rock":
            print("You Won")
            user_win += 1
        elif user_input.lower() == 'scissor' and pick == "paper":
            print("You Won")
            user_win += 1
        else:
            print("You Lost")
            comp_wins += 1
print("You won ",user_win," times")
print("Computer won ",comp_wins," times")