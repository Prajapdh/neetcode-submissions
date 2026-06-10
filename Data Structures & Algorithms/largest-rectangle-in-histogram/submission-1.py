class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack=[]    #stores a pair: (height, index)
        maxArea=0
        # We will append height to the stack if current height is more than top height
        # If not, we will try to find the area with the top height and pop it
        for i,h in enumerate(heights):
            it=i
            while stack and stack[-1][0]>h:
                ht,it = stack.pop()
                maxArea =  max(maxArea, (i-it)*ht)
            stack.append((h,it))
        
        while stack:
            ht,it=stack.pop()
            maxArea=max(maxArea, (len(heights)-it)*ht)
        
        return maxArea