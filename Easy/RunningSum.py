def RunningSum(array):
    for i in range(1, len(array)): # start at index 1 as index 0 - 1 DNE so we start at 2nd element and add the first one to it
        array[i] += array[i - 1] # each element of the array is updated as we go so we have the sum of the array before the ith element 

    return array

array = [1, 2, 3, 4, 5] # ruuning sum => [1, 2+1, 3+3, 4+6, 5+10]

print(RunningSum(array))