# TODO: fix time error for arrays of very large size 1000 + the time limit is exceded
def maximumBeauty(items, queries):
    maxBeautyarray = [] # array to store max beauty for each query
    for querie in queries: # lop over each query
        validitemsarray = [] # array to store valid items for each query
        maxBeauty = 0 # variable to store max beauty for each query
        
        for item in items: # find all iteams in the given items array whose first value (price) is less than or equal to the current query
            if item[0] <= querie:
                validitemsarray.append(item) # add the item to the valid items array
        
        for validitems in validitemsarray: # loop over each valid item and find the maximum beauty
            if validitems[1] > maxBeauty: # if the current item's beauty is greater than the max beauty found so far
                maxBeauty = validitems[1] # update the max beauty
        
        maxBeautyarray.append(maxBeauty) # add the max beauty found for the current query to the max beauty array and move to the next query
    
    return maxBeautyarray # return the max beauty array
    
print(maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6])) # Output: [2,4,5,5,6,6]
print(maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1])) # Output: [4]
print(maximumBeauty([[10,1000]], [5])) # Output: [0]