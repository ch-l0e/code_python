def string_cleaner(prompt):
    user_input = input(prompt)
    clean_string = ""
    for i in user_input:
        if i.isalpha():
            clean_string = clean_string + i
    return clean_string # only in function

# user_input = input("Enter a string: ")
# clean_string = ""
# for i in user_input:
#     if (ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122):
#         clean_string = clean_string + i
#     #print(ord(i))

print(string_cleaner("Enter a string: "))