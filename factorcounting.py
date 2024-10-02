#Problem: Determine number of factors of each number from 1 to N

def is_divisable(num1, num2): #blue text is the parameter - what needs to pass through to make it work
    '''checks if num1 is divisable by num2
    Args:
        num1 --> an integer, the numerator
        num2 --> integer, denominator
    Returns:
        true if num1 is divisable by num2, otherwise false
    '''
    return num1 % num2 == 0

def factor_count(number): 
    '''determine the  number of factors the number has.
    Args:
        number = integer needed to determine number of factors.

    Returns:
        an integer, which is the total abount of factors the arguement has
    ''' #docs string --> document what the code does

    counter = 0

    for divider in range(1, number + 1):
        #if number % divider == 0:
        if is_divisable(number, divider):
            counter += 1
    
    return counter

upper_limit = int(input("Enter value of 'n' : "))

for num in range(1, upper_limit + 1):
    factor_size = factor_count(num)
    print(f"{num} has {factor_size} factors.")