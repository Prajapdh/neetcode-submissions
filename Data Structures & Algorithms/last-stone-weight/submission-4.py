class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap=[]
        for s in stones:
            heapq.heappush(maxHeap, -1*s)
        
        print(maxHeap)
        
        while len(maxHeap)>1:
            a,b=heapq.heappop(maxHeap), heapq.heappop(maxHeap)
            diff=abs(a-b)
            if diff>0:
                heapq.heappush(maxHeap, -1*diff)
            

        return -1*maxHeap[0] if maxHeap else 0