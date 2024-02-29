def count_pairs(nums:list[int], target:int) -> int: # easiest question on leetcode if u cant do this drop out(JK)
    counter = 0 # we will be counting the number of pairs so get a empty counter ready
    # two pointer array look at my two sum for more deatil 
    # the second loop always stating from i+1 ensures i<j and no pairs are counted twice
    for i in range(len(nums) - 1): # pointer 1 
        for j in range(i + 1, len(nums)): # pointer 2
            if (nums[i] + nums[j]) < target: # if the current pairs sum is less than the target
                counter += 1 # we have found a pair so count it
    return counter # return the total number of valid pairs
            
print(count_pairs([-6,2,5,-2,-7,-1,3], -2)) # output -> 10
# example explained
"""
- (0, 1) nums[0] + nums[1] = -4 < target
- (0, 3) nums[0] + nums[3] = -8 < target
- (0, 4) nums[0] + nums[4] = -13 < target
- (0, 5) nums[0] + nums[5] = -7 < target
- (0, 6) nums[0] + nums[6] = -3 < target
- (1, 4) nums[1] + nums[4] = -5 < target
- (3, 4) nums[3] + nums[4] = -9 < target
- (3, 5) nums[3] + nums[5] = -3 < target
- (4, 5) nums[4] + nums[5] = -8 < target
- (4, 6) nums[4] + nums[6] = -4 < target
"""