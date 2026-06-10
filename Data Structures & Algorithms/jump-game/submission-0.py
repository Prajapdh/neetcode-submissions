class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True
        jumpsRemain=nums[0]
        for i,n in enumerate(nums):
            if((jumpsRemain-1)<n): jumpsRemain=n
            else: jumpsRemain-=1
            print(jumpsRemain)
            if(jumpsRemain==0 and i!=len(nums)-1): return False
        
        return True