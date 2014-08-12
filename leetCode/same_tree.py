class Solution:
    def isSameTree(self, p, q):
        if (not p and q) or (p and not q):
            return False
        elif not p and not q:
            return True
        return (
            p.val == q.val and
            self.isSameTree(p.left, q.left) and
            self.isSameTree(p.right, q.right)
        )