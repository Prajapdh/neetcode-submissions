"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # usinng BFS
        if not node:
            return None
            
        oldToNew={}
        queue=collections.deque()
        oldToNew[node]= Node(node.val)
        queue.append(node)

        while queue:
            curr=queue.popleft()
            for nei in curr.neighbors:
                # Create the copy of neighbors
                if nei not in oldToNew:
                    oldToNew[nei]= Node(nei.val)
                    queue.append(nei)
                # append the copies of neighbors to the copy node
                oldToNew[curr].neighbors.append(oldToNew[nei])


        return oldToNew[node]