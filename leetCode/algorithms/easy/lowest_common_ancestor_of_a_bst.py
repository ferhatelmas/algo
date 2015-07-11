class Solution:
    def lowestCommonAncestor(self, root, p, q):
        if root == p or root == q:
            return root
        n = (p.val > root.val) + (q.val > root.val)
        if n == 0:
            return self.lowestCommonAncestor(root.left, p, q)
        elif n == 2:
            return self.lowestCommonAncestor(root.right, p, q)
        return root
