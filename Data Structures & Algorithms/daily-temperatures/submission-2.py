class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic decreasing stack
        n=len(temperatures)
        res=[0]*n
        stack = []
        for i,t in enumerate(temperatures):
            while stack and t>temperatures[stack[-1]]:
                idx=stack.pop()
                res[idx]=i-idx
            stack.append(i)
        print(stack)
        
        return res