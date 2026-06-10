class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        n=len(nums)
        lastSeen={}
        for i,n in enumerate(nums):
            if n in lastSeen:
                if abs(lastSeen[n]-i)<=k:
                    return True
            lastSeen[n]=i

        return False