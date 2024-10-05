def palindrome(prompt):
    word = input(prompt).lower()
    flipped = ""
    i = len(word) - 1
    while i >= 0:
        flipped = flipped + word[i]
        i = i - 1
    if flipped == word:
        print(f"{word} is a palindrome")
    else:
        print(f"{word} is not a palindrome")
    return flipped # ASK: is this line necessary

#print(palindrome("Enter a word: "))
palindrome("Enter a word: ")