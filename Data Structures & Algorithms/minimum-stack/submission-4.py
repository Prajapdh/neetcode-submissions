class MinStack:

    def __init__(self):
        self.stack=[]
        self.decStack=[]

    def push(self, val: int) -> None:
        self.stack.append(val)
        if (not self.decStack) or (self.decStack[-1]>=val):
            self.decStack.append(val)
        print(f"stack: {self.stack}, decStack: {self.decStack}")

    def pop(self) -> None:
        val = self.stack.pop()
        if self.decStack and self.decStack[-1]==val:
            self.decStack.pop()
        print(f"stack: {self.stack}, decStack: {self.decStack}")

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        print(f"stack: {self.stack}, decStack: {self.decStack}")
        return self.decStack[-1]
