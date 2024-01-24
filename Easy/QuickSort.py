def QuickSort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    left = [x for x in array[1:] if x < pivot] # NOTE: "1:" creates a new array using array that has all of arrays elemnts starting from index 1
    right = [x for x in array[1:] if x >= pivot]

    return QuickSort(left) + [pivot] + QuickSort(right)

array = [3, 6, 8, 10, 1, 2, 1]
arr_sorted = QuickSort(array)
print(arr_sorted)

# time complexity: O(log(n))