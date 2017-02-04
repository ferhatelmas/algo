import collections


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findMode(self, root):
        d = collections.defaultdict(int)

        def go(r):
            if r is None:
                return
            d[r.val] += 1
            go(r.left)
            go(r.right)
        go(root)
        m = max(d.values() or [0])
        return [k for k, v in d.items() if v == m]
