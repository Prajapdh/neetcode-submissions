class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # edge case: return [] if k=0
        # question: will k be always k<=n?
        # question: avoid duplicate, right?
        # Time: k*(nCk)
        # Space: k*(nCk)
        res=[]
        curr=[]
        def dfs(i,len):
            if len==k:
                res.append(curr.copy())
                return
            if i>n or len>k:
                return
            curr.append(i)
            dfs(i+1, len+1)
            curr.pop()
            dfs(i+1, len)
        
        dfs(1, 0)
        return res