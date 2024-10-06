def consonantCounter(prompt):
    consonants = "bcdfghjklmnpqrstvwxyz"
    counter = 0
    user_input = input(prompt).lower()
    for i in user_input:
        if consonants.find(i) != -1:
            counter += 1
    return counter

def vowelCounter(prompt):
    vowels = "aeiou"
    counter = 0
    user_input = input(prompt).lower()
    for i in user_input:
        if vowels.find(i) != -1:
            counter += 1
    return counter

while True:
    user_choice = input("Enter 'c' to pick consonants and 'v' to pick vowels: ").lower()
    if user_choice == "c":
        num_consonant = consonantCounter("Enter a string: ")
        print(f"The number of consonants in the string is: {num_consonant}")
        break
    elif user_choice == "v":
        num_vowel = vowelCounter("Enter a string: ")
        print(f"The number of consonants in the string is: {num_vowel}")
        break
    else:
        print("Invalid input. Please try again.")