from collections import Counter


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        c = Counter(T)
        return "".join(e * c[e] for e in S if e in c) + "".join(
            e for e in T if e not in S
        )
