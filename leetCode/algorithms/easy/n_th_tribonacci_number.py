class Solution:
    def tribonacci(self, n: int) -> int:
        fib = [0, 1, 1]
        for i in range(3, n + 1):
            fib.append(fib[i - 1] + fib[i - 2] + fib[i - 3])
        return fib[n]
