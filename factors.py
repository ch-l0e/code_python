def factor(n, k):
    factors = []
    for i in range (1, n + 1):
        if n % i == 0:
            factors.append(i)
    if len(factors) <= k-1:
        return -1
    else:
        return factors[k-1]

num = int(input("Enter value of n: "))
location = int(input("Enter value of k: "))
print(factor(num, location))