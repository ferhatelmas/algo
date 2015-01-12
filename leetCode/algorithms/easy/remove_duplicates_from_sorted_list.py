class Solution:
    def deleteDuplicates(self, head):
        if head:
            p = head.next
            while p and p.val == head.val:
                p = p.next
            head.next = self.deleteDuplicates(p)
        return head