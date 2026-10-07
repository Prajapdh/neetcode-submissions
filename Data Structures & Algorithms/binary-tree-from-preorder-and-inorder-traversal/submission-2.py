# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not inorder and not preorder:
            return None
        
        indices={val:idx for idx,val in enumerate(inorder)}
        pre_idx=[0]

        # l and r are limits for inorder
        def dfs(l,r):
            if l>r:
                return None

            nodeVal=preorder[pre_idx[0]]
            node=TreeNode(nodeVal)
            pre_idx[0]+=1

            node.left=dfs(l, indices[nodeVal]-1)
            node.right=dfs(indices[nodeVal]+1,r)
            return node
        
        return dfs(0, len(inorder)-1)
            