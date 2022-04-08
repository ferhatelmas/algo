class Solution:
    def reverseList(self, head):
        p = None
        while head:
            n, head.next = head.next, p
            p, head = head, n
        return p
