# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        large = max(p.val,q.val)
        small = min(p.val,q.val)
        while root:
            if root.val < small:
                root = root.right
            elif root.val > large:
                root = root.left
            else:
                return root
        return None
