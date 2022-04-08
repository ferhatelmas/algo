class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        a = [0, 1]
        for i in range(2, N + 1):
            a.append(a[i - 2] + a[i - 1])
        return a[N]
