# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        stack=[]
        slow,fast=head, head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        while slow:
            stack.append(slow.val)
            slow=slow.next
        
        node=head
        size=len(stack)
        res=0
        for i in range(size):
            res=max(res, stack.pop()+node.val)
            node=node.next
        return res