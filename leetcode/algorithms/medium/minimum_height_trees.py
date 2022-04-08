import collections


class Solution:
    def findMinHeightTrees(self, n, edges):
        g = collections.defaultdict(set)
        for a, b in edges:
            g[a].add(b)
            g[b].add(a)
        deg = {k: len(g[k]) if k in g else 0 for k in range(n)}
        k = n
        while k > 2:
            d = [i for i in range(n) if deg[i] == 1]
            k -= len(d)
            for i in d:
                v = g[i].pop()
                deg[i], deg[v] = -1, deg[v] - 1
                g[v].remove(i)
        return [k for k, v in deg.items() if v != -1]
