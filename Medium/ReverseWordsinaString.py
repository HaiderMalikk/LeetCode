"""
given a string reverse its words:
Not only should the words be reversef but there should be no leading or trailing spaces and only 1 space between words in the final string

Example 1:
Input: s = "   the     sky is  blue  "
Output: "blue is sky the"
"""


def reverseWords(s):
    s = s.strip()
    words = s.split()
    s = ""
    for word in range(len(words) - 1, -1, -1):
        s += words[word]
        if word != 0:
            s += " "
    return s


# testcases
print(reverseWords("   the     sky is  blue  "))  # "blue is sky the"
print(reverseWords("   hello   world  "))  # "world hello"
print(reverseWords("   a   b   c   "))  # "c b a"  #
