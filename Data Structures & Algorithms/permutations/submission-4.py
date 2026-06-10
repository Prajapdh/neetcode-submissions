class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(i):
            if i == len(nums):
                return [[]]
            perms = dfs(i + 1)
            res = []
            for perm in perms:
                for idx in range(len(perm) + 1):
                    new_perm = perm.copy()
                    new_perm.insert(idx, nums[i])
                    res.append(new_perm)
            return res

        return dfs(0)