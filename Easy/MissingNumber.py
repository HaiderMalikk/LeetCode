def missingnumber(nums: list) -> int: # missing number in nums a list [0, n]
    n = max(nums) # first get the max of list so we know what number to go up to
    currentnum = 0 #  keep track of the last seen number in nums
    while currentnum <= n: # once the list max is reached stop
        if currentnum not in nums: # from 0 till n look at every integer and check if that current num is in the list nums
            return currentnum # if current num not in nums return it
        currentnum += 1 # increment from last seen number +1 so that we can compare each element from 0 to n and so the loop stops
    else:
        return currentnum # if the list is complete return the int after max since we did current num += 1 the curent num is the num after the completed lists max num

print(missingnumber([0, 1,]))  # Output: 2
print(missingnumber([0, 1, 2 ,3 ,5])) # Output: 4
print(missingnumber([9,6,4,2,3,5,7,0,1])) # Output: 8
