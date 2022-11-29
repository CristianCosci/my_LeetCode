# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        def visit(root):
            if not root:
                return None
            elif root.val > high:
                return visit(root.left)
            elif root.val < low:
                return visit(root.right)
            else:
                root.left = visit(root.left)
                root.right = visit(root.right)
                return root
        
        return visit(root)