class ListNode:
    def __init__(self,key=-1, val=-1, next=None):
        self.key=key
        self.val=val
        self.next=next

class MyHashMap:
    def __init__(self):
        self.arr=[ListNode() for _ in range(10000)]
    
    def getIdx(self, key):
        return key%10000

    def put(self, key: int, value: int) -> None:
        curr = self.arr[self.getIdx(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return
            curr = curr.next
        curr.next = ListNode(key, value)

    def get(self, key: int) -> int:
        curr=self.arr[self.getIdx(key)]
        while curr:
            if curr.key==key:
                return curr.val
            curr=curr.next
        return -1

    def remove(self, key: int) -> None:
        curr = self.arr[self.getIdx(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)