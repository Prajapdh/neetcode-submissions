class Solution:
    def combinationSum2(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=set()
        curr=[]
        def dfs(i, diff):
            if diff==0:
                res.add(tuple(curr.copy()))
                return
            if i>=len(nums) or diff<0:
                return
            # Include
            curr.append(nums[i])
            dfs(i+1, diff-nums[i])
            # Don't include
            curr.pop()
            dfs(i+1, diff)
        
        dfs(0,target)
        return [list(t) for t in res]