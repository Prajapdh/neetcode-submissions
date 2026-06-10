class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0 for _ in range(len(temperatures))]
        for i,t in enumerate(temperatures):
            if not stack:
                # print(f"adding {t}, {i} in stack")
                stack.append([t,i])
                continue
 
            # print(f"last temp: {stack[-1][0]}, last index: {stack[-1][1]}")
            if(t>stack[-1][0]):
                while(stack and t>stack[-1][0]):
                    res[stack[-1][1]]=i-stack[-1][1]
                    # print(f"removing {stack[-1][0]}, {stack[-1][1]} in stack")
                    stack.pop()
                    
                # print(f"adding {t}, {i} in stack")
                stack.append([t,i])
            else:
                # print(f"adding {t}, {i} in stack")
                stack.append([t,i])
        return res
            