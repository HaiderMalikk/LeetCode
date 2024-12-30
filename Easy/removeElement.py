# Problem: remove all occurances of val in nums in place and return its new len
def removeElement(nums, val):
    index = 0 # track index as when we delete element we shift array and lose track of index if we use a normal for loop
    while index != len(nums): # go on until we reach the end of list
        if nums[index] == val: # if we found val
            nums.pop(index) # remove val by its index
            index -= 1 # to compensate for index ++
        index += 1 # goto next index
        # the + inedex and - index cancle so when we remove a element we stay at the same index as the next element will now be at the current index so we muct check that index again
    return index # stop when index == len(nums) hence just return index


print(removeElement([0,1,2,2,3,0,4,2], 2)) # ouput = 5 as nums = 0,1,3,0,4