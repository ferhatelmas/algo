from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def gcd(self, a: int, b: int) -> int:
        while b:
            a, b = b, a % b
        return abs(a)

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        p = head
        while p.next:
            t = ListNode(self.gcd(p.val, p.next.val), p.next)
            p.next = t
            p = t.next
        return head
