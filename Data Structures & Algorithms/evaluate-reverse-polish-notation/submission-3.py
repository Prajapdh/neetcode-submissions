class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            val=t
            if t=="+":
                right, left = int(stack.pop()), int(stack.pop())
                val=left+right
            elif t=='-':
                right, left = int(stack.pop()), int(stack.pop())
                val=left-right
            elif t=='*':
                right, left = int(stack.pop()), int(stack.pop())
                val=left*right
            elif t=='/':
                right, left = int(stack.pop()), int(stack.pop())
                val=left/right            

            stack.append(val)
        return int(stack.pop())