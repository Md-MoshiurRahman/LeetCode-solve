/*
 * by modifying  the values
 */
package javaproblems;

/*
class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    public ListNode swapPairs(ListNode head) {
        ListNode current = head;
        while(current != null && current.next!=null)
        {
            int value = current.val;
            current.val = current.next.val;
            current.next.val = value;
            current = current.next.next;
        }
        return head;
    }
}
public class SwapNodesinPairs {
    public static void main(String[] args) {
        Solution s = new Solution();
        int value[] = {1,2,3,4};
        ListNode head = new ListNode();
        if(value.length !=0)
        {
            
            ListNode cur = head;
            for(int i=0;i<value.length;i++)
            {
                cur.val = value[i];
                if(i == value.length-1)
                {
                    cur.next = null;
                }
                else
                {
                    cur.next = new ListNode();
                    cur = cur.next;
                }
                
            }
        }
        else
        {
            head = null;
        }
 
        //System.out.println(s.swapPairs(head));
        ListNode newhead = s.swapPairs(head);
        while(newhead != null)
        {
            System.out.println(newhead.val);
            newhead = newhead.next;
        }
    }
}
*/

/*
 * by modifying  the nodes
 */

class ListNode {
    int val;
    ListNode next;
    ListNode() {}
    ListNode(int val) { this.val = val; }
    ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
class Solution {
    public ListNode swapPairs(ListNode head) {
        
        
        if(head == null || head.next==null)
        {
            return head;
        }
        
        //ListNode nextR = head.next.next;
        
        ListNode newhead = head.next;
        head.next = newhead.next;
        newhead.next = head;
        
        ListNode prev = head;
        head = head.next;
        
        while(head != null && head.next!=null)
        {
            ListNode curr = head.next;
            head.next = curr.next;
            curr.next = head;
            prev.next = curr;
            prev = head;
            head = head.next;
        }
        return newhead;
    }
}
public class SwapNodesinPairs {
    public static void main(String[] args) {
        Solution s = new Solution();
        int value[] = {1,2,3,4,5,6,7,8};
        ListNode head = new ListNode();
        if(value.length !=0)
        {
            
            ListNode cur = head;
            for(int i=0;i<value.length;i++)
            {
                cur.val = value[i];
                if(i == value.length-1)
                {
                    cur.next = null;
                }
                else
                {
                    cur.next = new ListNode();
                    cur = cur.next;
                }
                
            }
        }
        else
        {
            head = null;
        }
 
        //System.out.println(s.swapPairs(head));
        ListNode newhead = s.swapPairs(head);
        while(newhead != null)
        {
            System.out.println(newhead.val);
            newhead = newhead.next;
        }
    }
}