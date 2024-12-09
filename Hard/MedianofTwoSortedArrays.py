def findMedianSortedArrays(nums1: list[int], nums2: list[int]) -> float:
        def QuickSort(array):
            if len(array) <= 1:
                return array
        
            pivot = array[0]
            left = [x for x in array[1:] if x < pivot]
            right = [x for x in array[1:] if x >= pivot] 

            return QuickSort(left) + [pivot] + QuickSort(right)
    
        merged = QuickSort(nums1 + nums2)

        n = len(merged)

        if n % 2 == 0:
            return float((merged[n // 2 - 1] + merged[n // 2]) / 2.0)
        else:
            return float(merged[n // 2])
             
print(findMedianSortedArrays([1,3],[2])) # 2.0
print(findMedianSortedArrays([1,2],[3,4])) # 2.5