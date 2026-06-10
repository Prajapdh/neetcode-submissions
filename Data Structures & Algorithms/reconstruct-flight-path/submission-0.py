class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adjList=collections.defaultdict(list)
        tickets.sort()
        for a1, a2 in tickets:
            adjList[a1].append(a2)
        
        print(adjList)

        # perform DFS
        path=["JFK"]
        def dfs(src):
            print(path, len(path), len(tickets))
            # used all flight tickets
            if (len(path)==(len(tickets)+1)):
                return True
            # No outgoing paths present, cover this path at last
            if src not in adjList:
                return False
            
            temp=list(adjList[src])
            for i,dst in enumerate(temp):
                adjList[src].pop(i)
                path.append(dst)
                if dfs(dst): return True
                adjList[src].insert(i,dst)
                path.pop()
            return False

        dfs("JFK")
        return path
        

