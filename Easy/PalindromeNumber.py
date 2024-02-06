def PalindromeNumber(x: int):
    numStr = str(x)
    if numStr == numStr[::-1]:
        return True
    else:
        return False

var = PalindromeNumber(121)
var2 = PalindromeNumber(12234)
print(var)
print(var2)

