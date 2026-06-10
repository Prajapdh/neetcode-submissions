class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        def dfs(i, curr):
            # end of decision tree reached
            if i>=len(nums):
                res.append(curr.copy())
                return
            
            # pick nums[i]
            curr.append(nums[i])
            dfs(i+1, curr)
            curr.pop()

            # don't pick nums[i]
            # skiping all duplicate elements because we decided not to pick nums[i]
            while(i+1<len(nums) and nums[i+1]==nums[i]):
                i+=1
            dfs(i+1, curr)
        
        dfs(0,[])
        return res