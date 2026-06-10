# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next and n>=1:
            return None
        dummy=ListNode(-1, head)
        l=r=head
        while n and r:
            # print(f"n: {n} , r.val: {r.val}")
            r=r.next
            n-=1
            
        
        while(r and r.next):
            # print(f"l: {l.val}, r: {r.val}")
            l=l.next
            r=r.next
        # print(l.val, r.val)
        if not r and l==head:
            return head.next

        l.next= l.next.next
        # print(l.next.val)
        # print(dummy.val, dummy.next.val)
        return dummy.next