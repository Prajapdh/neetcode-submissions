class Solution:
    def jump(self, nums: List[int]) -> int:
        res = l = r = 0
        while(r<len(nums)-1):
            farthest=0
            # find the fartehest possible point from this window
            for i in range(l,r+1):
                farthest=max(farthest, i+nums[i])
            # shift to the next window
            l=r+1
            r=farthest
            res+=1
        
        return res