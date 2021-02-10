package javaproblems;

class ListNode {

    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class Solution {

    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode newhead = new ListNode();
        ListNode current, next, prev, start, end;
        current = head;
        next = null;
        prev = null;

        int count = 1;
        while (count < k && current != null) {
            current = current.next;
            count++;
        }

        if (current != null && count == k) {
            start = current.next;
            end = head;
            current = head;
            next = null;
            prev = start;
            count = 0;

            while (count < k && current != null) {
                next = current.next;
                current.next = prev;
                prev = current;
                current = next;
                count++;
            }
            newhead = prev;
        }
        else
        {
            //newhead = head;
            return head;
        }

        end.next = reverseKGroup(start,k);

        return newhead;
    }
}

public class ReverseNodesink_Group {

    public static void main(String[] args) {
        Solution s = new Solution();
        int value[] = {1, 2, 3,4,5,6,7,8};
        ListNode head = new ListNode();
        if (value.length != 0) {

            ListNode cur = head;
            for (int i = 0; i < value.length; i++) {
                cur.val = value[i];
                if (i == value.length - 1) {
                    cur.next = null;
                } else {
                    cur.next = new ListNode();
                    cur = cur.next;
                }

            }
        } else {
            head = null;
        }

        ListNode newhead = s.reverseKGroup(head, 3);
        while (newhead != null) {
            System.out.println(newhead.val);
            newhead = newhead.next;
        }
    }
}