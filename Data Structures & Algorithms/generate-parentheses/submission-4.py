class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # open var to track open braces
        res = []
        def dfs(open, curr):
            if open==0 and len(curr)==2*n:
                res.append(curr)
                return
            if open<0 or open>n or len(curr)>=2*n:
                return
            # add open
            curr+='('
            open+=1
            dfs(open, curr)
            open-=1
            curr=curr[:-1]
            if open>0:
                curr+=')'
                open-=1
                dfs(open, curr)
                curr=curr[:-1]
                open+=1
        dfs(0, "")
        return res