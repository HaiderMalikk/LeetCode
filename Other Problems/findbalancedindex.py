""" 
- Find a index where the same amount even numbers at left and odd numbers at right, the index is the middle point of the array and dose not count as left or right.

EX:
arr =  [2, 4, 1, 3, 5, 6]

ans: index 2, element value: 1 we have 2 even number at left(2, 4) and 2 odd number at right(3, 5)
"""
# Solution

def findbalancedindex(arr): # returns the first index where the same amount even numbers at left and odd numbers at right
    for i in range(len(arr)): # loop through the array n times where n is the length of the array this makes sure we check the left and right side of the array at each element
        left = arr[:i] # the left side of the array if from the start to before the current index (here i is discluded)
        right = arr[i+1:] # the right side of the array if from the end to the current index + 1 this +1 discards the current index making it the middle, here i is included so we need i + 1
        # all left and right arrays are with reference to the current index (middle)
        
        eveninleft = list(filter(lambda x: x % 2 == 0, left))  # filter out even numbers from the left side
        oddinright = list(filter(lambda x: x % 2 != 0, right))  # filter out odd numbers from the right side
        
        if len(eveninleft) == len(oddinright): # if the number of even numbers in the left side is equal to the number of odd numbers in the right side
            return i # return the current index which is the middle point of the array
        
    return None # if no such index is found return None
        
arr = [2, 4, 1, 3, 5, 6]
print(findbalancedindex(arr)) # output: 2 at index 2 = value 1, theres is 2 even number at left(2,4) and 2 odd number at right(3,5)
arr2 = [2, 6, 3, 5, 5, 4, 7] 
print(findbalancedindex(arr2)) # output: 3 at index 3 = value 5, theres is 2 even number at left(2,6) and 2 odd number at right(3,5)
arr3 = [1, 3, 5, 7, 9, 11 ] 
print(findbalancedindex(arr3)) # output: 5 at index 5 = value 11, theres is 0 even number at left(1,3,5,7,9) and 0 odd number at right(no elements so 0 elements)
arr4 = [1, 3, 6, 8, 1, 1]
print(findbalancedindex(arr4)) # output: None