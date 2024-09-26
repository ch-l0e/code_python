from random import choice
options = ["rock", "paper", "scissors"]
player1 = choice(options)
player2 = choice(options)
print(f"Player 1: {player1}")
print(f"Player 2: {player2}")
if player1 == player2:
    print("Tie game.")
elif player1 == "rock":
    if player2 == "paper":
        print("Player 2 wins.")
    else:
        print("Player 1 wins.")
elif player1 == "paper":
    if player2 == "rock":
        print("Plater 1 wins.")
    else:
        print("Player 2 wins.")
elif player1 == "scissors":
    if player2 == "rock":
        print("Player 2 wins.")
    else:
        print("Player 1 wins.")