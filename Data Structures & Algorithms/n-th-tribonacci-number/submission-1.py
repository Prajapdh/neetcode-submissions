class Solution:
    def tribonacci(self, n: int) -> int:
        dp=[-1]*(n+1) if n>2 else [-1]*3
        dp[0]=0
        dp[1]=1
        dp[2]=1
        # print(dp)
        for i in range(n+1):
            if dp[i]==-1:
                dp[i]=dp[i-1]+dp[i-2]+dp[i-3]
        # print(dp)
        return dp[n]