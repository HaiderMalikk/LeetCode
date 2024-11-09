# PRonlem
""" 
You are given a string num consisting of only digits. 
A string of digits is called balanced if the sum of the digits at even indices is equal to the sum of digits at odd indices.

Input: num = "1234"

Output: false

Explanation:

The sum of digits at even indices is 1 + 3 == 4, and the sum of digits at odd indices is 2 + 4 == 6.
Since 4 is not equal to 6, num is not balanced.
"""

# ! Solution
# NOTE: there is a much shorter solution using map and list slicing but just the syntax will give you nightmares plus this solution is easy to understand and read and uses common things like remainder division and int() casting

def isBalanced(num: str) -> bool: # num is a string of digits
        index = 0 # index to track position in string as char is not a number
        evensum = 0 # sum of digits at even indices
        oddsum = 0 # sum of digits at odd indices
        for char in num: # loop through each char in string
            if index % 2 == 0: # if index is even i.e if the index divided by 2 has a remainder of 0
                evensum += int(char) # add the digit to the sum of even indices as its an even index, i use int() to convert char to int
            else: # if index is odd 
                oddsum += int(char) # add the digit to the sum of odd indices as its an odd index
            
            index += 1 # increment the index by 1 as we just processed a char (i.e one element in the num string)
     
        return evensum == oddsum # return true if the sum of even indices is equal to the sum of odd indices else return false
    
print(isBalanced("1234")) # false
print(isBalanced("24123")) # true