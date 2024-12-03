""" 
You are given a 0-indexed string s and a 0-indexed integer array spaces that describes the indices in the original string where spaces will be added. Each space should be inserted before the character at the given index.

For example, given s = "EnjoyYourCoffee" and spaces = [5, 9], we place spaces before 'Y' and 'C', which are at indices 5 and 9 respectively. Thus, we obtain "Enjoy Your Coffee".
Return the modified string after the spaces have been added.
"""
# Solution
def addSpaces(self, s: str, spaces: list[int]) -> str: # create the function with parameters
    spacedstring = "" # initialize an empty string to store the result as we move through the string and add spaces
    lastwordindex = 0 # initialize a variable to keep track of the last word index we will continoue the string starting from this index after we add a space
    for space in spaces: # loop through the spaces array
        spacedstring += s[lastwordindex:space] # add the characters from the last word index to the space index to the result string
        spacedstring += " " # add a space to the result string as we just added the word before the space
        lastwordindex = space # update the last word index to the space index so we can continue from here in the next iteration
        
    spacedstring += s[lastwordindex:] # add the remaining characters in the string to the result string
    return spacedstring # return the result string
