class Solution:
    def kthSmallest(self, root, k):
        self.k = k

        def r(n):
            if n:
                c = r(n.left)
                if not self.k:
                    return c
                self.k -= 1
                if not self.k:
                    return n.val
                return r(n.right)

        return r(root)
