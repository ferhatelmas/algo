class Solution:
    def hasCycle(self, head):
        curr = head
        while curr:
            if curr.val is None:
                return True
            curr.val = None
            curr = curr.next
        return False
