# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, root1, root2):
        #both empty
        if root1 == None and root2 == None:
            return None
        
        #both non-empty
        if root1 is not None and root2 is not None:
            root1.val = root1.val + root2.val
            root1.left = self.visit(root1.left, root2.left)
            root1.right = self.visit(root1.right, root2.right)
            return root1
        
        #one is empty
        return root1 or root2
        
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        return self.visit(root1, root2)