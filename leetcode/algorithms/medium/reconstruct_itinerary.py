import collections


class Solution:
    def findItinerary(self, tickets):
        if not tickets:
            return []
        g = collections.defaultdict(list)
        for a, b in tickets:
            g[a].append(b)
        for k in g.keys():
            g[k].sort()
        it, dfs = [], ["JFK"]
        while dfs:
            t = dfs[-1]
            if not g[t]:
                it.append(t)
                dfs.pop()
            else:
                dfs.append(g[t].pop(0))
        return it[::-1]
