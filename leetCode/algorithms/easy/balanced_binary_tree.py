class Solution:

    def isBalanced(self, root):
        self.r = True
        self.h(root)
        return self.r

    def h(self, n):
        if n is None:
            return 0
        lh, rh = self.h(n.left), self.h(n.right)
        if abs(lh - rh) > 1:
            self.r = False
        return max(lh, rh) + 1
