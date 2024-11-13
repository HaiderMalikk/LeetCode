# most beautiful item for each query

# problem"
""" 
You are given a 2D integer array items where items[i] = [pricei, beautyi] denotes the price and beauty of an item respectively.

You are also given a 0-indexed integer array queries. For each queries[j], you want to determine the maximum beauty of an item whose price is less than or equal to queries[j]. If no such item exists, then the answer to this query is 0.

Return an array answer of the same length as queries where answer[j] is the answer to the jth query.

 

Example 1:

Input: items = [[1,2],[3,2],[2,4],[5,6],[3,5]], queries = [1,2,3,4,5,6]
Output: [2,4,5,5,6,6]
Explanation:
- For queries[0]=1, [1,2] is the only item which has price <= 1. Hence, the answer for this query is 2.
- For queries[1]=2, the items which can be considered are [1,2] and [2,4]. 
  The maximum beauty among them is 4.
- For queries[2]=3 and queries[3]=4, the items which can be considered are [1,2], [3,2], [2,4], and [3,5].
  The maximum beauty among them is 5.
- For queries[4]=5 and queries[5]=6, all items can be considered.
  Hence, the answer for them is the maximum beauty of all items, i.e., 6.
"""



# ! sol 3 (solution with sorting)
# def maximumBeauty(items, queries):
#     maxBeautyarray = []
#     for querie in queries:
#         validitemsarray = []
#         for item in items:
#             if item[0] <= querie:
#                 validitemsarray.append(item)
#         # * till here the same code as next sol
        
#         # using the key concept to sort the valid items array by the second element of each item in validitemsarray 
#         # then getting the last subarray as that is the one with the highest beauty and getting the inner index of one as the index of 1 in item subarray holds the beauty
#         maxBeautyarray.append(
#             sorted(validitemsarray, key = lambda x : x[1])[-1][1]
#             )
    
#     return maxBeautyarray if len(maxBeautyarray) != 0 else [0] # return max beauty array

# # ! sol 2 (using max function along with lambda 'key' to find max beauty)
# def maximumBeauty(items, queries):
#     maxBeautyarray = [] # array to store max beauty for each query
#     for querie in queries: # for each query
#         validitemsarray = [] # array to store valid items for each query
#         for item in items: # for each item
#             if item[0] <= querie: # if item's beauty is less than or equal to query
#                 validitemsarray.append(item) # add item to valid items array
                
#         # we have valid iteams insted of loping over it just use max
#         # use key = x: x[1] to get the second element of each item in validitemsarray with the each iteam in the list being x
#         # the max function returns the subarray in items with the highest beauty beacuse of the lambda function
#         # NOTE from last line: this is beacuse iteam is a list and valid itemsarray is a collection of iteams so a 2d array hence the max function returns the subarray 
#         # then append the element at index 1 of the max tuple (validitem subarray/ item) in validitemsarray as index 1 is the beauty
#         # if we find no valid iteams we append 0 as beauty
        
#         if len(validitemsarray) != 0:
#             maxBeautyarray.append(max(validitemsarray, key = lambda x: x[1])[1]) # add this to notes in python
#         else:
#             maxBeautyarray.append(0)
    
#     return maxBeautyarray if len(maxBeautyarray) != 0 else [0] # shorthand to return empty array with 0 if no valid items found

# ! sol 1 (brute force with for loops)
# def maximumBeauty(items, queries):
#     maxBeautyarray = [] # array to store max beauty for each query
#     for querie in queries: # lop over each query
#         validitemsarray = [] # array to store valid items for each query
#         maxBeauty = 0 # variable to store max beauty for each query
        
#         for item in items: # find all iteams in the given items array whose first value (price) is less than or equal to the current query
#             if item[0] <= querie:
#                 validitemsarray.append(item) # add the item to the valid items array
        
#         for validitems in validitemsarray: # loop over each valid item and find the maximum beauty
#             if validitems[1] > maxBeauty: # if the current item's beauty is greater than the max beauty found so far
#                 maxBeauty = validitems[1] # update the max beauty
        
#         maxBeautyarray.append(maxBeauty) # add the max beauty found for the current query to the max beauty array and move to the next query
    
#     return maxBeautyarray # return the max beauty array
    
# test cases
# print(maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6])) # Output: [2,4,5,5,6,6]
# print(maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1])) # Output: [4]
# print(maximumBeauty([[10,1000]], [99])) # Output: [0]
# print(maximumBeauty([[10,1000]], [5, 9])) # Output: [0, 0]
# print(maximumBeauty([[193,732],[781,962],[864,954],[749,627],[136,746],[478,548],[640,908],[210,799],[567,715],[914,388],[487,853],[533,554],[247,919],[958,150],[193,523],[176,656],[395,469],[763,821],[542,946],[701,676]], [885,1445,1580,1309,205,1788,1214,1404,572,1170,989,265,153,151,1479,1180,875,276,1584])) # out: [962,962,962,962,746,962,962,962,946,962,962,919,746,746,962,962,962,919,962]