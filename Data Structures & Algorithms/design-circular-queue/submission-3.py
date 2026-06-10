class Node:
    def __init__(self, val, next=None, prev=None):
        self.val=val
        self.next=next
        self.prev=prev

class MyCircularQueue:

    def __init__(self, k: int):
        self.frontDummy = Node(-1, None, None)
        self.backDummy = Node(-1, None, self.frontDummy)
        self.frontDummy.next=self.backDummy
        self.space=k

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        temp=self.backDummy.prev
        node=Node(value, self.backDummy, temp)
        temp.next=node
        self.backDummy.prev=node
        self.space-=1
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        self.frontDummy.next = self.frontDummy.next.next
        self.frontDummy.next.prev = self.frontDummy
        
        self.space+=1
        return True

    def Front(self) -> int:
        if not self.isEmpty():
            return self.frontDummy.next.val
        return -1

    def Rear(self) -> int:
        if not self.isEmpty():
            return self.backDummy.prev.val
        return -1      

    def isEmpty(self) -> bool:
        return self.frontDummy.next==self.backDummy

    def isFull(self) -> bool:
        return self.space==0


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()