total = 0
counter = 0

while True:
    user_input = input("Enter grade. Enter 'exit' to exit : ").lower()
    if user_input == "exit":
        break
    try:
        user_input = int(user_input)
        total += user_input
        counter += 1
    except:
        print("Invalid input. moving on.")

average = total / counter

print(f"Your average is: {average}")