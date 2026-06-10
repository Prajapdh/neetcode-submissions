class Solution:
    def mySqrt(self, x: int) -> int:
        l,r=0,x
        res=0
        while l<=r:
            m=(r-l)//2+l
            sq=m*m
            print(l,m,r,sq)
            if sq==x:
                return m
            elif sq>x:
                r=m-1
            else:
                l=m+1
                res=m
        return res