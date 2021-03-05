class FoxAndClassroom:
    def ableTo(self, n, m):
        s, i, j = set(), 0, 0
        while (i, j) not in s:
            s.add((i, j))
            i, j = (i + 1) % n, (j + 1) % m
        return "Possible" if len(s) == n * m else "Impossible"
