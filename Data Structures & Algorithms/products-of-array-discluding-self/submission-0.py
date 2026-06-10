class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        res=[1]
        # store prefix in the output array
        prefix=1
        for i in range(len(nums)-1):
            prefix = prefix*nums[i]
            res.append(prefix)
        
        # multify the postfix with the prefix and store it
        postfix=1
        for i in range(len(nums)-1, -1, -1):
            res[i] = res[i]*postfix
            postfix=postfix*nums[i]

        return res