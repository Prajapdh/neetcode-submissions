/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode insertionSortList(ListNode head) {
        ListNode resDummy = new ListNode(), inputDummy = new ListNode(-1, head);
        while(inputDummy.next!=null){
            ListNode temp = inputDummy.next;
            inputDummy.next = temp.next;
            ListNode curr = resDummy;
            while(curr.next!=null && curr.next.val<temp.val){
                curr=curr.next;
            }       
            temp.next = curr.next;
            curr.next=temp;
        }
        return resDummy.next;
    }
}