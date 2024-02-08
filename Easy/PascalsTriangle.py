def Pascals_Triangle(numRows: int) -> list:
    # Initialize an empty list to store the triangle
    triangle = []
    
    # Loop through each row up to numRows
    for i in range(numRows):
        # Create a new row with length i+1 
        #* (i + 1): This is the repetition operator in Python. 
        # When you multiply a list by an integer Python creates 
        # a new list by repeating the elements of the original list
        # the specified number of times. In this case, (i + 1) : int
        # determines the number of times the list [1] will be repeated.
        row = [1] * (i + 1)
        
        # Update elements in the row excluding the first and last
        for j in range(1, i):
            # Each element except first and last is the sum of the two elements above it in the previous row
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        
        # Append the generated row to the triangle
        triangle.append(row)
    
    # Return the generated Pascal triangle
    return triangle


solution = Pascals_Triangle(5)
print(solution)
