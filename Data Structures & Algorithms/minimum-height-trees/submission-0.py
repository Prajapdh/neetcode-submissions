class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        edgeMap=collections.defaultdict(list)
        for n1,n2 in edges:
            edgeMap[n1].append(n2)
            edgeMap[n2].append(n1)
        
        def dfs(i,visited):
            h=0
            visited.add(i)
            for n in edgeMap[i]:
                if n not in visited:
                    h=max(h, 1+dfs(n,visited))
            return h

        minH=float('inf')
        res=[]
        for i in range(n):
            h=dfs(i,set())
            # print(i,h)
            if h==minH:
                res.append(i)
            elif h<minH:
                minH=h
                res=[i]
            
        return res