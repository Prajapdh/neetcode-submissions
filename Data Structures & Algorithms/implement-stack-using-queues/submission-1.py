class MyStack:

    def __init__(self):
        self.queue1,self.queue2=deque(),deque()
        self.size=0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.size+=1
    
    def pop(self) -> int:
        if not self.size: return None
        self.size-=1
        if self.queue1:
            n=len(self.queue1)
            for i in range(n-1):
                self.queue2.append(self.queue1.popleft())
            return self.queue1.popleft()
        else:
            n=len(self.queue2)
            for i in range(n-1):
                self.queue1.append(self.queue2.popleft())
            return self.queue2.popleft()

    def top(self) -> int:
        if self.queue1:
            return self.queue1[-1]
        elif self.queue2:
            return self.queue2[-1]
        return None

    def empty(self) -> bool:
        return False if self.size else True


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()