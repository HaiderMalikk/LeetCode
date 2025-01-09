def canJump(nums):
    n = len(nums)
    jumps = 0
    farthest = 0
    current_end = 0

    for i in range(n - 1):
        farthest = max(farthest, i + nums[i])  # Track the farthest point reachable
        if i == current_end:  # When we reach the end of the current jump range
            jumps += 1
            current_end = farthest  # Update the range for the next jump
    
    return jumps
    
print(canJump([2,3,1,1,4])) # Output: 2
print(canJump([10,9,8,7,6,5,4,3,2,1,1,0])) # Output: 2
print(canJump([2,1,1,1,1])) # Output: 3
print(canJump([1,1,1,1,1])) # Output: 4
print(canJump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3])) # Output: 2




