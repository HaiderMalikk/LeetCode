def romanToInt(str):
    #  map Roman numeral characters to integers
    m = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    # roman letters will tally here
    answer = 0

    # loop through all eleemnts in string
    for i in range(len(str)):
        # if the current character is smaller than the next one
        if i < len(str) - 1 and m[str[i]] < m[str[i+1]]:
            # If true then subtract the value of the current character
            answer -= m[str[i]] # roman numeral subtraction rule
        else:
            # If false then add the value of the current character
            answer += m[str[i]] # roman rumeral additon

    # Return the final integer value
    return answer

romantoInt_result = romanToInt("MCMXCIV")
print(romantoInt_result)