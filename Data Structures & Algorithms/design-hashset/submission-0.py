class ListNode:
    def __init__(self, key=-1, next=None):
        self.key=key
        self.next=next

class MyHashSet:
    def __init__(self):
        self.arr=[ListNode() for _ in range(1000)]
    
    def hash(self, key):
        return key%len(self.arr)

    def add(self, key: int) -> None:
        curr=self.arr[self.hash(key)]
        while curr.next:
            # Don't add the same key again
            if curr.next.key==key:
                return
            curr=curr.next
        # curr is last node
        curr.next=ListNode(key)

    def remove(self, key: int) -> None:
        curr=self.arr[self.hash(key)]
        while curr.next:
            if curr.next.key==key:
                curr.next=curr.next.next
                return
            curr=curr.next
        

    def contains(self, key: int) -> bool:
        curr=self.arr[self.hash(key)]
        while curr.next:
            if curr.next.key==key:
                return True
            curr=curr.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)