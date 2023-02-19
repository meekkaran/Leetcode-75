# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: return 
        return self.swap(root.left,root.right)
    
    def swap(self, a,b):
        if not a or not b:
            return not a and not b
        return a.val == b.val and self.swap(a.left,b.right) and self.swap(a.right,b.left)
