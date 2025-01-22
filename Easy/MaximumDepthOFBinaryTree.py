# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def maxDepth(root) -> int:
    if not root: return 0
    def helper(root):
        if root is None: return 0
        leftdepth = helper(root.left)
        rightdepth = helper(root.right)
        return 1 + max(leftdepth, rightdepth)       
    return helper(root)

