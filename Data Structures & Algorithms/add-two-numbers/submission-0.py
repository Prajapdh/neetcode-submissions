# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        node=dummy
        carry=0
        while(l1 or l2 or carry):
            l1val=l1.val if l1 else 0
            l2val=l2.val if l2 else 0
            summ=l1val+l2val+carry
            val=summ%10
            carry=summ//10
            node.next=ListNode(val)
            node=node.next
            if l1: l1=l1.next
            if l2: l2=l2.next
        
        return dummy.next