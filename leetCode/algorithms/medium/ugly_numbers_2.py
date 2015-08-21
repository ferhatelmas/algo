class Solution:
    def nthUglyNumber(self, n):
        if n < 1:
            return 0
        j = [[0, 2], [0, 3], [0, 5]]
        ls = [1]
        for i in range(1, n):
            ls.append(min(ls[a] * b for a, b in j))
            for k, (a, b) in enumerate(j):
                if ls[a] * b == ls[i]:
                    j[k][0] += 1
        return ls[n - 1]
