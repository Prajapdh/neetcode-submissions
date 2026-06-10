class FreqStack:

    def __init__(self):
        self.cnt={}
        self.stack=[[]]
        self.maxCnt=0

    def push(self, val: int) -> None:
        if val not in self.cnt:
            self.cnt[val]=0
        self.cnt[val]+=1
        if self.cnt[val]>self.maxCnt:
            self.maxCnt=self.cnt[val]
            self.stack.append([])
        self.stack[self.cnt[val]].append(val)

    def pop(self) -> int:
        if self.maxCnt and self.stack[self.maxCnt]:
            val=self.stack[self.maxCnt].pop()
            self.cnt[val]-=1
            if len(self.stack[self.maxCnt])==0: self.maxCnt-=1
            return val
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()