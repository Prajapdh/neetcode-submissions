class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(nums,i):
            # We will stop when we reach the end of the array
            if i>=len(nums):
                res.append(nums.copy())
                return
            for j in range(i,len(nums)):
                # start swaping current index with rest of the elements
                nums[j],nums[i]=nums[i], nums[j]
                dfs(nums,i+1)
                # Undo the swap
                nums[j],nums[i]=nums[i], nums[j]
        dfs(nums, 0)
        return res