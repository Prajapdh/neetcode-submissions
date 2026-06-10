class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        res=[0]
        def dfs(i,lastNum, currLen):
            if i>=len(nums):
                res[0]=max(res[0],currLen)
                return
            # pick this number in subsequence
            if nums[i]>lastNum:
                dfs(i+1,nums[i], currLen+1)
            # Don't pick
            dfs(i+1, lastNum, currLen)
        
        dfs(0,float('-inf'),0)
        return res[0]
