class MyStack:

    def __init__(self):
        self.queue1,self.queue2=deque(),deque()
        self.size=0

    def push(self, x: int) -> None:
        self.queue1.append(x)
        self.size+=1
    
    def pop(self) -> int:
        if self.empty():
            return None  # or raise, depending on spec

        # Move all but last from q1 to q2
        while len(self.queue1) > 1:
            self.queue2.append(self.queue1.popleft())

        # Last element of q1 is the stack top
        top_elem = self.queue1.popleft()
        self.size -= 1

        # Swap queues so q1 is always the main one
        self.queue1, self.queue2 = self.queue2, self.queue1
        return top_elem

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