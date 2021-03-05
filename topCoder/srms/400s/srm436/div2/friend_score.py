from collections import defaultdict


class FriendScore:
    def highestScore(self, friends):
        d = defaultdict(set)
        for i, f in enumerate(friends):
            for j, e in enumerate(f):
                if e == "Y":
                    d[i].add(j)
                    for k, g in enumerate(friends[j]):
                        if g == "Y":
                            d[i].add(k)
        return max(map(len, d.values())) - 1 if d else 0
