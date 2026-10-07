# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, node: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Binary search tree
        if not node:
            return None
        if(p.val<node.val and q.val<node.val):
            return self.lowestCommonAncestor(node.left, p,q)
        elif(p.val>node.val and q.val>node.val):
            return self.lowestCommonAncestor(node.right, p,q)
        else:
            return node