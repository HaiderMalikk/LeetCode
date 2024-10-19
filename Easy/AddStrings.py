# add 2 strings
def addStrings(num1: str, num2: str) -> str:
    # Reverse both strings to start adding from the least significant digit
    num1, num2 = num1[::-1], num2[::-1]

    carry = 0
    result = []

    # Loop through the longest of the two numbers so we know the max times we need to loop
    for i in range(max(len(num1), len(num2))):
        # Get the current digits, if a number has been exhausted meaning if it runs out use 0 so for 433 + 33 after adding 43 and 33 the last 3 in 433 will be added with 0 so think of it as 433 + 033 and vise versa for both strs but rememebring the strings are reversed
        digit1 = int(num1[i]) if i < len(num1) else 0
        digit2 = int(num2[i]) if i < len(num2) else 0

        # Add digits and carry at first there is no carry but there can be a carry in the next iteration
        total = digit1 + digit2 + carry
        carry = total // 10  # Update carry the carry is simply the total divided by 10 so for 7 + 3 = 10 the remainder is 10 // 10 = 1 which is then moved to the carry 
        result.append(str(total % 10))  # Append the last digit to result why? as we are dding from the least significant digit to the most significant digit meaning for 400 we would add from the ones place to the hundreds place so here we need to only add the remander of our carry here the if cary is 10 10%10=0 so we add 0 to our result but we still carry one to be added with the next digits

    # If there's a remaining carry, append it as its the last digit there nothing left to add 
    if carry:
        result.append(str(carry))

    # Reverse the result back to its correct order and join the list into a string using the '' and reversing using ::-1 
    return ''.join(result[::-1])

# Example usage
print(addStrings("11", "123"))  # Output: "134"
print(addStrings("456", "77"))  # Output: "533"
print(addStrings("0", "0"))     # Output: "0"
print(addStrings("477", "33"))  # Output: "510"



""" 
# ! here is chat gpt taking us through each iteration and wathcing the variables for the ex: 477 + 33
Let’s go through a detailed iteration of the code for the example 477 + 33, step by step, and observe how it works line by line.

Initial Setup
num1 = "477" and num2 = "33".
We reverse both strings:
num1 = "774"
num2 = "33"
We also initialize:

carry = 0
result = [] (this will store the sum digits in reverse order).
Now we enter the loop where we add corresponding digits from both numbers. We loop for the maximum length of the two numbers, which is max(len("774"), len("33")) = 3.

Iteration 1 (i = 0)
Digit Extraction:
digit1 = int(num1[0]) = int('7') = 7
digit2 = int(num2[0]) = int('3') = 3
Addition:
total = digit1 + digit2 + carry = 7 + 3 + 0 = 10
We update carry with total // 10 = 10 // 10 = 1.
Store the Last Digit:
We append total % 10 = 10 % 10 = 0 to result, so result = ['0'].
Iteration 2 (i = 1)
Digit Extraction:
digit1 = int(num1[1]) = int('7') = 7
digit2 = int(num2[1]) = int('3') = 3
Addition:
total = digit1 + digit2 + carry = 7 + 3 + 1 = 11
We update carry with total // 10 = 11 // 10 = 1.
Store the Last Digit:
We append total % 10 = 11 % 10 = 1 to result, so result = ['0', '1'].
Iteration 3 (i = 2)
Digit Extraction:
digit1 = int(num1[2]) = int('4') = 4
digit2 = 0 because num2 has no digit at index 2 (out of bounds).
Addition:
total = digit1 + digit2 + carry = 4 + 0 + 1 = 5
We update carry with total // 10 = 5 // 10 = 0 (no carry left).
Store the Last Digit:
We append total % 10 = 5 % 10 = 5 to result, so result = ['0', '1', '5'].
End of Loop
At this point, we've processed all digits of both numbers. There's no remaining carry, so we don't need to append anything further.

Final Result
The result list currently contains ['0', '1', '5'], which is the reversed sum.
We reverse it back to the correct order: ''.join(result[::-1]) = ''.join(['5', '1', '0']) = "510".
Thus, the sum of 477 + 33 is "510".

Summary of Iterations:
Add 7 and 3 → 10 → Store 0, carry 1.
Add 7 and 3 → 11 → Store 1, carry 1.
Add 4 and 0 → 5 → Store 5, no carry.
Final result after reversing: "510".


"""