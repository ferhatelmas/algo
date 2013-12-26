from operator import itemgetter

class SerialNumbers:
    def sortSerials(self, serialNumbers):
        def digit_sum(s):
            return sum(map(lambda e: int(e) if '0' <= e <= '9' else 0, s))
        ls = map(lambda n: (len(n), digit_sum(n), n), serialNumbers)
        return [e[2] for e in sorted(ls, key=itemgetter(0, 1, 2))]
