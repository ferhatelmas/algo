class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseBetween(self, head, m, n):
        t = ListNode(0)
        t.next = head
        p, s = t, head
        for _ in range(m - 1):
            p, s = p.next, s.next
        for _ in range(n - m):
            c = s.next
            s.next, c.next = c.next, p.next
            p.next = c
        return t.next
