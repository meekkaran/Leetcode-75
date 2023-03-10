# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        self.depth(root)
        return self.ans
    def depth(self,node):
        if node == None: return 0
        leftDepth = self.depth(node.left)
        rightDepth = self.depth(node.right)

        self.ans = max(self.ans, leftDepth + rightDepth)
        return max(leftDepth,rightDepth) +1
