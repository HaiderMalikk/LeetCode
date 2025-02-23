def reverseVowels(s):
    vset = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]
    v = []
    for char in s:
        if char in vset:
            v.append(char)
    index = len(s) - 1
    for char in s[::-1]:
        if char in vset:
            s = s[:index] + v.pop(0) + s[index + 1 :]
        index -= 1
    return s


print(reverseVowels("IceCreAm"))


# Example 1:

# Input: s = "IceCreAm"

# Output: "AceCreIm"

# Explanation:

# The vowels in s are ['I', 'e', 'e', 'A']. On reversing the vowels, s becomes "AceCreIm".

# Example 2:

# Input: s = "leetcode"

# Output: "leotcede"
