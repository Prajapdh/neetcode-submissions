# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        res=[]
        # pre order traversal
        def dfs(node):
            if not node:
                res.append('N')
                return
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return ",".join(str(n) for n in res)
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        print(data)
        values=data.split(',')
        self.i=0
        def dfs():
            if self.i>=len(values):
                return None
            node=None
            if values[self.i].isdigit():
                node=TreeNode(int(values[self.i]))
                self.i+=1
                node.left=dfs()
                self.i+=1
                node.right=dfs()
            return node
        return dfs()
