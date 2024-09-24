def nameInput(prompt):
    name = input(prompt)
    return name

def yearInput(prompt):
    while True:
        year = input(prompt)
        try:
            year = int(year)
            return year
        except:
            print("Invalid input. Please try again.")

first_name = nameInput("Enter your first name: ")
last_name = nameInput("Enter your last name: ")
birth_year = yearInput("Enter your birth year: ")
current_year = yearInput("Enter the current year: ")
age = current_year - birth_year
print(f"Hello {first_name} {last_name}! You are {age} year(s) old!")
if age < 18:
    print("you are a child.")
elif age >= 18 and age <60:
    print("you are an adult")
else:
    print("you are old.")