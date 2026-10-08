class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # permutation -> rearrange elements
        # [1] -> [[2,1], [1,2]] -> [[3,2,1], [2,3,1], [2,1,3], ....]
        # avoid duplicates -> every permutation is unique cuz unique elements
        def dfs(i, perms):
            if(i>=len(nums)):
                return perms
            print(i, perms)
            newPerms=[]
            for perm in perms:
                for j in range(len(perm)+1):
                    newPerm=perm.copy()
                    newPerm.insert(j,nums[i])
                    newPerms.append(newPerm)
            return dfs(i+1, newPerms)
        return dfs(0,[[]])
        