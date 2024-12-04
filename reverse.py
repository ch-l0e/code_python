def reverse(word):
    def helper(word, num, reverse = ""):
        if num < 0:
            return reverse
        else:
            reverse = reverse + word[num]
            return helper(word, num - 1, reverse)
    if len(word) == 1:
        return word
    else:
        return helper(word, len(word) - 1, "")

print(reverse("taco"))