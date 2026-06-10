class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack=[]  #to keep track of open braces
        res=""
        for i in range(len(s)):
            if s[i]==")" and not stack:
                continue
            elif s[i]==")" and stack:
                stack.pop()
            elif s[i]=="(":
                stack.append(len(res))
            res+=s[i]
        while stack:
            res=res[:stack[-1]]+res[stack[-1]+1:]
            stack.pop()
        
        return res
            
