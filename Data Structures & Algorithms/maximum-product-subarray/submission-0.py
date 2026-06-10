class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # observation:
        # all positive -> multiply all
        # even negatives -> mulitply all
        # odd negatives -> set one of the negatives as pivot and multiply both sides to find max
        # contains zero -> set the product as 1 and then continue multiplying
        prefix, suffix = 1,1
        n=len(nums)
        res=float('-inf')
        for i in range(n):
            # if prefix or suffix becomes 0, reset them to 1
            if prefix==0: prefix=1
            if suffix==0: suffix=1
            
            prefix = prefix*nums[i]
            suffix = suffix*nums[n-1-i]
            res=max(prefix, suffix, res)
        
        return res