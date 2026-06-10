# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy=ListNode()
        node = dummy
        while list1 or list2:
            val1 = list1.val if list1 else float("inf")
            val2 = list2.val if list2 else float("inf")
            # print(val1, val2)
            if val1<=val2:
                node.next = list1
                list1 = list1.next if list1 else None
            else:
                node.next = list2
                list2 = list2.next if list2 else None
            node.next.next=None
            node=node.next
            
            
        # print(dummy.val, dummy.next.val)
        return dummy.next

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        for i in range(1, len(lists)):
            lists[i]=self.mergeTwoLists(lists[i], lists[i-1])
        
        return lists[-1]





        