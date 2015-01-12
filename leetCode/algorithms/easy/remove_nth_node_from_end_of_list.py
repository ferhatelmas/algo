class Solution:
    def removeNthFromEnd(self, head, n):
        s = e = d = ListNode(0)
        d.next = head

        for _ in xrange(n):
            e = e.next
        while e.next is not None:
            s, e = s.next, e.next
        s.next = s.next.next
        return d.next
