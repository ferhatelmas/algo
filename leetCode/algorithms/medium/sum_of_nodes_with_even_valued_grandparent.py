class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def add(n):
    return n.val if n else 0


class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        if not root or (not root.left and not root.right):
            return 0

        c, even = 0, root.val % 2 == 0
        if root.left:
            c += self.sumEvenGrandparent(root.left)
            if even:
                c += add(root.left.left)
                c += add(root.left.right)
        if root.right:
            c += self.sumEvenGrandparent(root.right)
            if even:
                c += add(root.right.left)
                c += add(root.right.right)
        return c
