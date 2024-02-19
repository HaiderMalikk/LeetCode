def PowerOfTwo(x: int) -> bool: # GENIUS SOLUTION (kinda)
    if x == 1: # base case: any number rasied to the power of zero is one including 2
        return True # is power fo two 2^0 = 1
    
    # Method: the multiplyer of used to multiply the multiplyer itself until we reach x
    # the power of 2 means 2 * 2 * 2 ...... should give us x eventualy if x is a power of 2
    multiplyer = 2
    while multiplyer <= x: # run the loop until multiplyer is less than x for ex: if x = 5 after second iteration it will break and return False because multiplyer will be 10 (5 * 2) but note the multiplyer if more than the given integer x it cant be power of two for any x
        if x == multiplyer: # until we reach x by multiplying 2 * 2 * 2 n times
            return True # once our number x is a power of 2
        multiplyer = multiplyer * 2 # if x was not a power of 2 the first time multiply by 2

    return False # if nothing works not a power of 2

print(PowerOfTwo(1)) # True
print(PowerOfTwo(16)) # true
print(PowerOfTwo(3)) # false

# Example
# x = 16
# multiplyer = 2
# 2 <= 16 run while loop as multiplyer(2) is < x(16)
# 16 != 2 if statement false
# 2 * 2 = 4 or multiplyer = multiplyer * 2, now multiplyer = 4
# 4 <= 16 While loop cont...
# 4 != 16 if statement false again
# 4 * 2 = 16 or multiplyer = multiplyer * 2 now multiplyer = 8
# 8 <= 16 While loop cont...
# 8 != 16 if statement false again
# 8 * 2 = 16, multiplyer = multiplyer * 2 now multiplyer = 16
# 16 <= 16 While loop cont...
# 16 == 16 if statement true 16 is power of 2
# note if our x was 15 on the last iniration multiplyer is 16 but x is 15 now multiplyer is not <= x and the loop would stop and return false indeed 15 is not a power of 2
