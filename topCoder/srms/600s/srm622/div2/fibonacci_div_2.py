class FibonacciDiv2:
    def find(self, N):
        i, j = 0, 1
        while N >= j:
            i, j = j, i + j
        return min(j - N, N - i)
