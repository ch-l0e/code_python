from random import randrange

while True:
    difficulty = input("Enter the DC: ")
    try:
        difficulty = int(difficulty)
        break
    except:
        print(f"{difficulty} was not a valid input. Please enter an integer")
player_roll = randrange(1, 21) #randrange(a, b) never includs b

print(f"The player rolled {player_roll} on their D20")

if player_roll >= difficulty:
    print(f"Player's roll was successful as the roll was greater than the difficulty.")
else:
    print(f"Player's roll was unsuccessful as the roll was less than the difficulty.")