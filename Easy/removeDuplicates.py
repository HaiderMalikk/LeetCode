def removeDuplicates(nums: list) -> list: # dynamicly changing len of array
    i = 0 # start a counter
    while i < len(nums) - 1: # kinda a for loop runs until we have checked all elements in the list.
        if nums[i] == nums[i + 1]:#  check to see if current element is equal to next one if so then it's a duplicate
            nums.pop(i + 1) # remove duplicate NOTE pop(index) while remove(element) 
        else:
            i += 1 # if there is no duplicates move on to next element but we treversed 1 element to increment counter by 1 to keep track of list
    return nums

nums = [1, 1, 1, 2, 3, 3, 4]
print(removeDuplicates(nums))

# NOTE: the leetcode solution will ask you to return k the ammount of elements in your new array
# to do this
## 1) under i put k = 1  # we will Initialize k to 1 since the first element is always included
## 2) under the else pit k += 1  # we will Increment k only when a new unique element is encountered as that whats added to new array
