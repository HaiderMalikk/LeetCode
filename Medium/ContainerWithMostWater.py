def maxArea(height):
    maxArea = 0
    for i in range(0, len(height)-1):
        for j in range(1, len(height)):
            width = j - i
            maxheight = int(min(height[i], height[j]))
            Area = width * maxheight
            if Area > maxArea:
                maxArea = Area
    
    return maxArea
    
print(maxArea([1,8,6,2,5,4,8,3,7]))
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49