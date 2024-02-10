def plusOne(digits):
    if digits[0] == 9:
        digits[0] = 1
        digits.append(0)
    else:
        digits[-1] = digits[-1] + 1
    return digits

print(plusOne([9]))