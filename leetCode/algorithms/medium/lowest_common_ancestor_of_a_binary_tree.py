class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root is None or p == root or q == root:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)
        if l is None:
            return r
        if r is None:
            return l
        return root
