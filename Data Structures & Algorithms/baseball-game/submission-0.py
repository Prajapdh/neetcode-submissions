class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for op in operations:
            if op=='+' and len(stack)>=2:
                stack.append(stack[-1]+stack[-2])
            elif op=='D' and len(stack)>0:
                stack.append(2*stack[-1])
            elif op=='C' and len(stack)>0:
                stack.pop()
            else:
                stack.append(int(op))
        
        res=0
        while stack:
            res+=stack.pop()
        return res