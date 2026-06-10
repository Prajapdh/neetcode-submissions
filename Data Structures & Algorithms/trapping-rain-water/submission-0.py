class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        area=0
        l,r = 0, len(height)-1
        leftMax, rightMax = height[l], height[r]
        while(l<r):
            if(leftMax < rightMax):
                print(f"lmax<rmax. l: {l}, r: {r}, leftMax: {leftMax}, rightMax: {rightMax}")
                area+= leftMax-height[l]
                print(f"area: {area}")
                l+=1
                leftMax=max(height[l], leftMax)
            else:
                print(f"lmax>rmax. l: {l}, r: {r}, leftMax: {leftMax}, rightMax: {rightMax}")
                area+= rightMax-height[r]
                print(f"area: {area}")
                r-=1
                rightMax=max(height[r], rightMax)
        return area
            