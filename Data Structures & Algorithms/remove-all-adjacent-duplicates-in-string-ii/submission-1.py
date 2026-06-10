class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack=[] # stores char, count
        for c in s:
            count=1
            if stack and stack[-1][0]==c:
                count=1+stack.pop()[1]
            stack.append((c, count))
            while stack and stack[-1][-1]==k:
                stack.pop()                     
        # print(stack)
        res=""
        for char, count in stack:
            for i in range(count):
                res+=char
        return res
            