class TeamsSelection:
    def simulate(self, preference1, preference2):
        i, j, c, n = 0, 0, 0, len(preference1)
        s, r = set(i for i in xrange(1, n+1)), ['1'] * n
        while c < n:
            if c%2 == 0:
                while preference1[i] not in s:
                    i += 1
                r[preference1[i]-1] = '1'
                s.remove(preference1[i])
            else:
                while preference2[j] not in s:
                    j += 1
                r[preference2[j]-1] = '2'
                s.remove(preference2[j])
            c += 1
        return ''.join(r)
