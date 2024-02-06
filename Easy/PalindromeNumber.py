def PalindromeNumber(x: int): # EZ METHOD
    numStr = str(x) # convert to string  for easy reversal
    if numStr == numStr[::-1]: # ::-1 reverses the array to characters the string
        return True # if palindrome meaning same number forward and backward, return true
    else:
        return False # else false

var = PalindromeNumber(121) # true 121 = 121 
var2 = PalindromeNumber(12234) # false 12234 = 43221
print(var)
print(var2)

