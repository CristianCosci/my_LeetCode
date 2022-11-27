# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isIdentical(self, root, subRoot):
        if root is None and subRoot is None:
            return True
        
        if root is not None and subRoot is not None:
            return ((root.val == subRoot.val) and
                self.isIdentical(root.left, subRoot.left) and 
                self.isIdentical(root.right, subRoot.right))
        
        return False

    def visit(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]):
        if root is not None:
            return self.isIdentical(root, subRoot) or self.visit(root.left, subRoot) or self.visit(root.right, subRoot)
        else:
            return False
            
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.visit(root, subRoot)