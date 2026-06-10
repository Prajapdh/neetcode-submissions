class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        # output: max sum of non-empty circular subarray
        totalSum=0
        curMax=0
        globalMax=nums[0]
        curMin=0
        globalMin=nums[0]

        for i in range(len(nums)):
            totalSum+=nums[i]
            curMax=max(curMax+nums[i], nums[i])
            globalMax=max(globalMax, curMax)
            curMin=min(curMin+nums[i], nums[i])
            globalMin=min(globalMin, curMin)
        
        return max(globalMax, totalSum-globalMin) if globalMax>0 else globalMax #max sum was in middle portion of array, or if max sum was on boundaries