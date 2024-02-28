# when i was making this solution i just brute forced it plz dont use this there are better solutions out there
def lastStoneWeight(stones: list[int]) -> int: 
    stones.sort() # after sorting the largest element is x second largest is y
    while len(stones) > 1: # run untill one element is left
        x = stones[-1] # last element (largest)
        y = stones[-2] # second last element (second largest)
        if x > y:
            newrock=  x - y # new stones
            stones.pop() # pop the last stone (x)
            stones.pop() # pop the last stone (y)
            stones.append(newrock) # add the newrock to the end of list

        if x == y:# if the stones are same 
            # remove the two identical stones
            stones.pop()
            stones.pop()
            stones.append(0) # add a zero as thats the diffrence of x and y if there the same 

        stones.sort()

    return stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))
# sorted array: 1,1,2,4,7,8