class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        if l1 is None and l2 is None:
            return None

        result = ListNode()
        curr = result
        end = result

        while l1 is not None or l2 is not None:
            if l1 is None and l2 is not None:
                curr.val = l2.val
                end = curr
                curr.next = ListNode()
                curr = curr.next
                l2 = l2.next
            elif l2 is None and l1 is not None:
                curr.val = l1.val
                end = curr
                curr.next = ListNode()
                curr = curr.next
                l1 = l1.next
            elif l1.val <= l2.val:
                curr.val = l1.val
                end = curr
                curr.next = ListNode()
                curr = curr.next
                l1 = l1.next
            else:
                curr.val = l2.val
                end = curr
                curr.next = ListNode()
                curr = curr.next
                l2 = l2.next

        end.next = None
        return result



if __name__ == "__main__":
    val1 = []
    val2 = []

    if len(val1) != 0:
        l1 = ListNode()
    else:
        l1 = None

    curr = l1

    for i in range(len(val1)):
        curr.val = val1[i]
        if i == len(val1) - 1:
            curr.next = None
            break
        else:
            curr.next = ListNode()
            curr = curr.next

    if len(val2) != 0:
        l2 = ListNode()
    else:
        l2 = None
    curr = l2

    for i in range(len(val2)):
        curr.val = val2[i]
        if i == len(val2) - 1:
            curr.next = None
            break
        else:
            curr.next = ListNode()
            curr = curr.next

    s = Solution()
    r = s.mergeTwoLists(l1, l2)

    while r is not None:
        print(r.val)
        r = r.next