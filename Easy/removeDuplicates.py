def removeDuplicates(nums: list) -> list: # dynamicly changing len of array
    i = 0 # start a counter
    k = 1 # k is the len of our new array the len of nums is > 1 and the first elememt is always included
    while i < len(nums) - 1: # kinda a for loop runs until we have checked all elements in the list.
        if nums[i] == nums[i + 1]:#  check to see if current element is equal to next one if so then it's a duplicate
            nums.pop(i + 1) # remove duplicate NOTE pop(index) while remove(element) 
        else:
            i += 1 # if there is no duplicates move on to next element but we treversed 1 element to increment counter by 1 to keep track of list
            k += 1 # if theres no duplicates we have encounterd a unique number so add one to k
    
    return k # retunr the len of new array
    # return nums can be used to show new array (not required in leetcode)

nums = [1, 1, 1, 2, 3, 3, 4]
print(removeDuplicates(nums))