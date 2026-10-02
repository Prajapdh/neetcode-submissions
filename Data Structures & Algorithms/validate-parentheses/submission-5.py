class Solution:
    def isValid(self, s: str) -> bool:
        braces={']':'[', '}':'{',')':'('}
        stack=[]
        for c in s:
            if c in braces:
                if not stack or (stack and stack[-1]!=braces[c]):
                    return False
                stack.pop()
            else:
                stack.append(c)
        
        return True if not stack else False
