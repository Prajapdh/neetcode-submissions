# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None

        if root.val<key:
            root.right=self.deleteNode(root.right, key)
        elif root.val>key:
            root.left=self.deleteNode(root.left, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            #Case when you want to delete current node
            node=root.right
            while node.left:
                    node=node.left
            node.left=root.left
            res=root.right
            del root
            return res

        # return the root for if and elif case
        return root