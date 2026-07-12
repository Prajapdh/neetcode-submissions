class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Implementing the Dijkstra's Algo
        edges=collections.defaultdict(list) #adjacency list: (target node, weight from source to target node)
        for u,v,w in times:
            edges[u].append((v,w))
        
        # We will perform BFS here
        # We will traverse the node with lowest weight first
        minHeap=[(0, k)]    #lets start from the start node, stores: (weight, target node)
        visited=set()
        res=0
        while minHeap:
            weight, target = heapq.heappop(minHeap)
            # continue if that node is already visited
            if target in visited:
                continue
            visited.add(target)
            res=weight  #updating the result value as the last value will be largest
            # traverse all neighbors of this node
            for nei, neiWei in edges[target]:
                if nei not in visited:
                    heapq.heappush(minHeap, (weight+neiWei, nei))
            
        return res if len(visited)==n else -1  
            