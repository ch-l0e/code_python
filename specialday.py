month = int(input("Enter month as numerical value: "))
day = int(input("Enter day as a numerical value: "))

if month < 2:
    print("Before")
elif month > 2:
    print("After")
else:
    if day < 18:
        print("Before")
    elif day > 18:
        print("After")
    else:
        print("Special")