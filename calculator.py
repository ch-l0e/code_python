# 1. obatain two numbers
# 2. obtain choice of adding. subtracting, multiplying or dividing
# 3. do the wanted calculation with the given numbers
# 4. output the calculation/result

print("Welcome to our calculator app")

# 1. obtaining the numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# 2. obtain a way to choose add, mutiple, divide, subtract
choice = input("Choose either add, multiple, subtract or divide: ")

# 3. completing the wanted calculation
# 4. output the calculation
if choice == "add":
    print(num1 + num2)
elif choice == "subtract":
    print(num1 - num2)
elif choice == "multiple":
    print(num1 * num2)
elif choice == "divide":
    print(num1 / num2)
else:
    print("Invalid operation.")