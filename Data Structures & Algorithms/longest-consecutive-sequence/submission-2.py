class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums.sort()
        seen=set(nums)
        longest=0
        streak=0
        for num in seen:
            if (num-1) not in seen:
                streak=1
                while (num+streak) in seen:
                    streak+=1
                longest = max(streak, longest)
        return longest