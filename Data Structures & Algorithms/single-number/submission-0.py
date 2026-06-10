class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res=nums[0]
        # using XOR operation here
        # XOR of same numbers is 0, you remain with number which only exists once
        for num in nums[1:]:
            res=res^num
        
        return res