# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def SameTree(self, r1,r2):
            if not r1 and not r2:
                return True
            elif r1 and r2 and r1.val==r2.val:
                return self.SameTree(r1.left, r2.left) and self.SameTree(r1.right, r2.right)
            else:
                return False

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True
        elif not root and subRoot:
            return False
        if self.SameTree(root,subRoot):
            return True
        left=self.isSubtree(root.left, subRoot)
        right=self.isSubtree(root.right, subRoot)
        return left or right
        
        