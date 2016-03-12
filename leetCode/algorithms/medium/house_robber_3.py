class Solution:
    def rob(self, root):
        def f(n):
            if not n:
                return [0, 0]
            l, r = f(n.left), f(n.right)
            return [l[1] + r[1], max(l[1] + r[1], n.val + l[0] + r[0])]
        return max(f(root))
