class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # Graph with numerator: [edge, denominator]
        # If we can reach denominator from numerator, we got our answer, else -1
        adjList=defaultdict(list)
        for i in range(len(equations)):
            adjList[equations[i][0]].append((values[i],equations[i][1]))
            adjList[equations[i][1]].append((1/values[i],equations[i][0]))
        print(adjList)
        visited=set()
        def dfs(n,d):
            if n not in adjList or d not in adjList:
                return -1
            if n==d:
                return 1
            visited.add(n)
            for i in range(len(adjList[n])):
                if adjList[n][i][1] not in visited:
                    val=adjList[n][i][0]*dfs(adjList[n][i][1],d) 
                    print(n, adjList[n],i,val)
                    if val>=0:
                        return val
            return -1        

        res=[]
        for n,d in queries:
            visited=set()
            val=dfs(n,d)
            res.append(val if val>=0 else -1)
        return res