# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def gcd(a, b):
            # Find Minimum of a and b
            result = min(a, b)
            while result > 0:
                if a % result == 0 and b % result == 0:
                    break
                result -= 1
            # Return gcd of a and b
            return result

        dummy=ListNode(-1, head)
        curr=dummy.next
        prev=dummy
        while curr:
            if prev and curr and prev!=dummy:
                value=gcd(prev.val, curr.val)
                node=ListNode(value, curr)
                prev.next=node
            prev=curr
            curr=curr.next
        return dummy.next