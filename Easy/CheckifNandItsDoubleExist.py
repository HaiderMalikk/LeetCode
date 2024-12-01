
""" 
Given an array arr of integers, check if there exist two indices i and j such that :

i != j
0 <= i, j < arr.length
arr[i] == 2 * arr[j]
 

Example 1:

Input: arr = [10,2,5,3]
Output: true
Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
Example 2:

Input: arr = [3,1,7,11]
Output: false
Explanation: There is no i and j that satisfy the conditions.
"""

# Solution
def checkIfExist(arr: list[int]) -> bool: # returns true if there exist two indices i and j such that i != j and arr[i] == 2 * arr[j]
    for i in range(len(arr)): # iterate over the array
        for j in range(len(arr)): # iterate over the array again with a element at index i selected as N
            if arr[j] * 2 == arr[i] and i != j: # check if the element at index j * 2 is equal to the element at index i and indexes are not the same
                return True # if the condition is met, return True
    return False # if no such pair is found, return False

arr = [10,2,5,3]
print(checkIfExist(arr)) # Output: True
arr = [3,1,7,0]
print(checkIfExist(arr)) # Output: False
arr = [0,0]
print(checkIfExist(arr)) # Output: True