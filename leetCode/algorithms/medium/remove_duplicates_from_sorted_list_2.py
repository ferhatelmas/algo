class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __str__(self):
        return '{}->{}'.format(self.val, self.next)


class Solution:
    def deleteDuplicates(self, head):
        p = h = ListNode(0)
        while head is not None:
            if head.next is not None and head.val == head.next.val:
                v = head.val
                while head is not None and head.val == v:
                    head = head.next
            else:
                p.next = head
                p = p.next
                head = head.next
        p.next = None
        return h.next
