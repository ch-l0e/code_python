def prime(num):
    if num == 0:
        return False
    for i in range(num - 1, 1, -1):
        if num % i == 0:
            return False
    return True

#print(prime(5))

def average(a_list):
    answer = []
    if len(a_list) == 0:
        return None
    for i in range(len(a_list)):
        for j in range(2, len(a_list)*2 + 1):
            for k in range(2, len(a_list)*2 + 1):
                if prime(j) and prime(k):
                    if (j + k)/2 == a_list[i]:
                        answer.append(f"{j} {k}")
                        break
            if prime(j) and prime(k):
                if (j + k)/2 == a_list[i]:
                    break
    return answer

size = int(input())
values = []
for i in range(size):
    values.append(int(input()))
print(average(values))