# given a binary tree check if two trees are the same
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# sol
def isSameTree(p, q) -> bool:
    def traverse(root, arr): # traverse the whole tree
        if root is None: # if any node is none left or right we append none to the array marking that the left or right node is none for any leaf node
            arr.append(None)
            return
        arr.append(root.val) # if the node is not none we append the value of the node to the array
        traverse(root.left, arr) # traverse the left node
        traverse(root.right, arr) # traverse the right node
    # make two arrays and use the fact that they are reference types to traverse the trees with those arrays and then compare the arrays
    parr = [] 
    qarr = []
    traverse(p, parr)
    traverse(q, qarr)
    return parr == qarr

# test cases
""" 
p = [1,2]
q = [1,null,2]
# false
"""

        


    