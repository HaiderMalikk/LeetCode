def plusOne(digits):
    # try chainging add it works!
    add = 1  # Set the initial add to 1 since we are adding 1 to digits
    
    # Iterate over the digits from right to left
    # (len(digits) - 1, -1, -1) # start at the last element stop at first element, step by -1 so now last element is -1
    for i in range(len(digits) - 1, -1, -1):
        digits[i] += add  # Increment the current digit in the digits array by the add = 1 
        add = digits[i] // 10  # carry the remainder over to the next digit in digits by updating add
        digits[i] %= 10  # this Updates the current digit to be in the range [0, 9] so the digit 15 would be 5
    
    # If there's a carry left after the loop append it as a new leading digit
    if add != 0:
        digits.insert(0, add) # if we have a number like 99 after the loop digits == [0, 0] by the carry 1 witch was added to add is there now lets add that to the start so digits = [1,0,0]
    return digits


print(plusOne([1, 2, 3]))  # Output [1, 2, 4]
print(plusOne([4, 3, 2, 1]))  # Output [4, 3, 2, 2]
print(plusOne([9]))  # Output [1, 0]
print(plusOne([9, 9]))  # Output [1, 0, 0]
