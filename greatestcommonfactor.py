def greatfactor(int1, int2):
    for i in range (min(int1, int2), 0, -1):
        if int1 % i == 0 and int2 % i == 0:
            return i

x = int(input("Enter first int: "))
y = int(input("Enter second int: "))
print(greatfactor(x, y))

def gcf(int1, int2):
    def helper(x, y, div):
        if div == 1:
            return div
        elif x % == 0 and y % div == 0:
            return div
        else:
            return helper(x, y, div - 1)
    return helper(num1, num2, min(num1, num2))