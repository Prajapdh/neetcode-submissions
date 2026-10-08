# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # possible paths:
        # left-root-right, left-root-parent, right-root-parent
        res=[root.val]
        def dfs(node):
            if not node:
                return 0
            left=max(dfs(node.left),0)
            right=max(dfs(node.right),0)
            
            res[0] = max(res[0],left+node.val+right, left+node.val, right+node.val)
            # print(node.val, res[0])
            return max(left+node.val, right+node.val)
        dfs(root)
        return res[0]