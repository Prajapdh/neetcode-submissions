class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2:
            return False
        
        def dfs(i, target):
            if i>=len(nums) or target<0:
                return False
            elif target==0:
                return True
            else:
                pick = dfs(i+1, target-nums[i])
                notpick = dfs(i+1, target)
                return pick or notpick

        target = sum(nums)//2
        return dfs(0, target)
