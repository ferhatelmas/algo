class SortMachine:
    def countMoves(self, a):
        b, i = sorted(a), 0
        for e in a:
            if e == b[i]:
                i += 1
        return len(a) - i
