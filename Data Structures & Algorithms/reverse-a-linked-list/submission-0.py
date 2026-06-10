# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        revNode, node = None, head
        while node.next:
            nxtNode=node.next
            node.next=revNode
            revNode = node
            node = nxtNode
            # print(f"revNode: {revNode.val}, node: {node.val}")
        node.next=revNode
        # print(node.next)
        return node
        