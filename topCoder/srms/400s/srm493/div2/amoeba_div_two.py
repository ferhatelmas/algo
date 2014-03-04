from itertools import groupby

class AmoebaDivTwo:
    def count(self, table, K):
        def count(r):
            return sum(max(len(list(g))-K+1, 0)
                       for k, g in groupby(r) if k == 'A')
        return sum(count(r) for r in table) + \
               (sum(count(r) for r in zip(*table)) if K > 1 else 0)
