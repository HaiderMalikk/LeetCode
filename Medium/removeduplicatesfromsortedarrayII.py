# ! removeDuplicates 2, remove any duplicates that occur more than twice 9array is sorted
def removeDuplicates(nums) -> int:
    seen = {}
    index = 0
    while index < len(nums):
        if nums[index] not in seen:
            seen[nums[index]] = 1
        else:
            seen[nums[index]] += 1
            if seen[nums[index]] > 2:
                nums.pop(index)
                index -= 1 # compensates for index++
        index += 1
    print(nums) # for ref, not required
    return len(nums)
    
print(removeDuplicates([1,1,1,2,2,3])) # 5
print(removeDuplicates([0,0,1,1,1,1,2,3,3])) # 7
