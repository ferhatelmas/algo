class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        res, r = [], 0
        for a in A:
            r = (r * 2 + a) % 5
            res.append(r == 0)
        return res
