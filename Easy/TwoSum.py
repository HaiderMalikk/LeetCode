# TWO SUM
#! better hash table solutiondef two_sum(nums, target):
def two_sum(nums, target):
    # Create a hash table to store the complement and its index
    # the comliment is target - nums[i] lets say we have 2, 7, 11, 15 and we want to find 9 the answer is 2 and 7 as 2+7 =9
    # So the compliment at first is 9 - 2 = 7 where num is 2 if we find that 7 is in the hash table we can return the index
    # or else we add the current value to the hash table now we have 7 in the table and we run the loop again
    # this time compliment is 9 - 7 = 2 and we find that 7 our last compliment is in the hash table we can return the index
    # so essentialy we added the element 7 to the hash map as nothing in the hash map whe added with 7 gave 9
    # but now 2 our compliment when added with 7 the value in our hash map is 9 so we return the number we found in hashmap, current number in array
    hash_table = {}
    
    for i in range(len(nums)):  # Regular for loop to iterate by index
        num = nums[i]  # Get the value at index i
        complement = target - num
        
        # Check if the complement exists in the hash table
        if complement in hash_table:
            return [hash_table[complement], i]
        
        # If complement is not found, add the current number to the hash table
        hash_table[num] = i
    
    # If no solution is found
    return None

# Example usage:
nums = [2, 7, 11, 15]
target = 9
result = two_sum(nums, target)
print(result)  # Output: [0, 1] = [2, 7]




#! alternitive solution, this is not the best solution as its time complexity is O(n^2)
# def TwoSum_bad_solution(array, target):  #ignore this # sourcery skip: instance-method-first-arg-name 
#     n = len(array)
#     for i in range(n - 1): # sliding window selects every element until the second last one as there would be nothing after last element to compare with
#         for j in range(i + 1, n): # for every element look at the next index do this goes until the last element as we can compare it with last element - 1
#             if array[i] + array[j] == target: # if any element and the element after it add to our target
#                 return f'Index numbers: [{i} {j}],  Index Values: [{array[i]} {array[j]}]' # found
#     return ("no two sum") # not found
    
# Array = [1 ,3 , 5, 9, 11]
# Target = 8 # 3 + 5

# solution_mid = TwoSum_bad_solution(Array, Target)
# print(solution_mid)
    
    
    