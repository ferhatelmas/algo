class ThrowTheBall:
    def timesThrown(self, N, M, L):
        i, ls, c = 0, [0]*N, 0
        while True:
            ls[i] += 1
            if ls[i] == M:
                break
            c += 1
            if ls[i]%2:
                i = (i-L)%N
            else:
                i = (i+L)%N
        return c
