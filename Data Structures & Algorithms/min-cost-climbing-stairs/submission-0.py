class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # Output: min cost to reach top floor(len(cost))
        # Can climb 1 or 2 floors at a time
        # can start from either 1 or 2
        n=len(cost)
        dp=[-1 for _ in range(n+2)]
        dp[n]=0
        dp[n+1]=0
        for floor in range(n-1,-1,-1):
            currCost=cost[floor]+min(dp[floor+1], dp[floor+2])
            dp[floor]=currCost
        
        return min(dp[0], dp[1])