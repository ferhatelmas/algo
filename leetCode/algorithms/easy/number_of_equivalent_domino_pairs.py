from typing import List


class Solution:
    def nom(self, a):
        return tuple(sorted(a))

    def numEquivDominoPairs(self, dominoes: List[List[int]]) -> int:
        s, cnt = {}, 0
        for d in dominoes:
            d = self.nom(d)
            if d in s:
                cnt, s[d] = cnt + s[d], s[d] + 1
            else:
                s[d] = 1
        return cnt
