class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        curr=[]
        def dfs(open, close):
            if len(curr)==2*n and open==close:
                res.append("".join(curr))
                return
            if not curr:
                curr.append('(')
                dfs(open+1, close)
            if open<n:
                curr.append('(')
                dfs(open+1, close)
                curr.pop()
            if open>close:
                curr.append(')')
                dfs(open, close+1)
                curr.pop()
        
        dfs(0,0)
        return res