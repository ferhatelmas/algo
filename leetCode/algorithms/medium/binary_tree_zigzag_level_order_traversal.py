class Solution:
    def zigzagLevelOrder(self, root):
        res = []
        if root is None:
            return []
        q = [root]
        f = True
        while q:
            l = len(q)
            r = [0] * l
            for i in l:
                c = q.pop(0)
                j = i if f else l - i - 1
                r[j] = c.val
                if c.left is not None:
                    q.append(c.left)
                if c.right is not None:
                    q.append(c.right)
            f = not f
            res.append(r)
        return res
