def consonantCounter(prompt):
    vowels = "bcdfghjklmnpqrstvwxyz"
    counter = 0
    user_input = input(prompt)
    for i in user_input:
        if vowels.find(i) != -1:
            counter += 1
    return counter

num_consonant = consonantCounter("Enter a string: ")
print(f"The number of consonants are: {num_consonant}")