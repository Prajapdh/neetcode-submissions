class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window={}
        maxHeap=[]
        res=[]
        for r in range(len(nums)):
            # print(r, window, maxHeap, res)
            window[nums[r]]=1+window.get(nums[r],0)
            heapq.heappush(maxHeap, -1*nums[r])
            if r<k-1:
                continue
            while -1*maxHeap[0] not in window or (-1*maxHeap[0] in window and window[-1*maxHeap[0]]<=0):
                heapq.heappop(maxHeap)
            res.append(-1*maxHeap[0])
            # print(r,k)
            window[nums[r-k+1]]-=1
       
        return res