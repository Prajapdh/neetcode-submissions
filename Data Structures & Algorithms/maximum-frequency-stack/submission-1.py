class FreqStack:

    def __init__(self):
        self.counterMap={}
        self.maxHeap=[]
        self.index=0

    def push(self, val: int) -> None:
        if val not in self.counterMap:
            self.counterMap[val]=0
        self.counterMap[val]+=1
        heapq.heappush(self.maxHeap, (-1*self.counterMap[val], -1*self.index, val))
        self.index+=1

    def pop(self) -> int:
        count, ind, val = heapq.heappop(self.maxHeap)
        self.counterMap[val]-=1
        if self.counterMap[val]==0: del self.counterMap[val] 
        return val       

# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()