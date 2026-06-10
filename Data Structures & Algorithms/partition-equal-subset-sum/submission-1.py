class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        target = sum(nums)//2
        memo=[[-1 for _ in range(target+1)] for _ in range(len(nums)+1)]

        def dfs(i, target):
            if i>=len(nums) or target<0:
                return False
            elif target==0:
                return True
            elif memo[i][target]!=-1:
                return memo[i][target]
            else:
                pick = dfs(i+1, target-nums[i])
                notpick = dfs(i+1, target)
                memo[i][target] = pick or notpick
                return memo[i][target]

        return dfs(0, target)
