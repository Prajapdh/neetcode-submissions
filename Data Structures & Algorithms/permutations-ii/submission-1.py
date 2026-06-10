class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = collections.defaultdict(int)
        for n in nums:
            counter[n]+=1
        res=[]
        def dfs(i, perm):
            if i==len(nums):
                res.append(perm.copy())
                return
            for k in counter.keys():
                if counter[k]==0:
                    continue
                perm.append(k)
                counter[k]-=1
                dfs(i+1, perm)
                perm.pop()
                counter[k]+=1
        
        dfs(0,[])
        return res
