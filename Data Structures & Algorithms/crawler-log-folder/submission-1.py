class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack=[]
        for command in logs:
            if command=="../":
                if stack: stack.pop()
            elif command=="./":
                continue
            else:
                stack.append(command)
        
        return len(stack)