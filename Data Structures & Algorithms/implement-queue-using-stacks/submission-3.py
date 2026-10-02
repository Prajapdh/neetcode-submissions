class MyQueue:

    def __init__(self):
        self.appendStack=[]
        self.popStack=[]

    def push(self, x: int) -> None:
        self.appendStack.append(x)

    def pop(self) -> int:
        if not self.popStack:
            while self.appendStack:
                self.popStack.append(self.appendStack.pop())
        return self.popStack.pop()

    def peek(self) -> int:
        if not self.popStack:
            while self.appendStack:
                self.popStack.append(self.appendStack.pop())
        return self.popStack[-1]

    def empty(self) -> bool:
        return max(len(self.appendStack),len(self.popStack))==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()