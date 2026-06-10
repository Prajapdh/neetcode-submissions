class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minHeap=[]
        for point in points:
            dist= point[0]*point[0] + point[1]*point[1]
            heapq.heappush(minHeap, (dist, point))
        
        res=[]
        for i in range(k):
            res.append(heapq.heappop(minHeap)[1])
        
        return res