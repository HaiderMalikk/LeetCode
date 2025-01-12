""" 
given a string reverse its words:
Not only should the words be reversef but there should be no leading or trailing spaces and only 1 space between words in the final string

Example 1:
Input: s = "   the     sky is  blue  "
Output: "blue is sky the"
"""

def reverseWords(s):
    stringarr = s.strip().split(" ") # split the string by spaces and remove leading and trailing and leading spaces
    stringarr.reverse() # reverse the array of words
    # we splitted on spaces meaning any words with multiple spaces will leave many empty strings in the array reperesented by ""
    # each extra "" i.e each extra space between words is represented by an empty string in the array, so we remove them
    stringarr = [word for word in stringarr if word != ""] # this is a list comprehension that filters out the empty strings
    stringarr = " ".join(stringarr) # join the words back together with a space in between
    return stringarr # return the string

# testcases
print(reverseWords("   the     sky is  blue  ")) # "blue is sky the"
print(reverseWords("   hello   world  ")) # "world hello"
print(reverseWords("   a   b   c   ")) # "c b a"  #