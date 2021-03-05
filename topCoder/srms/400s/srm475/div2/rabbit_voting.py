class RabbitVoting:
    def getWinner(self, names, votes):
        d, m = {}, 0
        for n, v in zip(names, votes):
            if n != v:
                d[v] = d.get(v, 0) + 1
                m = max(d[v], m)
        if not d:
            return ""
        r = filter(lambda (k, v): v == m, d.items())
        return "" if len(r) > 1 else r[0][0]
