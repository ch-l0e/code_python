while True:
    num = int(input("Enter a number between 1 and 50: "))
    if num < 1 or num > 50:
        print("Number out of range. please try again.")
    else:
        break

if num % 3 == 0 and num % 5 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
else:
    print(num)