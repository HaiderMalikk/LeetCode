#Input: nums = [1,1,1,2,2,3]
#Output: 5, nums = [1,1,2,2,3,_]
#[0,0,1,1,1,1,2,3,3]
# [0,0,1,1,2,3,3]

# !! FIX
# while loop approach to track curr element not just index

def removeDuplicates(nums) -> int:
    seen = {}
    index = 0
    for num in nums:
        if num not in seen:
            seen[num] = 1
        else:
            print(num, seen[num], index)
            seen[num] += 1
            if seen[num] > 2:
                nums.pop(index)
                index -= 1
        index += 1
                
    print(nums)
    return len(nums)
    
print(removeDuplicates([1,1,1,2,2,3]))
print(removeDuplicates([0,0,1,1,1,1,2,3,3]))
