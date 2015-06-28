from collections import deque


class Solution:
    def levelOrderBottom(self, root):
        res = []
        if not root:
            return res
        d = deque([root])
        while d:
            l, ls = len(d), []
            for _ in range(l):
                n = d.popleft()
                ls.append(n.val)
                if n.left:
                    d.append(n.left)
                if n.right:
                    d.append(n.right)
            res.append(ls)
        return res[::-1]
