"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        output = []
        self.traverse(root, output)
        return output
    def traverse(self, root, output):
        if root is None: return 
        #append root
        output .append(root.val)
        #recursively traverse each node in children array
        for child in root.children:
            self.traverse(child, output)
