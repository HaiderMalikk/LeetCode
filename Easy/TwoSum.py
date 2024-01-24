Array = [1 ,3 , 5, 9, 11]
Target = 8 # 3 + 5

class Solution: # two sum
    def TwoSum(array, target):
        n = len(array)
        for i in range(0, n - 1):
            for j in range(i + 1, n):
                if array[i] + array[j] == target:
                    return f'Index numbers: [{i} {j}],  Index Values: [{array[i]} {array[j]}]'
        return ("no two sum")
        

print(Solution.TwoSum(Array, Target))
    
    
    