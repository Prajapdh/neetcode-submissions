class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minHeap=[]
        for n in nums:
            heapq.heappush(minHeap, n)
            while len(minHeap)>k:
                heapq.heappop(minHeap)
        
        return minHeap[0]