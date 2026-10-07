# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, node: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not node:
            return None
        
        if node.val==key:
            # No right subtree: promote the left subtree.
            # This also handles a leaf, where node.left is None.
            if not node.right:
                return node.left

            # Find the smallest node in the right subtree.
            curr = node.right
            while curr.left:
                curr = curr.left

            # Preserve the left subtree, then promote the right subtree.
            curr.left = node.left
            return node.right
        elif node.val>key:
            # print("going left")
            node.left=self.deleteNode(node.left, key)
        else:
            # print("going right")
            node.right=self.deleteNode(node.right, key)
        return node