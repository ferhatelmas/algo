from collections import Counter


class P8XMatrixTransformation:
    def solve(self, original, target):
        def c(m):
            c = Counter()
            for r in m:
                c += Counter(r)
            return c

        return ("NO", "YES")[c(original) == c(target)]
