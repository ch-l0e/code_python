def create_line(num):
    """
    Arguement:
        num = integer above zero

    Return:
        series of 1 and 0 depending on the line
    """
    pattern = ""
    for i in range (1, num + 1):
        if i % 2 == 1:
            pattern = pattern + "1"
        else:
            pattern = pattern + "0"
    return pattern

def pattern_output(num):
    for i in range (1, num + 1):
        print(create_line(i)) 

print(pattern_output(5))