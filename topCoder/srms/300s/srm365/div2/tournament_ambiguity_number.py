class TournamentsAmbiguityNumber:
    def scrutinizeTable(self, table):
        c = 0
        for k, t in enumerate(table):
            for i, e in enumerate(t):
                if e == '1':
                    for j, f in enumerate(table[i]):
                        if f == '1' and table[j][k] == '1':
                            c += 1
        return c
