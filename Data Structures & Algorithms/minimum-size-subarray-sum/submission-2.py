class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixSum=[0]
        for n in nums:
            val = n+prefixSum[-1]
            prefixSum.append(val)
        # print(prefixSum)
        n=len(nums)
        res = n+1
        for i in range(n):
            l, r = i, n
            while l<r:
                mid = (r-l)//2+l
                curSum = prefixSum[mid+1]-prefixSum[i]
                if curSum>=target:
                    # if window sum is greater, try to shrink the window from [i, r] to [i, mid]
                    r=mid
                else:
                    # Increase the size of window
                    l=mid+1
            if l!=n:
                res=min(res, l-i+1)
        return res%(n+1)