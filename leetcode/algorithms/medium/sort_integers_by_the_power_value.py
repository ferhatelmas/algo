class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        d = dict()

        def power(n: int):
            cnt, initial = 0, n
            while n > 1:
                if n in d:
                    d[initial] = cnt + d[n]
                    return d[initial]
                if n % 2:
                    n = 3 * n + 1
                else:
                    n /= 2
                cnt += 1
            d[initial] = cnt
            return cnt

        return sorted((power(e), e) for e in range(lo, hi + 1))[k - 1][1]
