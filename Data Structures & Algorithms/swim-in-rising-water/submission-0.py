class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        adjList=collections.defaultdict(list)
        N=len(grid)
        for i in range(N):
            for j in range(N):
                # print(i,j)
                if i+1<N:
                    adjList[(i,j)].append((i+1,j))
                    adjList[(i+1, j)].append((i,j))
                if j+1<N:
                    adjList[(i,j)].append((i,j+1))
                    adjList[(i,j+1)].append((i,j))
                # print(adjList)
        # print(adjList)
        visited=set()
        minHeap=[(grid[0][0], (0,0))]   #weight, coordinates
        res=0

        while (N-1, N-1) not in visited:
            time, point=heapq.heappop(minHeap)
            if point not in visited:
                visited.add(point)
                res=time
                for p in adjList[point]:
                    if p not in visited:
                        heapq.heappush(minHeap, (max(grid[p[0]][p[1]], time), p))

        return res