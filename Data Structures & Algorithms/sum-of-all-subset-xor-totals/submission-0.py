class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        # pick and notPick; if pick then sumXORnums[i]
        # if i>=len(nums) return sum
        def dfs(i, sum):
            if i>=len(nums):
                return sum
            pick=dfs(i+1, sum^nums[i])
            nonPick=dfs(i+1, sum)

            return pick+nonPick
        
        return dfs(0,0)