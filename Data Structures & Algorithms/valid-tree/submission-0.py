class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        # Create an adjacency list for this non directed graph
        adjList={i:[] for i in range(n)}
        for n1,n2 in edges:
            adjList[n1].append(n2)
            adjList[n2].append(n1)
        
        # A graph is considered valid when all nodes are connected and there isn't any cylce in graph
        # We will keep track of prev node
        visited=set()

        def dfs(node, prev):
            if node in visited:
                return False
            visited.add(node)

            for nei in adjList[node]:
                if nei==prev:
                    continue
                if not dfs(nei, node):
                    return False
            return True
        
        return dfs(0, -1)  and (n==len(visited))