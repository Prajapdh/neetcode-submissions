class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for op in tokens:
            if op=="+":
                stack.append(stack.pop()+stack.pop())
            elif op=='*':
                stack.append(stack.pop()*stack.pop())
            elif op=='-':
                a=stack.pop()
                b=stack.pop()
                stack.append(b-a)
            elif op=='/':
                a=stack.pop()
                b=stack.pop()
                stack.append(b//a if b>0 and a>0 else -1*(abs(b)//abs(a)))
            else:
                stack.append(int(op))
            # print(stack)
        
        return stack.pop()