from operator import itemgetter

class PaperRockScisQuals:
    def whoPassed(self, players):
        def play(a, b):
            c = 0
            for x, y in zip(a, b):
                if x == 'P':
                    if y == 'R':
                        c += 1
                    elif y == 'S':
                        c -= 1
                elif x == 'R':
                    if y == 'S':
                        c += 1
                    elif y == 'P':
                        c -= 1
                else:
                    if y == 'P':
                        c += 1
                    elif y == 'R':
                        c -= 1
            if c > 0:
                return 1
            elif c == 0:
                return 0.5
            return 0
        s = []
        for i, a in enumerate(players):
            c = 0
            for j, b in enumerate(players):
                if i != j:
                    print i, j, a, b, play(a, b)
                    c += play(a, b)
            s.append((i, -c))
        return sorted(s, key=itemgetter(1, 0))[0][0]
