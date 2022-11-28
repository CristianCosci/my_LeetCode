"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def visit(self, root: 'Node', to_return):
        if root is not None:
            to_return.append(root.val)
            for i in root.children:
                self.visit(i, to_return)
            
    def preorder(self, root: 'Node') -> List[int]:
        to_return = []
        self.visit(root, to_return)
        return to_return