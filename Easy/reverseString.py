def RevStr(s: list) -> list:
    left = 0 # left starts at start of array index 0
    right = len(s)-1  # right is set to the last element in the array, the -1 is there as we are using zero based indexing (index starts at zero).
    while left < right: # left ++ and right -- insure the pointers will meet in the middel where to flip in needed
        temp = s[left] # temporarily store the value of the left element
        s[left] = s[right] # in the first iteration let the first element be the last one then the second one be the second lsat one etc
        s[right] = temp # let the right element be the left one this is s[right] = s[left] but in theline above we gave s[left] a value so to remember left we set temp = s[left]
        left += 1 # left pointer moves up one element (forwards)
        right -= 1# right pointer moves down a element (backwards)
        # NOTE we could have done # s[left], s[right] = s[right], s[left]  but that would not be efficient

    return s # once done return new str

print(RevStr(["a","b","c","d","e"])) # ["e", "d", "c" , "b" , "a"]
