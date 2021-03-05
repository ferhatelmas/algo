from collections import defaultdict


class InterestingParty:
    def bestInvitation(self, first, second):
        d = defaultdict(int)
        for f, s in zip(first, second):
            d[f] += 1
            d[s] += 1
        return max(max(d.values()), 1)
