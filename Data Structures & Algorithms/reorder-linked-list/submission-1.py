# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        l=head
        # dummy = ListNode(head)
        while(l and l.next and l.next.next):
            print(".")
            r=l
            while r.next.next:
                print("_")
                r=r.next
            nxt = l.next
            l.next = r.next
            r.next.next = nxt
            l=nxt
            r.next = None
        # return dummy.next
