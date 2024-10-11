def listmaking():
    user_input = input("Enter numbers, seperate with commas. : ")
    user_input = user_input.replace(' ', '')
    current = ""
    numbers = []
    #print(user_input)
    for i in user_input:
        #print(i)
        if i != ',':
            current = current + i
        if i == ',' or user_input.find(i) == len(user_input) - 1:
            current_int = int(current)
            numbers.append(current_int)
            current = ""
    print(numbers)

listmaking()