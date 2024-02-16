def three_sum(nums): # two pointer approch 
    # Sort the input list in ascending order
    nums.sort()
    # Initialize an empty list to store the result
    result = []
    # Get the length of the input list
    n = len(nums)
    
    # Iterate over each index in the input list
    for i in range(n):
        # Skip duplicates by checking if the current element is the same as the previous element
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Calculate the target sum using two-pointer approach
        target = -nums[i] # transforming the problem into finding two numbers in the remaining array (to the right of nums[i]) that sum up to -nums[i], which is equivalent to finding two numbers that add up to target
        # Initialize two pointers, one at the element just after i and the other at the end of the list
        left, right = i + 1, n - 1
        
        # Loop until the two pointers meet
        while left < right:
            # Check if the sum of the elements at the two pointers is equal to the target
            if nums[left] + nums[right] == target:
                # If the sum is equal, add the triplet to the result list
                result.append([nums[i], nums[left], nums[right]])
                # Move the left pointer to the right to avoid duplicates
                left += 1
                # Move the right pointer to the left to avoid duplicates
                right -= 1
                
                # Skip over any duplicate elements to avoid duplicate triplets in the result
                while left < right and nums[left] == nums[left - 1]: #This line skips over any duplicate elements to the right of the left pointer
                    left += 1 # += 1 is used to increment the left pointer to move it to the next (unique) element in the array
                while left < right and nums[right] == nums[right + 1]: # skips over any duplicate elements to the left of the right
                    right -= 1 # (-= 1) to skip over the duplicate and consider the next unique element from the right side.
            # If the sum is less than the target, move the left pointer to the right
            elif nums[left] + nums[right] < target:
                left += 1
            # If the sum is greater than the target, move the right pointer to the left
            else:
                right -= 1
                
    # Return the list of unique triplets that sum up to zero
    return result

# Example usage
nums = [-1, 0, 1, 2, -1, -4]
print(three_sum(nums))  # Output: [[-1, -1, 2], [-1, 0, 1]]
