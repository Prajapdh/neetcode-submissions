class Solution:
    def rob(self, nums: List[int]) -> int:
        # can't rob two adjacent houses
        # 2 choices: rob(i) + rob(i+2) or rob(i+1)
        # base case: if i>=n return 0
        n=len(nums)
        dp=[-1]*(n+2)
        dp[n]=0
        dp[n+1]=0
        for i in range(n-1, -1, -1):
            dp[i]=max(nums[i]+dp[i+2], dp[i+1])
        return dp[0]