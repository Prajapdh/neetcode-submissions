class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # BFS with priority queue
        adjList={}
        for u,v,w in times:
            if u not in adjList:
                adjList[u]=[]
            adjList[u].append((v,w))
        
        visited=set()
        minHeap=[(0,k)]
        res=0
        while minHeap:
            time, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            res=max(time, res)
            if node in adjList:
                for nei, neiTime in adjList[node]:
                    if nei not in visited:
                        heapq.heappush(minHeap, (neiTime+time, nei))
        
        return res if len(visited)==n else -1