# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def visit(self, node: Optional[TreeNode]):
        if node is not None:
            tmp = node.left
            node.left = node.right
            node.right = tmp
            self.visit(node.left)
            self.visit(node.right)
        
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.visit(root)
        
        return root