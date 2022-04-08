# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def oddEvenList(self, head):
        s, t = ListNode(0), ListNode(0)
        o, e, c, i = s, t, head, 1
        while c is not None:
            if i % 2:
                o.next = c
                o = o.next
            else:
                e.next = c
                e = e.next
            c, i = c.next, i + 1
        o.next, e.next = t.next, None
        return s.next
