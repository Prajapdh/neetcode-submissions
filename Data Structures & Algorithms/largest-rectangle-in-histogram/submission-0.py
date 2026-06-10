class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea=0
        stack=[]
        n = len(heights)
        for i, height in enumerate(heights):
            startIndex=i
            while stack and height<stack[-1][1]:
                j, h = stack.pop()
                area = (i-j)*h
                maxArea=max(maxArea, area)
                startIndex=j
            stack.append([startIndex, height])

        while stack:
            j, h = stack.pop()
            area = (n-j)*h
            maxArea=max(maxArea, area)
        
        return maxArea
            