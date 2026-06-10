class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        def dfs(i,lastNum, currLen):
            if i>=len(nums):
                return currLen
            pick=nonPick=0
            # pick this number in subsequence
            if nums[i]>lastNum:
                pick=dfs(i+1,nums[i], currLen+1)
            # Don't pick
            nonPick = dfs(i+1, lastNum, currLen)
            return max(pick, nonPick)
        
        return dfs(0,float('-inf'),0)
