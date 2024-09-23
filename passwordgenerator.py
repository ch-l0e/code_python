# Goal: create password generator
# requires password length
# requires password creteria
# does it contain uppercase characters?
# does it include numbers?
# does it contain special characters?
# generate password with given constraints
# output the generated password

import random

print("Welcome to password generator.")

#set password length
pswd_length = int(input("Enter the length of the password: "))

#password criteria
lowercase = list(range(97, 123)) #numbers from ascii table
uppercase = list(range(65, 91)) #range does not include last value
digits = list(range(48, 58))
special = list(range(33, 48)) + list(range(58, 65)) + list(range(91, 97)) + list(range(123, 127))

pswd_symbols = lowercase.copy() #list of possible characters for password

#contain uppercase?
has_upper = input("Include uppercase characters? (y/n): ")
if has_upper == 'Y' or has_upper == 'y':
    pswd_symbols.extend(uppercase) #OR pswd_symbols = pswd_symbols + uppercase

#contain numbers?
has_number = input("Include numbers? (y/n): ")
if has_number == 'Y' or has_number == 'y':
    pswd_symbols.extend(digits)

#contain special characters?
has_special = input("Include special characters? (y/n): ")
if has_special == 'Y' or has_special == 'y':
    pswd_symbols.extend(special)

#generate password
new_password = ""
while len(new_password) != pswd_length:
    random_symbol = chr(random.choice(pswd_symbols)) #chr converts numbers from ascii table to their actual characters
    new_password = new_password + random_symbol
#end of while loop

print(f"{new_password} has been generated.")