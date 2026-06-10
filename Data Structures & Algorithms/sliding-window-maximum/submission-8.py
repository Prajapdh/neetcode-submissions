class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # monotonically decreasing queue: stores indices. if leftmost ele ind is out of range, popleft
        queue = collections.deque()
        res=[]
        for r in range(len(nums)):
            while queue and nums[queue[-1]]<nums[r]:
                queue.pop()
            queue.append(r)
            if r>=k-1:
                # print(queue)
                while queue and queue[0]<=r-k:
                    queue.popleft()
                res.append(nums[queue[0]])
        return res