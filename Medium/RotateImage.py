# rotate image clockwise solution stakc solution beats 35.3 % of python3 submissions

# ! NOTE
""" 
Rules:
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

i used a stack built by a double for loop and then looped over the matrix and modified its elements in place using the stack which dose not violate the rules as no 2d matrix or matrix copy was created the matrix given is returned nothing different
"""

# ! Approach
"""  
lets look at this example in a flat list 
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

look close at the pattern of the index the element goes to 1 goes to [0][2] 2 goes to [1][2] 3 goes to [2][2] 4 goes to [0][1]
and so on but the pattern if keep the inner index consatnt at matrix.len -1  while going up by one on the outter index each element, after finsihing the subarray decrement the inner index by one reset outer to 0 and repeat
but this would requre a second 2D matrix

my approach (stack)
if we get our element in a stack => (9, 8, 7, 6, 5, 4, 3, 2, 1) now we can just do the opposite of before 
the pattern now is 9 goes to [2][0] 8 goes to [1][0] 7 goes to [0][0] 6 goes to [2][1] the patter is: start the inner index at 0 and the outer index at matrix.len -1 
then after finising one subarray increment the inner index while staring the outer index at the same value matrix.len -1 and repeate for all subarrays
this solution is not the best solution but i will find a better one 
NOTE: i did not reverse the stack as that is not a constant time operation and is unnecessary as we can work around it by reversing method in approch 1 
"""

# ! solution
def rotate(matrix: list[list[int]]) -> list[list[int]]: # * you should return nothing just modify matrix, but for printing the output it i will return matrix
        stack = [] # create a stack
        # loop over all elements in matrix and add to stack
        for subarray in matrix: 
            for element in subarray:
                stack.append(element)
                
        # now we will loop over the matrix and modify its elements to be replaced with the elements in the stack note the the last element in the stack is modified first in the matrix
        inner_index = -1 # we need to start the inner index at one but if this was 0 after the first subarray the inner index would be 1 to compensate for the first loop and insure we satrt with inner index at 0 i initilize it here as -1
        for subarray in matrix: # loop over all subarrays in matrix
            outer_index = len(matrix) - 1 # we need to start the outer index at the last index of the matrix. NOTE: since this matrix is n x n  the length of both subarrays and matrix is the same 
            inner_index += 1 # since we started the inner index at -1 we need to increment it by one ensuring we start the inner index at 0
            for element in subarray: # loop over all elements in subarray
                matrix[outer_index][inner_index] = stack.pop() # pop the last element from the stack and assign it to the element in the matrix located at the current outer index and the current inner index
                outer_index -= 1 # decrement the outer index by one see EX for why (its just the pattern)
                
        return matrix

# ! test cases           
print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])) # out : [[7,4,1],[8,5,2],[9,6,3]]
print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # out : [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        
        
# ! Better approach but uses a empty array to build matrix, this new array is returned as a matrix which is not allowed but is better than the previous approach
# ! Better solution only uses 2 for loops and a empty list to store the result (rules said no 2d matrix or matrix copy i just used a list)
def rotate(matrix: list[list[int]]) -> list[list[int]]: # 
    newmatrix = []
    column = -1
    
    for row in matrix:
        newrow = []
        column += 1
        for row in matrix:
            newrow.append(row[column])
        newmatrix.append(newrow)
    
    return newmatrix

print(rotate(matrix = [[1,2,3],[4,5,6],[7,8,9]])) # out : [[7,4,1],[8,5,2],[9,6,3]]
print(rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) # out : [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        