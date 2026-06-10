class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp=[[-1]*len(word2) for _ in range(len(word1))]
        def dfs(i,j):
            # the remaining portion of word1 is empty, we need len(word2)-j deletions
            if i==len(word1):
                return len(word2)-j
            # if no char of word2 is remain
            if j==len(word2):
                return len(word1)-i
            if dp[i][j]!=-1:
                return dp[i][j]
            if word1[i]==word2[j]:
                return dfs(i+1,j+1)
            # insert char, delete char, replace char
            dp[i][j]=min(1+dfs(i,j+1), 1+dfs(i+1,j), 1+dfs(i+1,j+1))
            return dp[i][j]
        return dfs(0,0)