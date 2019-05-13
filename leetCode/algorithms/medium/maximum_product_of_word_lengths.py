import operator


class Solution:
    def maxProduct(self, words):
        m, ws = 0, sorted(
            ((set(w), len(w)) for w in words),
            key=operator.itemgetter(1),
            reverse=True)
        for i, a in enumerate(ws):
            for b in ws[i + 1:]:
                if not (a[0] & b[0]):
                    n = a[1] * b[1]
                    if n > m:
                        m = n
                    else:
                        break
        return m
