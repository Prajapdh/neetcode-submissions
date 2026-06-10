class Solution:
    def trap(self, height: List[int]) -> int:
        # two pointer approach, Space: O(1)
        leftMax, rightMax = 0, 0
        res=0
        l,r=0, len(height)-1
        while l<r:
            # always move the lowest pointer, there is no chance of overflowing if we move like this
            if(height[l]<=height[r]):
                if(leftMax>=height[l]):
                    res+=leftMax-height[l]  # we're sure there isn't anything greater than leftMax to the left
                else:
                    leftMax=height[l]
                l+=1
            else:
                if(rightMax>height[r]):
                    res+=rightMax-height[r]
                else:
                    rightMax=height[r]
                r-=1
        return res
            