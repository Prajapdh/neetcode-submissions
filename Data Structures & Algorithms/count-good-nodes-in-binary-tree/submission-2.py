# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=[0]
        def dfs(node, maxNode):
            if not node:
                return 0
            ans=1 if node.val>=maxNode else 0
            ans+= dfs(node.left, max(node.val, maxNode))
            ans+= dfs(node.right, max(node.val, maxNode))

            return ans
        return dfs(root, float('-inf'))