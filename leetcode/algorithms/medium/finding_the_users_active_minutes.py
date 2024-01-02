from typing import List


class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        d = {}
        for n, t in logs:
            if n not in d:
                d[n] = set()
            d[n].add(t)
        res = [0] * k
        for v in d.values():
            res[len(v) - 1] += 1
        return res
