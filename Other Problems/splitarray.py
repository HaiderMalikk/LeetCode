""" 
given a array see if it is possible to split the array into two parts such that the sum of the two parts is equal
subbarray must be non empty
"""

# O(n)
def split_array(arr: list[int], index=1, leftsum=0, rightsum=None) -> bool:
    if rightsum is None:
        rightsum = sum(arr)  # Calculate total sum only once at the beginning
    
    if index == len(arr):  # Base case: If we've checked all splits, return False
        return False

    leftsum += arr[index - 1]  # Add current element to left sum
    rightsum -= arr[index - 1]  # Remove current element from right sum

    if leftsum == rightsum:  # Check if split is valid # do after the first index is added as arr must be non empty
        return True

    return split_array(arr, index + 1, leftsum, rightsum)  # Recur with updated sums



# or o(n^2) 
def splitarray(arr: list[int], index) -> bool:
    left = arr[:index]
    right = arr[index:]
    
    leftsum = sum(left)
    rightsum = sum(right)
    
    if index == len(arr):
        return False
        
    if leftsum == rightsum:
        return True
        
    
    index += 1
    return splitarray(arr, index)
        


# Goal: split an array into two halves such that the sum of the elements in the left half is equal to the sum of the elements in the right half
print(splitarray([2,3,3,7,1], 1)) # true ([2,3,3] = [7,1])
print(splitarray([5, 6, 1, 1, 6, 5], 1)) # true ([5,6,1] = [1,6,5])
print(splitarray([1,1,1,1,1], 1)) # false no way to split 