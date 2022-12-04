"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
class Solution:
    def __init__(self):
        self.to_return = []
    
    def visit(self, root: 'Node'):
        if root is not None:
            self.to_return.append(root.val)
            for i in root.children:
                self.visit(i)
            
            
    def preorder(self, root: 'Node') -> List[int]:
        self.visit(root)
        return self.to_return