def isPowerOfFour(n: int) -> bool:
    if n in {1, 3}: # same as saying is x = 1 or x = 3
        return True # 3^0 = 1 3^1= 3 both 1, 3 are pow of 3
    while n > 3: # while n > 3 once the number n is below 3 it can no longer be a power of 3 Ex: 3
        n = n / 3 # turns out any power of 3 when divided by 3 will eventually equal to 3 (works for all numbers in fact i can replace all 3s by any numbers power i want to find)
        if n == 3: # when n dose == 3 we have a power of 3
            return True
    return False # if we devide x by 3 and its less than 3 its no longer a power of 3

print(isPowerOfFour(1))
print(isPowerOfFour(9))
print(isPowerOfFour(27))
print(isPowerOfFour(11))

# for 63: 
# 27/3 = 9; 9 != 3: 9 not power of 3, 9 > 3, run again
# 9/3 = 3: 3 == 3: True 27 is power of 3 