class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3)!=len(s1)+len(s2):
            return False
        curr=[]
        dp={}

        def dfs(i,x,y):
            if i == len(s3):
                return "".join(curr) == s3
            if (x,y) in dp:
                return dp[(x,y)]

            # Check if the last char was correctly placed
            if curr and curr[-1]!=s3[i-1]:
                # print("Last char not matched")
                return False
            
            pick1,pick2=False, False
            if x<len(s1):
                curr.append(s1[x])
                pick1=dfs(i+1, x+1, y)
                curr.pop()
            if y<len(s2):
                curr.append(s2[y])
                pick2=dfs(i+1, x, y+1)
                curr.pop()
            
            dp[(x,y)]=pick1 or pick2

            return dp[(x,y)]
        
        return dfs(0,0,0)