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
        # dp=[[-1 for _ in range(len(text2))] for _ in range(len(text1))]
        # def dfs(i,j):
        #     if i<0 or j<0:
        #         return 0
        #     if(dp[i][j]!=-1):
        #         return dp[i][j]
        #     if text1[i] == text2[j]:
        #         return 1 + dfs(i - 1, j - 1)
        #     dp[i][j]=max(dfs(i - 1, j), dfs(i, j - 1))
        #     return dp[i][j]
        
        # return dfs(len(text1)-1, len(text2)-1)

        #Tabulation
        # Here shifting of indices is required because we can't have negative incides in the dp data structure
        # n-->>n-1, m-->>m-1, 1-->>0
        dp=[[-1 for _ in range(len(text2)+1)] for _ in range(len(text1)+1)]
        # Write base cases
        for i in range(len(text1)+1):
                dp[i][0]=0
        for j in range(len(text2)+1):
                dp[0][j]=0
        
        # Write exploration steps in opposite fashion
        for i in range(1,len(text1)+1):
            for j in range(1,len(text2)+1):
                if(text1[i-1]==text2[j-1]):
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    pick=dp[i][j-1]
                    notpick=dp[i-1][j]
                    dp[i][j]=max(pick, notpick)
        print(dp)
        return dp[len(text1)][len(text2)]

