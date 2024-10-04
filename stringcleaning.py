user_input = input("Enter a string: ")
clean_string = ""
for i in user_input:
    if (ord(i) >= 65 and ord(i) <= 90 or ord(i) >= 97 and ord(i) <= 122):
        clean_string = clean_string + i
    #print(ord(i))

print(clean_string)