class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sum(self, root: TreeNode) -> int:
        if root is None:
            return 0
        return root.val + self.sum(root.left) + self.sum(root.right)

    def product(self, root: TreeNode, total: int) -> (int, int):
        if root is None:
            return (0, 0)
        sl, pl = self.product(root.left, total)
        sr, pr = self.product(root.right, total)
        s = root.val + sl + sr
        return (s, max([pl, pr, (total - s) * s]))

    def maxProduct(self, root: TreeNode) -> int:
        total = self.sum(root)
        _, p = self.product(root, total)
        return p % (10**9 + 7)
