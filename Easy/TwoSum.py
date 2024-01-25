class Solution: # two sum
    def TwoSum(array, target):  #ignore this # sourcery skip: instance-method-first-arg-name 
        n = len(array)
        for i in range(n - 1): # sliding window selects every element until the second last one as there would be nothing after last element to compare with
            for j in range(i + 1, n): # for every element look at the next index do this goes until the last element as we can compare it with last element - 1
                if array[i] + array[j] == target: # if any element and the element after it add to our target
                    return f'Index numbers: [{i} {j}],  Index Values: [{array[i]} {array[j]}]' # found
        return ("no two sum") # not found
        
Array = [1 ,3 , 5, 9, 11]
Target = 8 # 3 + 5

solution = Solution.TwoSum(Array, Target)
print(solution)
    
    
    