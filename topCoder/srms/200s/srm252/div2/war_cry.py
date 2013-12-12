class WarCry:
    def alertTime(self, outposts):
        a, c, m = False, 0, 0
        for e in outposts:
            if e == '-':
                c += 1
            else:
                m = max(m, c/2 + c%2 if a else c)
                c = 0
                a = True
        return max(m, c)
