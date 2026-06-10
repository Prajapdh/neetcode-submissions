class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0, len(nums)-1
        while l<=r:
            m=(l+r)//2
            if nums[m]>nums[r]:
                l=m+1
            elif nums[m]<nums[r] and nums[m]<nums[l]:
                r=m
            elif nums[m]<nums[r] and nums[m]>nums[l]:
                r=m-1
            else:
                print(f"l: {nums[l]}, r: {nums[r]}, m: {nums[m]}")
                return nums[m]
        return -1