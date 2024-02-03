def removeDuplicates(nums): # dynamicly changing len of array
    i = 0
    while i < len(nums) - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
        else:
            i += 1
    return nums

nums = [1, 1, 1, 2, 3, 3, 4]
print(removeDuplicates(nums))
