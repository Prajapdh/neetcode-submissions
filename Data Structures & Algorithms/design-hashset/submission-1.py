class ListNode:
    def __init__(self, val=-1, next=None):
        self.val=val
        self.next=next

class MyHashSet:

    def __init__(self):
        self.values=[ListNode(-1) for _ in range(10**4)]

    def hash(self, val):
        return val%10000

    def add(self, key: int) -> None:
        idx=self.hash(key)
        node=self.values[idx]
        while node.next:
            if node.next.val==key:
                return
            node=node.next
        node.next=ListNode(key)

    def remove(self, key: int) -> None:
        idx=self.hash(key)
        node=self.values[idx]
        while node.next:
            if node.next.val==key:
                node.next=node.next.next
                return
            node=node.next

    def contains(self, key: int) -> bool:
        idx=self.hash(key)
        node=self.values[idx]
        while node.next:
            if node.next.val==key:
                return True
            node=node.next
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)