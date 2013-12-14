class IsingModel:
    def energy(self, spins):
        li, lj, c = len(spins), len(spins[0]), 0
        for i in xrange(li):
            for j in xrange(lj):
                if j < lj-1:
                    if spins[i][j] == spins[i][j+1]:
                        c -= 1
                    else:
                        c += 1

                if i < li-1:
                    if spins[i][j] == spins[i+1][j]:
                        c -= 1
                    else:
                        c += 1
        return c
