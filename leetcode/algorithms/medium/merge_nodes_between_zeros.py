from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return head
        prev, cur, total = head, head, 0
        while cur:
            if cur.val == 0 and total > 0:
                total, prev.val = 0, total
                if cur.next is None:
                    prev.next = None
                else:
                    prev = prev.next
            else:
                total += cur.val
            cur = cur.next
        return head
