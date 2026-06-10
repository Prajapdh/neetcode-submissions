# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node: Optional[TreeNode], left: int, right: int)->bool:
            if not node:
                return True
            if (node.val<=left or node.val>=right):
                return False
            # the max value the node's left subtree can get is the node.val-1. loowest bound can be -inf
            # the min value the node's right subtree can get is node.val+1.
            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))
        
        return valid(root, float("-inf"), float("inf"))