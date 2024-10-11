def anagram_checker():
    """
    anagram: words with same characters
    Arguements:
        word1 = string --> only alphabetical characters in lowercase
        word2 = string --> only alphabetical characters in lowercase
    
    Return:
        boolean: true if words are anagrams, false if not
    """
    word1 = input("Enter first word: ").lower()
    word2 = input("Enter second word: ").lower()
    characters = word1
    if len(word1) != len(word2):
        return False
    else:
        for i in word2:
            if characters.find(i) != -1:
                characters = characters.replace(i, "")
            else:
                return False
        return True

print(anagram_checker())