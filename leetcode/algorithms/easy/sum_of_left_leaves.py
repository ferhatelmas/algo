class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sumOfLeftLeaves(self, root):
        if root is None:
            return 0
        v = 0
        if root.left is not None:
            l = root.left
            if l.left is None and l.right is None:
                v += l.val
            else:
                v += self.sumOfLeftLeaves(l)
        return v + self.sumOfLeftLeaves(root.right)
