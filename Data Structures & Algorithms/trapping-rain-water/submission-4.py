class Solution:
    def trap(self, height: List[int]) -> int:
        n=len(height)
        preMax,sufMax=[0]*n,[0]*n
        for i in range(1, n):
            preMax[i]=max(preMax[i-1],height[i-1], height[i])
            sufMax[n-i-1]=max(sufMax[n-i],height[n-i], height[n-i-1])
        
        print(preMax)
        print(sufMax)
        res=0
        for i in range(n):
            res+= 0 if min(sufMax[i], preMax[i])-height[i]<=0 else min(sufMax[i], preMax[i])-height[i]
        return res