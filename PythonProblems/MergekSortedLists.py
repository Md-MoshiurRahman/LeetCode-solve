class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeKLists(self, list):
        nums = []
        for l in list:
            curr = l
            while curr is not None:
                nums.append(curr.val)
                curr = curr.next
        nums.sort()

        if len(nums) != 0:
            result = ListNode()
            curr = result

            for i in range(len(nums)):
                curr.val = nums[i]
                if i == len(nums) - 1:
                    curr.next = None
                    break
                else:
                    curr.next = ListNode()
                    curr = curr.next
        else:
            result = None

        return result





if __name__ == "__main__":
    val1 = [[1,4,5],[1,3,4],[2,6]]
    list = []
    for val in val1:
        if len(val) != 0:
            l1 = ListNode()
            curr = l1
            for i in range(len(val)):
                curr.val = val[i]
                if i == len(val) - 1:
                    curr.next = None
                    break
                else:
                    curr.next = ListNode()
                    curr = curr.next
        else:
            l1 = None
        list.append(l1)

    s = Solution()
    r = s.mergeKLists(list)

    while r is not None:
        print(r.val)
        r = r.next