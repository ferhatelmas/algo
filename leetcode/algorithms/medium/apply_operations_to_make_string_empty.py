from operator import itemgetter


class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        last, counts, m = {}, {}, 0
        for i, e in enumerate(s):
            last[e] = i
            counts[e] = counts.get(e, 0) + 1
            m = max(m, counts[e])
        last = {a: b for a, b in last.items() if counts[a] == m}
        return "".join(a for a, _ in sorted(last.items(), key=itemgetter(1)))
