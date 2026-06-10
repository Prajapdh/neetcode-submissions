class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        maxx=max(piles)
        l=1
        r=maxx
        res=float("inf")
        while l<=r:
            m=(l+r)//2
            t=0
            for p in piles:
                t+=math.ceil(p/m)
            if(t<=h):
                res=min(res,m)
                r=m-1
            else:
                l=m+1
        return res
