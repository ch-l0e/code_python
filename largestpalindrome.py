def palindrome(num):
    return str(num) == str(num)[::-1]

def product():
    num = 0
    current = 0
    for i in range (999, 99, -1):
        for j in range (999, 99, -1):
            num = i*j
            if palindrome(num) and num > current:
                current = num
    return current

print(product())