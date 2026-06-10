class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # We will use a monotonic decreasing queue
        # only add elements to the queue if the are less than top else pop top
        # When we shift our sliding window, compare the leftmost queue element with nums[l], popleft until you remove nums[l]
        queue=deque()   #store indices of elements
        n=len(nums)
        res=[]
        l=0
        for r in range(n):
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            queue.append(r)

            # if first ele is not present in window
            if l>queue[0]:
                queue.popleft()
            
            # Add to answer for if window is formed
            if (r+1)>=k:
                res.append(nums[queue[0]])
                l+=1
        return res

