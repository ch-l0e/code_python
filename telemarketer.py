def lastDigits(prompt):
    while True:
        number = input(prompt)
        if len(number) == 1:
            try:
                number = int(number)
                return number
            except:
                print("Invalid input. Please try again.")
        else:
            print("Invalid input. Please try again.")

num1 = lastDigits("Enter the first digit of the last four digits: ")
num2 = lastDigits("Enter the second digit of the last four digits: ")
num3 = lastDigits("Enter the third digit of the last four digits: ")
num4 = lastDigits("Enter the fourth digit of the last four digits: ")

if num1 == 9 or num1 == 8:
    if num4 == 9 or num4 == 8:
        if num2 == num3:
            print("ignore")
        else:
            print("answer")
    else:
        print("answer")
else:
    print("answer")