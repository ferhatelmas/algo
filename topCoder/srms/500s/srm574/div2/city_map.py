from collections import defaultdict

class CityMap:
    def getLegend(self, cityMap, POIs):
        d = defaultdict(int)
        for r in cityMap:
            for c in r:
                if c != '.':
                    d[c] += 1
        dd = dict((v, k) for k, v in d.items())
        return ''.join(dd[p] for p in POIs)
