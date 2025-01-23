# given a Binary tree find the avg of the numbers at each level
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# sol
def averageOfLevels(root) -> list[float]:
    def bfs(root, arr): # traverse the tree using BFS so that we can traverse each lvl one by one
        queue = [root]
        while queue:
            lvlsum = []
            level_size = len(queue)
            for _ in range(level_size): # loop over the size of the queue meaning the number of nodes at each lvl so that we can find the avg
                current = queue.pop(0)
                lvlsum.append(current.val) # append the value of the node to the lvlsum list
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            avg = sum(lvlsum) / len(lvlsum) # find the avg of the lvlsum list meaning the avg of the numbers at each lvl
            arr.append(avg) # append the avg to the array
    avgarray = [] # create an array to store the avgs
    bfs(root, avgarray) # traverse the tree
    return avgarray # return the avg array

# test cases
# tree = [3,9,20,None,None,15,7]
# Output: [3.0,14.5,11.0]

