class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        n=len(nums)
        l,r=0,n-1
        if nums[r]<target:
            return r+1
        while l<r:
            m=(r-l)//2+l
            print(l,m,r)
            if nums[m]==target:
                return m
            elif nums[m]<target:
                l=m+1
            else:
                r=m
        return l