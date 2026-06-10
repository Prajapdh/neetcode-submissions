class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # empty area doesn't count
        # monotonically increasing stack: stores index, height 
        res=0
        stack=[]
        for i in range(len(heights)):
            start=i
            while stack and stack[-1][1]>heights[i]:
                res=max(res, stack[-1][1]*(i-stack[-1][0]))
                start=stack[-1][0]
                stack.pop()
                
            stack.append((start, heights[i]))
        print(stack)
        while stack:
            res=max(res, stack[-1][1]*(len(heights)-stack[-1][0]))
            stack.pop()
        return res
            
