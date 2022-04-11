class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        if head is None or head.next is None:
            return head
        prev, slow, fast = None, head, head
        while fast is not None and fast.next is not None:
            prev, slow, fast = slow, slow.next, fast.next.next

        prev.next = None
        return self.merge(self.sortList(head), self.sortList(slow))

    def merge(self, l1, l2):
        l = p = ListNode(0)

        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                p.next, l1 = l1, l1.next
            else:
                p.next, l2 = l2, l2.next
            p = p.next

        if l1 is not None:
            p.next = l1
        if l2 is not None:
            p.next = l2
        return l.next
