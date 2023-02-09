# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    #O(log(n) )time and space
    res = -1
    count = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.inOrder(root,k)
        return self.res

    def inOrder(self,root,k):
        if not root:return 
        self.inOrder(root.left,k)
        self.count += 1
        if self.count == k:
            self.res = root.val
            return None
        self.inOrder(root.right,k)
