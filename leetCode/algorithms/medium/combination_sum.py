class Solution:

    def combinationSum(self, candidates, target):
        res, s = [], sorted(candidates)

        def rec(ls, i, t):
            if t == 0:
                res.append(ls)
            else:
                for j, e in enumerate(s[i:], start=i):
                    if t - e >= 0:
                        rec([l for l in ls] + [e], j, t - e)
        rec([], 0, target)
        return res
