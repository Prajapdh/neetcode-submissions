class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        # len of longest subarray with abs diff between ANY two ele less than or equal to limit
        # use monotonically increasing queue, stores indices
        minQueue=collections.deque()
        # use monotonically decreasing queue
        maxQueue=collections.deque()
        l,r=0,0
        res=0
        for r in range(len(nums)):
            while minQueue and nums[minQueue[-1]]>nums[r]:
                minQueue.pop()
            minQueue.append(r)
            while minQueue[0]<l:
                minQueue.popleft()

            while maxQueue and nums[maxQueue[-1]]<nums[r]:
                maxQueue.pop()
            maxQueue.append(r)
            while maxQueue[0]<l:
                maxQueue.popleft()
            
            while maxQueue and minQueue and limit<abs(nums[maxQueue[0]]-nums[minQueue[0]]):
                # print(f"max: {nums[maxQueue[0]]}, min: {nums[minQueue[0]]}")
                if maxQueue[0]<minQueue[0]:
                    l=maxQueue.popleft()+1
                else:
                    l=minQueue.popleft()+1
                # print(f"l: {l}, r: {r}")

            res = max(res, r-l+1)
        return res   
            


