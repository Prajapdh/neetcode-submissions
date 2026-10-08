class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res=[]
        sol=[]
        def isPalindrome(s):
            l,r = 0, len(s)-1
            while l<=r:
                if s[l]!=s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def dfs(i, curr):
            if i>=len(s):
                if curr=="":
                    res.append(sol.copy())
                return
            if(isPalindrome(curr+s[i])):
                sol.append(curr+s[i])
                dfs(i+1, "")
                sol.pop()
            dfs(i+1, curr+s[i])
        
        dfs(0,"")
        return res