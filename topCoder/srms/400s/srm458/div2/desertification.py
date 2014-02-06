class Desertification:
    def desertArea(self, island, T):
        def it():
            for i, r in enumerate(island):
                for j, c in enumerate(r):
                    yield (i, j, c)
        d = [(i, j) for i, j, v in it() if v == 'D']
        if d:
            return len(d) + sum((v == 'F' and
                                 min([abs(r-i) + abs(c-j) for r, c in d]) <= T
                                 for i, j, v in it()))
        return 0
