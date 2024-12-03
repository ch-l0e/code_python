def power(base, expnt):
    if expnt == 0:
        return 1
    elif expnt == 1:
        return base
    else:
        return base * power(base, expnt - 1)

def power2(base, exponent, answer = 1):
    if exponent == 0:
        return answer
    else:
        return power2(base, exponent-1, answer*base)

print(power2(2, 4))