class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        res=0
        for i in range(len(nums)):
            val=nums[i]
            cnt=1
            if val-1 not in s:
                while val+1 in s:
                    cnt+=1
                    val+=1
            res=max(res, cnt)
        return res