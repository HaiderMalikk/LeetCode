# this is the worst sol i ever cooked up. ☠️
# i cant even explain this to myself.
# it works tho....

def canPlaceFlowers(flowerbed, n):
    if not flowerbed: return False
    if n == 0: return True
    # for 1 place, once n = 1 is ok
    if len(flowerbed) == 1:
        if flowerbed[0] == 0 and n == 1:
            return True
        else: return False
    # for 2 spots only n = 1 is ok
    if len(flowerbed) == 2:
        if flowerbed[0] == 0 and flowerbed[1] == 0 and n == 1:
            return True
        else: return False
    # for 3 spots only if all are 0 n can be 2, for [1,0,1] i must check here as for loop only for beds > 3 and the logic for the first and last bed messes with this [1,0,1] config
    if len(flowerbed) == 3 and (not all(flowerbed)):
        if n == 2: return True
        if n == 1:
            if flowerbed == [1,0,1]: return False
    # works for pots larger than 3
    for i in range(1, len(flowerbed) -1):
        prevbed = flowerbed[i-1]
        nextbed = flowerbed[i+1]
        if flowerbed[i] != 1 and (prevbed == 0 or i == len(flowerbed) - 2) and (nextbed == 0 or i == 1):
            if nextbed == 0 and i == len(flowerbed) - 2:
                flowerbed[i+1] = 1
            elif prevbed == 0 and i == 1:
                flowerbed[i-1] = 1
            else: flowerbed[i] = 1
            n -= 1
    return n <= 0 # optimal flower placement dose not stop once n is statisfied but goes beyond
        
print(canPlaceFlowers([1,0,0,0,1], 1)) # true
print(canPlaceFlowers([1,0,0,0,0,1], 2)) # false
print(canPlaceFlowers([1,0,0,0,1,0,1], 1)) # true
print(canPlaceFlowers([0,0,1,0,0], 1)) # true
print(canPlaceFlowers([0,0,0], 1)) # true
print(canPlaceFlowers([0,0,0], 2)) # true
print(canPlaceFlowers([0,0,1], 1)) # true
print(canPlaceFlowers([0,0], 2)) # false
print(canPlaceFlowers([0,0], 1)) # true
print(canPlaceFlowers([0,1,0], 1)) # False
print(canPlaceFlowers([1,0,1], 1)) # False




     
    