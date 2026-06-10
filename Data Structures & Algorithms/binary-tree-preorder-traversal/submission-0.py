# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def dfs(curr):
            if not curr:
                return
            res.append(curr.val)
            if curr.left:
                dfs(curr.left)
            if curr.right:
                dfs(curr.right)
        
        dfs(root)
        return res