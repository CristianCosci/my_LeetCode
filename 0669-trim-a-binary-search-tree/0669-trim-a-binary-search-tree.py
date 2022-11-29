# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, root, low, high):
        if not root:
            return None
        elif root.val > high:
            return self.visit(root.left, low, high)
        elif root.val < low:
            return self.visit(root.right, low, high)
        else:
            root.left = self.visit(root.left, low, high)
            root.right = self.visit(root.right, low, high)
            return root
        
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        return self.visit(root, low, high)