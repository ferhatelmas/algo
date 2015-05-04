class Solution:
    def partition(self, s):
        res = []
        if not s:
            return res
        self.dfs(0, s, [], res)
        return res

    def dfs(self, k, s, p, res):
        l = len(s)
        if k == l:
            res.append([e for e in p])
            return
        for i in range(k, l):
            if s[k:i+1] == s[k:i+1][::-1]:
                p.append(s[k:i+1])
                self.dfs(i+1, s, p, res)
                p.pop()
