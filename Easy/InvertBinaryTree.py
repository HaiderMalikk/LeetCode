# invert binary tree i.r flip the tree
""" 
Ex 
   1
  / \
 2   3
becomes 
   1
  / \
 3   2
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def invertTree(root):
    def invert(root): # invert the tree
        if root is None: # if the root is none the return as it has no left or right children to invert
            return
        root.left, root.right = root.right, root.left # swap the left and right children at each node
        invert(root.left) # invert the left subtree
        invert(root.right) # invert the right subtree
    invert(root) # invert the tree
    return root # return the inverted trees root

# test cases
# root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]
