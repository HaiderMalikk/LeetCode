def kidsWithCandies(candies, extraCandies):
    maxCandies = 0
    output = []
    for i in range(len(candies)):
        currCandies = candies[i]
        maxCandies = max(candies[:i] + candies[i+1:])
        if currCandies + extraCandies >= maxCandies:
            output.append(True)
        else:
            output.append(False)
    return output
    
print(kidsWithCandies([2,3,5,1,3], 3)) # [true,true,true,false,true] 

        