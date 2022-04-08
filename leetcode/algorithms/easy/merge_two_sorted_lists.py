class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1, l2):
        ls = p = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        while l1 is not None:
            p.next = l1
            p = p.next
            l1 = l1.next
        while l2 is not None:
            p.next = l2
            p = p.next
            l2 = l2.next
        return ls.next
