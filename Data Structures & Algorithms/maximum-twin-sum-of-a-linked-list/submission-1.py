# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow,fast=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        # reverse the second half of the list
        prev, node=None, slow
        while node:
            temp=node.next
            node.next = prev
            prev=node
            node=temp
        # prev is head of reversed linked list
        res=0
        first, second = head, prev
        while second:
            res=max(res, first.val+second.val)
            first = first.next
            second = second.next

        return res