class Solution:
    def rob(self, nums: List[int]) -> int:
        # can't rob two adjacent houses
        # 2 choices: rob(i) + rob(i+2) or rob(i+1)
        # base case: if i>=n return 0
        n=len(nums)
        dp=[-1]*(n+2)
        dp[n]=0
        dp[n+1]=0
        def dfs(i):
            if i>=n:
                return 0
            if dp[i]!=-1:
                return dp[i]
            dp[i]=max(dfs(i+1), nums[i]+dfs(i+2))
            return dp[i]
        return dfs(0)