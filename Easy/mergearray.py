""" 
problem:
    - Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.  
    - The number of elements initialized in nums1 and nums2 are m and n respectively.
    - You may assume that nums1 has a size equal to m + n such that it has enough space to hold additional elements from nums2.
    - You may modify the input array (the first operand) in-place with O(1) extra memory.
"""
# ! O(n+m) time complexity 
def merge(nums1, m, nums2, n):
    idx1 = 0 # index for nums1s current element
    idx2 = 0 # index for nums2s current element
    for _ in range(n): # loop through nums2 as num2 is the one being merged i.e nums2.len elements need to be merged
        # done skip elements compare starting with new lt added
        if m == 0: # if nums1 is empty just copy over nums2 into nums1
            nums1.insert(idx1, nums2[idx2]) # insert element from nums2 into nums1 at the index of idx1 which tracks the current element in nums1
            nums1.pop() # remove the last element in nums1 as its a placeholder '0'
            idx1 += 1 # increment idx1 we need to add at the next index in nums1
            idx2 += 1 # increment idx2 move to the next element in nums2
        elif nums1[idx1] <= nums2[idx2]: # if the current element in nums1 is less than or equal to the current element in nums2 
            # we must find the correct position to insert the element from nums2 into nums1
            # i.e if we have 1,1,3 and we need to insert 2 and we are comparing the first element in nums1 and nums2 
            # then we must keep comparing the elements in num1 until we find a number greater than or equal to the current element in nums2
            # then we insert the element from nums2 into nums1 at that position so that would be in 3's position, pushing 3 and the rest of the elements to the right
            # if we dont find that number than we insert after the last element so if it was 1,1,1 2 would be inserted at the 4th position after the last 1
            curr = nums2[idx2] # current element in nums2 we are trying to insert into nums1
            found = False # flag to check if we found the correct position to insert the element from nums2 into nums1
            for num in range(idx1, m+idx1): # loop through nums1 starting at the index we are currently at in nums1 until we reach the end of nums1, 'm+idx1' m is the base len of nums1 and idx1 is how many elements we have added so far i.e how much the base len has increased = the len of nums1 discluding the placeholder '0'
                if nums1[num] >= curr: # if the current element in nums1 is greater than or equal to the current element in nums2 we have found the correct position
                    nums1.insert(num, nums2[idx2]) # insert the element from nums2 into nums1 at the correct position, the rest of the arr will shift to the right
                    found = True # set the flag to true
                    break # exit the loop
            if not found: # if we did not find the correct position to insert the element from nums2 into nums1
                nums1.insert(m+idx1, nums2[idx2]) # insert the element from nums2 into nums1 at the end of nums1, 'm+idx1' if the index of the last element in nums1 discluding the placeholder '0'
            nums1.pop()  # remove the last element in nums1 as its a placeholder '0'
            idx1 += 1 # increment idx1 we need to add at the next index in nums1
            idx2 += 1 # increment idx2 move to the next element in nums2
        else: # if the current element in nums1 is greater than the current element in nums2 then we must insert the element from nums2 before the current element in nums1
            nums1.insert(idx1, nums2[idx2]) # insert the element from nums2 into nums1 at the current index the rest of the arr will shift to the right making the inserted element less that the next
            nums1.pop() # remove the last element in nums1 as its a placeholder '0'
            idx1 += 1 # increment idx1 we need to add at the next index in nums1
            idx2 += 1 # increment idx2 move to the next element in nums2
    
    print(nums1) # * not required just for testing, the testcase will check if nums1 is correct
    
# Test cases
merge([1,2,3,0,0,0], 3, [2,5,6], 3) # [1,2,2,3,5,6]
merge([1,1,3,0,0,0], 3, [2,3,6], 3) # [1,1,2,3,3,6]
merge([1,0], 1, [2], 1) # [1,2]
merge([3,4,5,0,0], 3, [1, 2], 2) # [1,2,3,4,5]
merge([0,0,0], 0, [1,2,3], 3) # [1,2,3]
