""" 
Given a list of integers, each int representing a jump length from that index to another index in the list. Determine if it is possible to jump to the last index in the list.
ex: [2,3,1,0,4] -> True as we can jump from 2 to 3 then 3 to 4 then 4 to the last index
# we can go from 2 to 3 or 1 as 2 repersents the jump length from 2
"""
def canJump(nums) -> bool: # sol
    if len(nums) == 1: # if only one element 
        return True  # we can jump to it
    currjump = nums[0] # jump value
    if currjump == 0: return False # cannot jump anywhere
    end = len(nums) - 1 # by index not value
    index = 0 # to track the current jump
    for _ in range(len(nums)): # loop over numbers as thats the max times we can jump
        foundmaxjump = False # to track if we found a jump greater than current
        foundat = 0 # to track the index of the jump greater than current so we can goto it
        maxsofar = 0 # to track the max jump seen in the range of current jump in case we dont find a jump greater than current
        maxsofarindex = 0 # to track the index of the max number seen so far
        for j in range(index+1, (index + currjump)+1): # scan all jumps in current jumps range to find max jump so that we can jump to that (+1 as range is exclusive)
            if nums[j] >= maxsofar: # find the max so far incase we dont mind a new jump greater than current jump we can goto that (keep it >= so that we always goto the furthest jump)
                maxsofar = nums[j] # update max so far
                maxsofarindex = j # update the index of max so far
            if j == end: # if we reach the end from current jump range return true
                return True # we can jump to the end
            if nums[j] >= currjump: # if we find a new max jump update curr jump to it so we can jump to that 
                currjump = nums[j] # update curr jump
                foundmaxjump = True # we found a jump greater than current
                foundat = j # update the index of the jump greater than current
        if not foundmaxjump and foundat == 0: # if no max jump was found from current jump than jump to the max so far but if the jump from max so far lands on 0 then goto the last possible jump from the current jump range
            zerojump = False # to track if the jump from max so far lands on 0
            for k in range(maxsofarindex + 1, (maxsofar + maxsofarindex) + 1): # loop from the start to the end of the next jump starting on the jump at max so far
                if k == end: # if we reach the end from current jump range return true beacuse in the next iteration it will jump to that anyway
                    return True # we can jump to the end
                if nums[k] == 0: # if any jump land on 0 then set the flag (this is really just to track the last jump to see if the last jump for the range of max so far jump lands on 0) but we must track the thing above so we must loop over all jumps in the range of max so far
                    zerojump = True  # set flag to true
                else: # if any jump doesn't land on 0
                    zerojump = False # reset flag to false 
            if zerojump: # if zerojump than jumping from max so far will land us on zero so goto the last possible jump from the current jump range
                currjump = nums[j] # update curr jump to the last possible jump
                index = j # update index to the last possible jump
            else: # if zerojump is false than jumping from max so far will not land us on zero so we can jump to the max so far and then jump from there
                currjump = maxsofar # update curr jump to the max so far
                index = maxsofarindex # update index to the max so far
        else: # if we found a jump greater than current jump
            index = foundat # update index to the index of the jump greater than current
        if currjump == 0: # if curr jump is 0 than we cannot jump anymore
            return False # we cannot jump anymore
    return False # if we exit the loop without returning true than we cannot jump
# test cases
print(canJump([5,9,3,2,1,0,2,3,3,1,0,0])) # Output: true
print(canJump([1,1,2,2,0,1,1])) # Output: true
print(canJump([2,2,0,2,0,2,0,0,2,0])) # Output: false
print(canJump([4,2,0,0,1,1,4,4,4,0,4,0])) # Output: true