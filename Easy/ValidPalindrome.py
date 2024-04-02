def isPalindrome(s: str) -> bool:
    if len(s) == 0: # is a empty str its a palindrome
        return True
    
    # joining all the letters in the string nums are filtered and lower unsures that it will be a valid char
    s = ''.join(filter(str.isalnum, s.lower()))
    if s == s[::-1]:
        return True
    else:
        return False

print(isPalindrome(" ")) # true
print(isPalindrome("race car")) # true
print(isPalindrome("Hello")) # false