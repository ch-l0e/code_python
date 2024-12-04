def palindrome(word):
    def helper(word, left, right):
        if left > right: 
            return True
        elif word[left] != word[right]:
            return False
        else:
            return helper(word, left + 1, right - 1)
    if not word:
        return True
    elif len(word) == 3:
        return word[-1] == word[0]
    else:
        return helper(word, 0, len(word) - 1)

print(palindrome("tacocat"))