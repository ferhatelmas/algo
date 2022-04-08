class Solution:
    def insertionSortList(self, head):
        r, c = [], head
        while c is not None:
            r.append(c.val)
            c = c.next
        c = head
        for e in sorted(r):
            c.val = e
            c = c.next
        return head
