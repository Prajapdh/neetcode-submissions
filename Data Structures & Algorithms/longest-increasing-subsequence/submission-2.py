class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # First convert everything in term of indices
        # We are doing repeatative work here
        # We can't store -1 in our cache, therefore we will do coordinate shift
        # i can be stored as it is, when storing j, we store j+1 (therefore we need values from 0 to n)
        n=len(nums)
        dp=[[-1 for _ in range(n+1)] for _ in range(n)]
        # i=current index, j=previous index
        def dfs(i,j):
            if i==len(nums):
                return 0
            if dp[i][j+1]!=-1:
                return dp[i][j+1]
            # Don't include the current index
            ans=dfs(i+1,j)
            if j==-1 or nums[i]>nums[j]:
                # Increase the length by 1
                ans=max(ans, 1+dfs(i+1, i))
            dp[i][j+1]=ans
            return ans
        dfs(0,-1)
        # print(dp)
        return dp[0][0]