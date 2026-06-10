class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        subset=[]
        def dfs(i, currSum):
            if i==len(nums) or currSum>target:
                if currSum==target: res.append(subset.copy())
                return
            subset.append(nums[i])
            dfs(i, currSum+nums[i])
            subset.pop()
            dfs(i+1, currSum)
        dfs(0, 0)
        return res