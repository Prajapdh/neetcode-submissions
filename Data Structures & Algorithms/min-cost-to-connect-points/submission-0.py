class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # Minimum Spanning Tree
        # Applying Prim's Algo
        totalCost=0
        visited=set()
        minHeap=[(0,0)] #We will store: Weight, PointIndex
        while len(visited)<len(points):
            # Get the path with least weight
            cost, pointIndex= heapq.heappop(minHeap)
            # Traverse it only if its not visited before
            if pointIndex not in visited:
                visited.add(pointIndex)
                totalCost+=cost
                # Find all possible edges from this point
                for i,p in enumerate(points):
                    if i!=pointIndex:
                        heapq.heappush(minHeap, (abs(points[pointIndex][0]-p[0]) + abs(points[pointIndex][1]-p[1]), i))
        
        return totalCost
                