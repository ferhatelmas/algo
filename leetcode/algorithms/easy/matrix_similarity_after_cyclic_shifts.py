from typing import List


class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        omat, k = [], k % len(mat[0])
        for i, r in enumerate(mat):
            if i % 2 == 0:
                omat.append(r[-k:] + r[:-k])
            else:
                omat.append(r[k:] + r[:k])
        return omat == mat
