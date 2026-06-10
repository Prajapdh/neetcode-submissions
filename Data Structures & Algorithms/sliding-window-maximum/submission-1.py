class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = {}
        maxHeap = []
        res = []
        
        for r in range(len(nums)):
            window[nums[r]] = 1 + window.get(nums[r], 0)
            heapq.heappush(maxHeap, -nums[r])
            
            if r >= k - 1:  # Window full
                while maxHeap and window.get(-maxHeap[0], 0) <= 0:
                    heapq.heappop(maxHeap)
                res.append(-maxHeap[0])
                
                # Remove LEAVING element (r - k + 1)
                leaving_idx = r - k + 1
                if leaving_idx >= 0:
                    window[nums[leaving_idx]] -= 1
        
        return res
