def isPowerOfFour(n: int) -> bool:
    if n in {1, 4}: # same as saying is x = 1 or x = 4
        return True # 4^0 = 1 4^1= 4 both 1, 4 are pow of 4
    while n > 4: # while n > 4 once the number n is below 4 it can no longer be a power of 4 Ex: 3
        n = n / 4 # turns out any power of 4 when divided by 4 will eventually equal to 4 (works for all numbers in fact i can replace all 4s by any numbers power i want to find)
        if n == 4: # when n dose == 4 we have a power of 4
            return True
    return False # if we devide x by 4 and its less than 4 its no longer a power of 4

print(isPowerOfFour(1))
print(isPowerOfFour(16))
print(isPowerOfFour(64))
print(isPowerOfFour(11))

# for 64: 
# 64/4 = 16; 16 != 4: 16 not power of 4, 16 > 4, run again
# 16/4 = 4: 4 == 4: True 64 is power of 4