class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res=[]
        combination=[]
        def dfs(i, diff):
            if diff==0:
                res.append(combination.copy())
                return
            elif i>=len(nums) or diff<0:
                return
            # Include ith position
            combination.append(nums[i])
            dfs(i, diff-nums[i])
            # Exclude ith position
            combination.pop()
            dfs(i+1, diff)
        
        dfs(0, target)
        return res