class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        # Using Pointers
        # area=0
        # l,r = 0, len(height)-1
        # leftMax, rightMax = height[l], height[r]
        # while(l<r):
        #     if(leftMax < rightMax):
        #         # print(f"lmax<rmax. l: {l}, r: {r}, leftMax: {leftMax}, rightMax: {rightMax}")
        #         area+= leftMax-height[l]
        #         # print(f"area: {area}")
        #         l+=1
        #         leftMax=max(height[l], leftMax)
        #     else:
        #         # print(f"lmax>rmax. l: {l}, r: {r}, leftMax: {leftMax}, rightMax: {rightMax}")
        #         area+= rightMax-height[r]
        #         # print(f"area: {area}")
        #         r-=1
        #         rightMax=max(height[r], rightMax)
        # return area

        # Using Arrays
        n = len(height)
        if n == 0:
            return 0
        
        leftMax = [0] * n
        rightMax = [0] * n
        
        leftMax[0] = height[0]
        for i in range(1, n):
            leftMax[i] = max(leftMax[i - 1], height[i])
        
        rightMax[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            rightMax[i] = max(rightMax[i + 1], height[i])
        
        res = 0
        for i in range(n):
            res += min(leftMax[i], rightMax[i]) - height[i]
        return res
            