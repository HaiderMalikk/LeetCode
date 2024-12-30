""" 
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""
# make sol in place dont return anything

# Sol:
""" 
if you look at the steps all this problem is is just rempoving the last element and adding it to the start of the array
how is this a medium ?
"""
def rotate(nums, k):
    for _ in range(k): # rotate k times
        temp = nums.pop() # remove last element and store it in temp
        nums.insert(0, temp) # add temp to the start of the array

nums = [1,2,3,4,5,6,7]
k = 3
rotate(nums, k)
print(nums) # [5,6,7,1,2,3,4]
