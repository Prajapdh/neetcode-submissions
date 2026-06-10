class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # use min heap to store our distances
        # we will store a pair in min heap: distance, coordinates
        minHeap = []
        for x, y in points:
            dist = (x ** 2) + (y ** 2)
            minHeap.append([dist, x, y])
        
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            dist, x, y = heapq.heappop(minHeap)
            res.append([x, y])
            k -= 1
            
        return res