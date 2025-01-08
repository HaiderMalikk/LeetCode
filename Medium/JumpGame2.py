def canJump(nums) -> int: 
    currjump = nums[0] 
    if len(nums) == 1: return 0
    end = len(nums) - 1 
    index = 0 
    jumps = 0
    for _ in range(len(nums)): 
        jumps += 1
        foundmaxjump = False 
        foundat = 0 
        maxsofar = 0 
        maxsofarindex = 0 
        for j in range(index+1, (index + currjump)+1): 
            if nums[j] >= maxsofar: 
                maxsofar = nums[j] 
                maxsofarindex = j 
            if j == end: 
                return jumps
            if nums[j] >= currjump: 
                currjump = nums[j] 
                foundmaxjump = True 
                foundat = j 
        if not foundmaxjump and foundat == 0: 
            zerojump = False 
            for k in range(maxsofarindex + 1, (maxsofar + maxsofarindex) + 1): 
                if k == end: 
                    return jumps + 1 
                if nums[k] == 0: 
                    zerojump = True  
                else: 
                    zerojump = False 
            if zerojump: 
                currjump = nums[j] 
                index = j 
            elif not zerojump:
                curr = nums[k]
                if k+1 == end:
                    return jumps + 1
                for l in range(k + 1, (curr + k) + 1):
                    if l == end: 
                        return jumps + 1
            else: 
                currjump = maxsofar 
                index = maxsofarindex 
        else: 
            index = foundat 
    
print(canJump([2,3,1,1,4])) # Output: 2
print(canJump([10,9,8,7,6,5,4,3,2,1,1,0])) # Output: 2
print(canJump([2,1,1,1,1])) # Output: 3




