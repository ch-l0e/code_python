def largest(array):
    def helper(a_list, num, big):
        if not a_list:
            return None
        elif len(a_list) == 1:
            return big
        elif num > len(a_list) - 1:
            return big
        else:
            if a_list[num] > big:
                big = a_list[num]
            return helper(a_list, num + 1, big)
    if not array:
        return None
    elif len(array) == 1:
        return array
    else:
        return helper(array, 1, array[0])


frogs = [2, 5, 1 , 8, 0]
print(largest(frogs))