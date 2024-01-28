def removeElement(nums, val):
        index = 0

        for i in range(len(nums)): # loop over all elements in nums
            if nums[i] != val: # if the element of nums at i is not equal to val
                nums[index] = nums[i] # take the index value and put i on its place
                index += 1 # increment the index as we now have a occurance of val

        return index # return index the occurance of val in nums

solution = removeElement([0,1,2,2,3,0,4,2], 2) # list, target
print(solution)