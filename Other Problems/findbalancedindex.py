""" 
- Find a index where the same amount even numbers at left and odd numbers at right

EX:
arr = [1, 2, 3, 4, 5, 6, 7]

ans: index 3, at element 4. we have 1 even number at left and 2 odd number s at left, and 1 even number at right and 2 odd numbers at right
this means the list is balanced at index 3
"""
# Solution

def findbalancedindex(arr): 
    for i in arr: # loop over the array
        # split the array into left and right subarrays at each loop the split point is the current index
        left = arr[:i-1] # get all elements to the left of the current element discluding the current element
        right = arr[i:] # get all elements to the right of the current element
        
        eveninleft = list(filter(lambda x: x % 2==0, left)) # get all even numbers in the left side
        oddinleft = list(filter(lambda x: x % 2 !=0, left)) # get all odd numbers in the left side
        eveninright = list(filter(lambda x: x % 2==0, right)) # get all even numbers in the right side
        oddinright = list(filter(lambda x: x % 2 !=0, right)) # get all odd numbers in the right side
        
        # if the number of even numbers in the left side is equal to the number of odd numbers in the right side
        # this compares values in the left and right subarrays
        if (len(eveninleft) == len(eveninright)) and (len(oddinleft) == len(oddinright)): 
            return arr.index(i) # return the index of the current element as thats the point where the array is balanced
        
arr = [1, 2, 3, 4, 5, 6, 7]
print(findbalancedindex(arr)) # output: 3