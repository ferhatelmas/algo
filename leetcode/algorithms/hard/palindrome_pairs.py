class Solution:
    def palindromePairs(self, words):
        m = {e: i for i, e in enumerate(words)}
        res = []
        for i, e in enumerate(words):
            l, r, le = 0, 0, len(e)
            while l <= r:
                s = e[l:r]
                j = m.get(s[::-1], -1)
                if j != -1 and i != j:
                    w = e[(0, r)[l == 0] : (l, le)[l == 0]]
                    if w == w[::-1]:
                        if l == 0:
                            res.append([i, j])
                        else:
                            res.append([j, i])
                if r < le:
                    r += 1
                else:
                    l += 1
        return res
