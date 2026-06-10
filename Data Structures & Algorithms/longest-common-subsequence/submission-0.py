class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Recurssion
        # T.C. O(2^(m+n))
        # S.C. O(m+n)
        # def dfs(i, j):
        #     if i<0 or j<0:
        #         return 0
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i - 1, j - 1)
        #     return max(dfs(i - 1, j), dfs(i, j - 1))
        
        # return dfs(len(text1)-1, len(text2)-1)

        # Dynamic Programming
        dp=[[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        def dfs(i,j):
            if i<0 or j<0:
                return 0
            if(dp[i][j]!=-1):
                return dp[i][j]
            if text1[i] == text2[j]:
                return 1 + dfs(i - 1, j - 1)
            dp[i][j]=max(dfs(i - 1, j), dfs(i, j - 1))
            return dp[i][j]
        
        return dfs(len(text1)-1, len(text2)-1)

        #Tabulation
        # dp[]