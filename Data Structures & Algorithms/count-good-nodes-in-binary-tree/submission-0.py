# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=[0]
        if not root:
            return res[0]
        
        maxValue=[root.val]
        def traverse(node, maxValue, res):
            if not node:
                return
            maxValue.append(max(maxValue[-1], node.val))
            if(node.val >= maxValue[-1]):
                res[0]+=1
                
            
            if node.left: traverse(node.left, maxValue, res)
            if node.right: traverse(node.right, maxValue, res)

            maxValue.pop()

        traverse(root, maxValue, res)
        return res[0]