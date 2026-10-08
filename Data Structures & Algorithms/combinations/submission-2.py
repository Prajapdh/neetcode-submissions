class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        comb=[]
        def dfs(i):
            if i>n or len(comb)>=k:
                if len(comb)==k: res.append(comb.copy())
                return
            comb.append(i)
            dfs(i+1)
            comb.pop()
            dfs(i+1)
        dfs(1)
        return res