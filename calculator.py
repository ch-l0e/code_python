# custom functions
def numericInput(prompt): # def defines numericInput, which creates a function
    while True:
        value = input(prompt)
        try:
            value = float(value) #f loat are decimal or fraction values
            return value
        except:
            print(f"{value} cannot be converted to a floating point") # the f will interpret {num1} as a variable and not a string
# end of numericInput
def menu():
    menu = """
Calculator Menu Options:
    1. add  (+)
    2. subtract (-)
    3. multiple (*)
    4. divide (/)
    5. exit program (Exit.)

""" # long form string
    while True:
        print(menu)
        user_choice = input("User's choice: ").lower() #puts everything lowercase
        if user_choice in {'add', '1', '+'}:
            return 1
        elif user_choice in {'subtract', '2', '-'}:
            return 2
        elif user_choice in {'multiple', '3', '*'}:
            return 3
        elif user_choice in {'divide', '4', '/'}:
            return 4
        elif user_choice in {'exit program', '5', 'Exit.'}:
            return 5
        else:
            print(f"{user_choice} is not a menu option")
# end of menu

# main part of program starts underneath:
while True:
    menu_result = menu()
    if menu_result != 5:
        num1 = numericInput("Enter a number: ")
        num2 = numericInput("Enter another number: ")
    menu_result = menu()
    answer = 0
    if menu_result == 1:
        answer = num1 + num2
        print(f"{num1} + {num2} = {answer}")
    elif menu_result == 2:
        answer = num1 - num2
        print(f"{num1} - {num2} = {answer}")
    elif menu_result == 3:
        answer = num1 * num2
        print(f"{num1} * {num2} = {answer}")
    elif menu_result == 4:
        try:
            answer = num1 / num2
            print(f"{num1} / {num2} = {answer}")
        except ZeroDivisionError:
            print(f"You cannot divide by zero. Please try different numbers.")
    elif menu_result == 5:
        print("Thank you for using our program calculator")
        break # exits the infinite loop