from typing import List


class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        positives, negatives = [], []
        for e in sorted(A):
            if e > 0:
                positives.append(e)
            else:
                negatives.append(e)

        k = min(len(negatives), K)
        if k == K:
            return sum(positives) - sum(negatives[:k]) + sum(negatives[k:])

        l = K - k
        positives.extend(abs(e) for e in negatives)
        s = sum(positives)
        if l % 2 == 1:
            positives.sort()
            s -= 2 * positives[0]
        return s
