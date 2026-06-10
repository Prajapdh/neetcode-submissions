class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = set()
        for n in nums:
            if n in numbers:
                return True
            numbers.add(n)
        return False
         