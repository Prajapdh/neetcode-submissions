class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,r=0,0
        windowSum=0
        res=float('inf')
        for r in range(len(nums)):
            windowSum+=nums[r]
            while windowSum>=target:
                res=min(res, r-l+1)
                windowSum-=nums[l]
                l+=1
        return res if res!=float('inf') else 0