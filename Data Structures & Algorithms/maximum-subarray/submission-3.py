class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # brute force
        # sliding window(change window if currentSum < 0)
        curr=0
        res=float('-inf')
        for r in range(len(nums)):
            curr+=nums[r]
            res=max(res, curr)
            if curr<0:
                curr=0
        return res
