""" 
Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.
Example 1:
Input: citations = [3,0,6,1,5]
Output: 3
Explanation: [3,0,6,1,5] means the researcher has 5 papers in total and each of them had received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3 citations each and the remaining two with no more than 3 citations each, their h-index is 3.
a hindex possiblity was also 2 as 5,6 are 2 elements with more than 2 citations but 3 is the maximum hindex
"""

def hIndex(citations) -> int: # citations is an array return the hIndex
    citations = sorted(citations) # sort the array this way we know all elements after the index are greater than or equal to the index
    n = len(citations) # length of the array
    if n == 1: # if the array has only one element
        if citations[0] == 0: # if the element is 0
            return 0 # return 0
        return 1 # if there is only one element and it is not 0 return 1
    hIndex = 0 # initialize the hIndex
    for i in range(n): # loop through the array
        largerthanorequal = n - i # number of elements larger than or equal to the current index
        if largerthanorequal <= citations[i]: # if the number of elements larger than or equal to the current index is less than or equal to the current element
            if largerthanorequal > hIndex: # if the number of elements larger than or equal to the current index is greater than the current hIndex
                hIndex = largerthanorequal # update the hIndex to the number of elements larger than or equal to the current index
    return hIndex # return the hIndex

# for EX1: sorted = [0,1,3,5,6] at index 2, largerthanorequal = 3, as 3,5,6 are greater than or equal to 3
# and largerthanorequal = citations[2] = 3, so hIndex = 3, as we have 3 elements larger than or equal to 3
# after that at the next index 5,6 are 2 elements larger than or equal to 5, but 3 out previous hindex is larger than 2, so hIndex = 3
    
# testcases with output
print(hIndex([3,0,6,1,5])) # 3
print(hIndex([1,3,1])) # 1
print(hIndex([0])) # 0
print(hIndex([100])) # 1
print(hIndex([11, 15])) # 2