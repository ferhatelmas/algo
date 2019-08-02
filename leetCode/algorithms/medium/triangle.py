class Solution:
    def minimumTotal(self, triangle):
        for j, (a, b) in enumerate(zip(triangle, triangle[1:])):
            b[0] += a[0]
            for i in xrange(1, len(a)):
                b[i] += min(a[i - 1 : i + 1])
            b[-1] += a[-1]
        return min(triangle[-1])
