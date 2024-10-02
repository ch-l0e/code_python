name = ""
length = 0
longest_name = ""

while name != 'x':
    name = input("Enter a name. Press x to exit. : ").lower()
    current_length = len(name)
    if current_length > length:
        length = current_length
        longest_name = name

print(f"the longest name is: {longest_name}")