class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        curr=[]
        def dfs(i, diff):
            if diff==0:
                res.append(curr.copy())
                return
            if i>=len(nums) or diff<0:
                return
            # include ith element
            curr.append(nums[i])
            dfs(i+1, diff-nums[i])

            # Don't include ith element
            curr.pop()
            # skip all elements same as nums[i] to avoid duplicates. Cause we already used a path which used element with equal value
            while i+1<len(nums) and nums[i]==nums[i+1]:
                i+=1
            dfs(i+1, diff)
        
        dfs(0, target)
        return res
