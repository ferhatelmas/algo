class Solution:
    def combinationSum2(self, candidates, target):
        return self.combination(sorted(candidates), target, 0, [], [])

    def combination(self, cands, t, n, comb, res):
        for i, e in enumerate(cands[n:], start=n):
            if i > n and e == cands[i - 1]:
                continue
            if e == t:
                res.append(comb + [e])
            elif e < t:
                self.combination(cands, t - cands[i], i + 1, comb + [e], res)
            else:
                break
        return res
