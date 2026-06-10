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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // Traverse through both linked list, store addition of digits in a stack
        // the stack will store: (carry, sum%10)
        Deque<Integer> stack1 = new ArrayDeque<>(), stack2 = new ArrayDeque<>();
        ListNode node1=l1, node2=l2;
        while((Objects.nonNull(node1))||(Objects.nonNull(node2))){
            if(Objects.nonNull(node1)) stack1.push(node1.val);
            if (Objects.nonNull(node2)) stack2.push(node2.val);
            node1 = (Objects.nonNull(node1)) ? node1.next : null;
            node2 = (Objects.nonNull(node2)) ? node2.next : null;
        }
        ListNode dummy = new ListNode();
        boolean carry = false;
        while(!stack1.isEmpty() || !stack2.isEmpty() || carry){
            int val = (!stack1.isEmpty()) ? stack1.pop() : 0;
            val += (!stack2.isEmpty()) ? stack2.pop() : 0;
            ListNode node = new ListNode((val + Boolean.compare(carry, false))%10);
            ListNode temp = dummy.next;
            dummy.next = node;
            node.next = temp;
            carry = ((val + Boolean.compare(carry, false))/10 == 1) ? true : false;
        }
        return dummy.next;
    }
}