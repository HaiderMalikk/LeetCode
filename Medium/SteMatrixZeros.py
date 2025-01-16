def setZeroes(matrix):
    # to keep track of places we set zero (i.e places we have seen and entered zeros in, we dont modify there col/rows only thr original zeros are modified)
    seen = []
    # loop over matrixs rows
    for r in range(len(matrix)):
        # loop over matrixs columns i.e the len of the row
        for c in range(len(matrix[r])):
            # if the element is zero and we have not seen it before
            if matrix[r][c] == 0 and (r, c) not in seen:
                # loop over the whole row the zero is in and set it to zero if there was a zero where we are stting 0 dont add it to seen otherwise add it to seen and set to zero
                # this way the check above will only trigger on original zeros and not zeros we set
                for delrow in range(len(matrix[r])):
                    if matrix[r][delrow] == 0: continue  
                    seen.append((r, delrow)) 
                    matrix[r][delrow] = 0 
                # loop over the whole column the zero is in and set it to zero if there was a zero where we are stting 0 dont add it to seen otherwise add it to seen and set to zero
                for delcol in range(len(matrix)):
                    if matrix[delcol][c] == 0: continue 
                    seen.append((delcol, c))
                    matrix[delcol][c] = 0
    # the question asked us to modify the original matrix so we dont return anything but here we are returning the modified matrix for testing
    return matrix

print(setZeroes([[1,1,1],[1,0,1],[1,1,1]]))
# ex
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# [1,1,1]
# [1,0,1]
# [1,1,1]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# [1,0,1]
# [0,0,0]
# [1,0,1]
print(setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])) # Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]