class PeopleCircle:
    def order(self, numMales, numFemales, K):
        t = numMales + numFemales
        ls, i = ['M'] * t, t-1
        for _ in range(numFemales):
            c = 0
            while c < K:
                i = (i + 1) % t
                if ls[i] == 'M':
                    c += 1
            ls[i] = 'F'
        return ''.join(ls)
