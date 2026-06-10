class Solution:
    def trap(self, height: List[int]) -> int:
        # stores max height unitl that index
        n=len(height)
        if n==0:
            return 0
        prefix, suffix = [0]*n, [0]*n
        for i in range(n):
            prefix[i]=max(prefix[i-1], height[i]) if i>0 else height[0]
            suffix[n-1-i]=max(suffix[n-i], height[n-1-i]) if i>0 else height[n-1]

        res=0
        for i in range(n):
            res+=min(prefix[i], suffix[i])-height[i]
        return res
