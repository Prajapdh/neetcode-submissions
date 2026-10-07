# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodeCount=[0]
        def dfs(node):
            if not node:
                return -1
            left=dfs(node.left)
            nodeCount[0]+=1
            if(nodeCount[0]==k):
                return node.val
            right=dfs(node.right)
            if left!=-1 or right!=-1:
                return left if left!=-1 else right
            return -1
        return dfs(root)       