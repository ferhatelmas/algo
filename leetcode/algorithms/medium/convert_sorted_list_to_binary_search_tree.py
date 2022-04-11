class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        if head is None:
            return None
        s, f, t = head, head, None
        while f.next is not None and f.next.next is not None:
            s, f, t = s.next, f.next.next, s

        if t is None:
            head = None
        else:
            t.next = None
        r = TreeNode(s.val)
        r.left = self.sortedListToBST(head)
        r.right = self.sortedListToBST(s.next)
        return r
