class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = self.right = None


class Solution(object):
    def eq(self, s, t):
        if s is None or t is None:
            return s == t
        if s.val != t.val:
            return False
        return self.eq(s.left, t.left) and self.eq(s.right, t.right)

    def isSubtree(self, s, t):
        if self.eq(s, t):
            return True
        if s is None:
            return False
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
