from operator import itemgetter

class TheBestName:
    def sort(self, names):
        ls = map(lambda e: (e, -sum(map(lambda j: ord(j)-ord('A')+1, e))), names)
        ls = [n for n, k in sorted(ls, key=itemgetter(1, 0))]
        r = []
        for e in ls:
            if e == 'JOHN':
                r.insert(0, e)
            else:
                r.append(e)
        return r
