# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=r=head
        dummy = ListNode(head)
        while(l and l.next and l.next.next):
            r=l
            tail = None
            while r.next.next:
                r=r.next
            tail=r.next
            nxt = l.next
            l.next = tail
            tail.next = nxt
            l=nxt
            r.next = None
        return dummy.next
