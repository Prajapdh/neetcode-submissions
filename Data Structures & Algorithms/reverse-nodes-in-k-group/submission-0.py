# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def findKth(self, node, k):
        while node and k>0:
            node=node.next
            k-=1
        return node

    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(-1, head)
        groupPrev=dummy
        while True:
            # break the loop if kth node not found
            # it means that there weren't enough elments
            kth=self.findKth(groupPrev, k)
            if not kth:
                break

            groupNext=kth.next
            # lets reverse the nodes from groupPrev.next till kth node
            prev=kth.next   #connecting the last node to the groupNext
            curr=groupPrev.next
            # stopping after reversing curr=kth node(node left to the groupNext)
            while(curr!=groupNext):
                nxt=curr.next
                curr.next=prev
                prev=curr
                curr=nxt

            # at this point our list's head is disconnected
            # lets connect the groupPrev with new group head
            # but first we will save the value of groupPrev.next as it is now the new group tail
            prevGroupTail=groupPrev.next
            groupPrev.next=kth
            groupPrev=prevGroupTail
        
        return dummy.next
            
            

