def removeElement(nums, val):
        index = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[index] = nums[i]
                index += 1

        return index

solution = removeElement([0,1,2,2,3,0,4,2], 2)
print(solution)