# fix testcase (1,0) 1 (2) 1

def merge(nums1, m, nums2, n):
    idx1 = 0
    idx2 = 0
    for _ in range(n):
        if m == 0:
            nums1.insert(idx1, nums2[idx2])
            nums1.pop()
            idx1 += 1
            idx2 += 1
            continue
        found = False
        if nums1[idx1] <= nums2[idx2]:
            for i in range(idx1, m):
                if nums1[i] >= nums2[idx2]:
                    nums1.insert(i, nums2[idx2])
                    nums1.pop()
                    idx1 += 2
                    idx2 += 1
                    found = True
                    break
            if found is not True:
                nums1.insert(i + idx1, nums2[idx2])
                nums1.pop()
                idx1 += 1
                idx2 += 1
        else:
            nums1.insert(idx1, nums2[idx2])
            nums1.pop()
            idx1 += 2
            idx2 += 1
        
    
    print(nums1)
      

merge([1,0], 1, [2], 1)
