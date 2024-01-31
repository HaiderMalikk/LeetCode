class Solution(object):
    def reverseString(self, s):
        # Initialize two pointers, one at the beginning and one at the end of the list
        start, end = 0, len(s) - 1

#        Iterate until the pointers meet in the middle
        while start < end:
            s[start], s[end] = s[end], s[start]
            # Move the pointers towards each other
            start += 1
            end -= 1

# The list has been modified in-place, and there's no need to return anything
#NOTE: this is a leetcode solution will not run in vs code etv

