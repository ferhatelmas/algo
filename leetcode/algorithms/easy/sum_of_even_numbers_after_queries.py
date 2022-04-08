from typing import List


class Solution:
    def sumEvenAfterQueries(self, A: List[int], queries: List[List[int]]) -> List[int]:
        res, s = [], sum(e for e in A if e % 2 == 0)
        for (val, i) in queries:
            prev, A[i] = A[i], A[i] + val
            if prev % 2 == 0:
                if A[i] % 2 == 0:
                    s += val
                else:
                    s -= prev
            elif A[i] % 2 == 0:
                s += A[i]
            res.append(s)
        return res
