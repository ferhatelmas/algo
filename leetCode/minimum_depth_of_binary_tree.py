class Solution:
    def minDepth(self, root):
        if not root:
            return 0
        l, r = self.minDepth(root.left), self.minDepth(root.right)
        return 1 + (min(l, r) if root.left and root.right else max(l, r))
