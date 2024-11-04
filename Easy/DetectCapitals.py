# Detect capitals
""" 
We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital, like "Google".
Given a string word, return true if the usage of capitals in it is right.
"""

# Beats 87% of python3 submissions.
# ! IDEA
""" 
in this case there are only 3 posibilities all are checked, first i add the str to a array and have my capital map ready to compare the elements of this chararray with
NOTE: first we check if the str is of length 1 if so we return true as it will fit into the 3 following cases no matter what + we check the strings upto 2 indexes so if the str length was one we would get a index out of bounds error
NOTE: here i aslo check if the str is of length 0 if so we return true BUT this is optinal as we are given a str on at least length 1 (i did it so no index out of bounds error)
3 CASES for true:
1) if the first and second letters are capital then all the letters are capital.
2) if the firs tletter is capital and the second letter is not capital then all letter of this string exepect the first letter should not be capital.
3) if the first letter is not capital then all the letters of this string must not be capital.
- The boolean var is capital is set to false and as we go through these 3 cases its value is changed depending on the case at the end this boolean value is returned. NOTE: so if one of these cases is not met then isCapital would be false. we want this as all the cases for iscapital to be true are there
"""
def detectCapitalUse(word: str) -> bool:
    Capitalmap = {'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'}
    isCapital = False
    chararray = []
    for char in word:
        chararray += char
        
    if len(chararray) == 1 or len(chararray) == 0:
        return True
        
    if chararray[0] in Capitalmap and chararray[1] in Capitalmap:
        isCapital = True
        for i in chararray:
            if i not in Capitalmap:
                isCapital = False
                
    elif chararray[0] in Capitalmap and chararray[1] not in Capitalmap: 
        isCapital = True
        index = 0
        for char in word:
            if char in Capitalmap and index != 0:
                isCapital = False
            index += 1
        
    elif chararray[0] not in Capitalmap:
        isCapital =True
        for char in word:
            if char in Capitalmap:
                isCapital = False
    
    return isCapital

print(detectCapitalUse("USA"))  # True
print(detectCapitalUse("leetcode")) # True
print(detectCapitalUse("Google"))  # True
print(detectCapitalUse("FlaG"))  # False
print(detectCapitalUse("a"))  # True
print(detectCapitalUse("FFFFFFFFFFFFf"))  # false