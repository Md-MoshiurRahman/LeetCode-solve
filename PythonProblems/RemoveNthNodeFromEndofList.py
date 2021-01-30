class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        length = 0
        first = head

        while first is not None:
            length += 1
            first = first.next

        length -= n
        first = dummy
        while length > 0:
            length -= 1
            first = first.next

        first.next = first.next.next
        return dummy.next


if __name__ == "__main__":
    val1 = [1,2,3,4,5]

    head = ListNode()
    curr = head

    for i in range(len(val1)):
        curr.val = val1[i]
        if i == len(val1) - 1:
            curr.next = None
            break
        else:
            curr.next = ListNode()
            curr = curr.next

    s = Solution()
    n = 2
    r = s.removeNthFromEnd(head, n)

    while r is not None:
        print(r.val)
        r = r.next
