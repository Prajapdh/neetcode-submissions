# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder and not inorder:
            return None
        
        root=TreeNode(preorder[0])    #root is always the first element of the preorder list
        # finding the number of elements in child segments
        midIndex=inorder.index(preorder[0]) #everything to the left of mid is the left segment
        root.left= self.buildTree(preorder[1:midIndex+1], inorder[:midIndex])
        root.right= self.buildTree(preorder[midIndex+1:], inorder[midIndex+1:])

        return root
