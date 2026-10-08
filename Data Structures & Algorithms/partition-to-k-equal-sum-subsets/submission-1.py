class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        totalSum=sum(nums)
        # It is not possible to divide the number inot groups
        if totalSum%k:
            return False
        
        targetSum=totalSum//k
        groups=[0]*k    #store the sum of each group
        nums.sort(reverse=True) #Optimization to get incorrect paths first
        def dfs(i):
            if i==len(nums):
                for g in groups:
                    if g!=targetSum:
                        return False
                return True
            
            for j in range(len(groups)):
                if groups[j]+nums[i]<=targetSum:
                    groups[j]+=nums[i]
                    print(groups)
                    if dfs(i+1):
                        return True
                    groups[j]-=nums[i]
                
                # sum is bigger than expected, can't go with this path
                if groups[j]==0:
                    break
            return False
        
        return dfs(0)
                    