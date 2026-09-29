class Solution:
    def trap(self, height: List[int]) -> int:
        stack=[]    #stores indices
        res=0
        for i,h in enumerate(height):
            while stack and h>=height[stack[-1]]:
                base = height[stack.pop()]
                if stack:
                    l=min(height[i], height[stack[-1]])-base
                    w=i-stack[-1]-1 #everything in between stack[-1] and i is counted, we just need to add additional area
                    res+=l*w
            stack.append(i)

        return res