def dupChecker():
    word1 = input("Enter first word: ")
    word2 = input("Enter second word: ")
    duplicates = []
    for i in word1:
        if word2.find(i) != -1 and i not in duplicates:
            duplicates.append(i)
    print(duplicates)

dupChecker()