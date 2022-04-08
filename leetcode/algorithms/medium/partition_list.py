class Solution:
    def partition(self, head, x):
        l, r = ListNode(0), ListNode(0)
        b, e = l, r
        while head is not None:
            if head.val < x:
                l.next = head
                l = l.next
            else:
                r.next = head
                r = r.next
            head = head.next
        l.next, r.next = e.next, None
        return b.next
