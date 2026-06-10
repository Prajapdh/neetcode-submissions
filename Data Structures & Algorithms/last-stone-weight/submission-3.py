class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # using max heap
        # we will just add all the values with a negative sign in the min heap
        # Therefore top value will be greatest when its sign is inversed

        maxHeap=[-1*n for n in stones]
        heapq.heapify(maxHeap)

        while(len(maxHeap)>1):
            # get the top two elements
            x=1*heapq.heappop(maxHeap)
            y=1*heapq.heappop(maxHeap)
            if(x==y):
                continue
            else:
                diff=-1*abs(x-y)
                heapq.heappush(maxHeap, diff)
        
        return -1*maxHeap[0] if maxHeap else 0
