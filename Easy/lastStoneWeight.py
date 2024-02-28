def lastStoneWeight(stones: list[int]) -> int:
    stones.sort()
    while len(stones) > 1:
        x = stones[-1]
        y = stones[-2]
        if x > y:
            newsum =  x - y
            stones.pop()
            stones.pop()
            stones.append(newsum)

        if x == y:
            if len(stones) == 2 and stones[0] == stones[1]:
                stones.pop()
                stones.pop()
                stones.append(0)


            else:
                stones.pop()
                stones.pop()


        stones.sort()

    return stones[0]

print(lastStoneWeight([2,7,4,1,8,1]))
# sorted array: 1,1,2,4,7,8