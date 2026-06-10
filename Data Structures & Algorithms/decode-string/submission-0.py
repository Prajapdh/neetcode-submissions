class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        for c in s:
            if c!=']':
                stack.append(c)
            else:
                curr=""
                while stack and stack[-1]!="[":
                    curr=stack.pop()+curr
                stack.pop()
                digit=""
                while stack and stack[-1].isdigit():
                    digit=stack.pop()+digit
                stack.append(curr*int(digit))
        return "".join(stack)