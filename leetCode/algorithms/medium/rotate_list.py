class Solution(object):
    def rotateRight(self, head, k):
        if head is None or head.next is None:
            return head
        n, p = 1, head
        while p.next:
            p, n = p.next, n + 1
        p.next = head
        n -= k % n
        while n > 0:
            p, n = p.next, n - 1
        r, p.next = p.next, None
        return r
