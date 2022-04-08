class Solution:
    def rightSideView(self, root):
        res = []
        self.dfs(root, 0, res)
        return res

    def dfs(self, r, n, res):
        if not r:
            return
        if n >= len(res):
            res.append(r.val)
        self.dfs(r.right, n + 1, res)
        self.dfs(r.left, n + 1, res)
