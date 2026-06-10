# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        values=[]
        def traverse(node, values):
            if not node:
                return
            if node.left: traverse(node.left, values)
            values.append(node.val)
            if node.right: traverse(node.right, values)
        traverse(root, values)
        print(values)
        return values[k-1]