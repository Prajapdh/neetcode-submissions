class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # remove duplicates inplace
        # output: k where first k elements are unique
        # it is sorted in asc order
        prev=nums[0]
        res=1
        r=1
        while r<len(nums):
            if nums[r]!=prev:
                nums[res]=nums[r]
                prev = nums[r]
                res+=1
            r+=1
        return res