# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    # Serialize the tree using preorder traversal
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(str(node.val))
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return ','.join(res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        # Convert preorder traversal to tree
        # if any node has both of its child node as 'N', that is a leaf node and we return
        arr=data.split(',')
        # print(arr)
        idx=[0]
        def dfs():
            if arr[idx[0]]=='N':
                # if leaf node reached, move to next node
                idx[0]+=1
                return None
            node=TreeNode(int(arr[idx[0]]))
            idx[0]+=1
            node.left=dfs()
            node.right=dfs()
            return node
        
        return dfs()

