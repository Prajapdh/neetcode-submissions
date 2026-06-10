class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        sett=set(nums)
        res=[]
        curr=[]
        def dfs(sett):
            if not sett:
                res.append(curr.copy())
                return
            # print(sett, curr)
            for n in sett.copy():
                curr.append(n)
                sett.remove(n)
                dfs(sett)
                sett.add(n)
                curr.pop()
        dfs(sett)
        return res