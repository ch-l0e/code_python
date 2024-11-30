def selection(a_list):
    for i in range(0, len(a_list) - 1):
        track = i
        for j in range(i + 1, len(a_list)):
            if a_list[j] > a_list[track]:
                track = j
        temp = a_list[i]
        a_list[i] = a_list[track]
        a_list[track] = temp
    return a_list

def bubble(a_list):
    swap = True
    while swap:
        swap = False
        for i in range(1, len(a_list)):
            if a_list[i] > a_list[i - 1]:
                temp = a_list[i - 1]
                a_list[i - 1] = a_list[i]
                a_list[i] = temp
                swap = True
    return a_list

def insertion(a_list):
    i = 0
    while i < len(a_list):
        j = i
        while j > 0 and a_list[j] > a_list[j - 1]:
            temp = a_list[j]
            a_list[j] = a_list[j - 1]
            a_list[j - 1] = temp
            j = j - 1
        i = i + 1
    return a_list

nums = [16, 37, 12, 42, 30, 36, 38, 49, 41, 41]
print(insertion(nums))