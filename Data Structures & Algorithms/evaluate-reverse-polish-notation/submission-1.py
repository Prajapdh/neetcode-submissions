class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res=0
        stack=[]
        for c in tokens:
            if(c=='+'):
                o1=stack.pop()
                o2=stack.pop()
                stack.append(o2+o1)
            elif(c=='-'):
                o1=stack.pop()
                o2=stack.pop()
                stack.append(o2-o1)
            elif(c=='*'):
                o1=stack.pop()
                o2=stack.pop()
                stack.append(int(o2*o1))
            elif(c=='/'):
                o1=stack.pop()
                o2=stack.pop()
                stack.append(int(o2/o1))
            else:
                stack.append(int(c))
        res = stack.pop()
        return res if not stack else 0