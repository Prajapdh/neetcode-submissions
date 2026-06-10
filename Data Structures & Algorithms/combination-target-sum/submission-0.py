class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # T.C.: O(2^target)

        res=[]

        def dfs(i, curr, total):
            if total==target:
                res.append(curr.copy())
                return
            if i>=len(nums) or total>target:
                return
            
            # All combinations with nums[i]
            curr.append(nums[i])
            dfs(i, curr, total+nums[i])
            curr.pop()

            # All combinations without nums[i]
            dfs(i+1, curr, total)
        
        dfs(0,[], 0)
        return res