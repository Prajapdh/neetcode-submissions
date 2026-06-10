class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        curSum=0
        l=0
        for r in range(len(nums)):
            curSum+=nums[r]
            while curSum>=target:
                print(curSum, l,r,r-l+1)
                res=min(res, r-l+1)
                curSum-=nums[l]
                l+=1
        if res!=float('inf'):
            return res
        return 0