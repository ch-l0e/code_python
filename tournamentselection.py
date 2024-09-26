while True:
    result = input("Enter all game results. Enter 'W' for win and 'L' for loss. ").upper()
    if len(result) != 6:
        print("Error. Please enter six game results.")
    else:
        break
win = 0
loss = 0
for current_game in result:
    if current_game == 'W':
        win += 1
    elif current_game == 'L':
        loss += 1
    else:
        print(f"{current_game} is an invalid input. Moving on.")
print(f"Wins: {win} Losses: {loss}")
if win > 4:
    print("Player is in group 1.")
elif win > 2 and win < 5:
    print("Player is in group 2.")
elif win > 0 and win < 3:
    print("Player is in group 3.")
else:
    print("Player is disqualified.")