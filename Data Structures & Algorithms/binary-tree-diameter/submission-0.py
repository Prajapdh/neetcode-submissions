# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=[0]
        def dfs(node):
            if not node and not node.left and not node.right:
                return 0
            left,right=0,0
            if node.left: left=dfs(node.left)
            if node.right: right=dfs(node.right)
            res[0]=max(res[0], left+right)
            return 1+max(left,right)
        dfs(root)
        return res[0]

            