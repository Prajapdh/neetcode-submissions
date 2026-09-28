class Solution:
    def validPalindrome(self, s: str) -> bool:
        # recursion -> two pointers
        def dfs(i,j,delCount):
            if(i>j):
                return False if delCount>1 else True
            elif(s[i]!=s[j]):
                return dfs(i,j-1,delCount+1) or dfs(i+1, j, delCount+1)
            else:
                return dfs(i+1, j-1, delCount)
        return dfs(0, len(s)-1,0)