# TODO: fix time error for arrays of very large size 1000 + the time limit is exceded

def maximumBeauty(items, queries):
    maxBeautyarray = []
    for querie in queries:
        validitemsarray = []
        maxBeauty = 0
        
        for item in items:
            if item[0] <= querie:
                validitemsarray.append(item)
        
        for validitems in validitemsarray:
            if validitems[1] > maxBeauty:
                maxBeauty = validitems[1]
        
        maxBeautyarray.append(maxBeauty)
    
    return maxBeautyarray
    
print(maximumBeauty([[1,2],[3,2],[2,4],[5,6],[3,5]], [1,2,3,4,5,6])) # Output: [2,4,5,5,6,6]
print(maximumBeauty([[1,2],[1,2],[1,3],[1,4]], [1])) # Output: [4]
print(maximumBeauty([[10,1000]], [5])) # Output: [0]