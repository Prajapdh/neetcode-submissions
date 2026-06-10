class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        count={}
        for n in nums:
            if n not in count:
                count[n]=0
            count[n]+=1
        
        res=[]
        curr=[]
        def dfs():
            if len(curr)==len(nums):
                res.append(curr.copy())
                return
            # lets pick unique elements to add to curr
            for n in count.keys():
                if count[n]>0:
                    curr.append(n)
                    count[n]-=1
                    dfs()
                    count[n]+=1
                    curr.pop()
        
        dfs()
        return res