from itertools import chain, combinations


class Solution:
    def subsetsWithDup(self, S):
        return [
            list(t) for t in sorted(
                set(
                    tuple(sorted(e)) for e in chain(
                        *[combinations(S, i) for i in range(len(S) + 1)])))
        ]
