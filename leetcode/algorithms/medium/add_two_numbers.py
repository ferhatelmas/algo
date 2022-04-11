class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        head, curr, c = None, None, 0

        def val(ls):
            return ls.val if ls else 0

        while l1 or l2:
            c, k = divmod(val(l1) + val(l2) + c, 10)
            if head:
                curr.next = ListNode(k)
                curr = curr.next
            else:
                head = ListNode(k)
                curr = head
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if c:
            curr.next = ListNode(c)
        return head
