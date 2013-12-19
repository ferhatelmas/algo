class NounReform:
    def makePlural(self, nouns):
        def make(s):
            if s[-2:] in ['ch', 'sh'] or s[-1] in ['s', 'z', 'x']:
                return s + 'es'
            elif s[-2:] in ['ay', 'ey', 'iy', 'oy', 'uy']:
                return s + 's'
            elif s.endswith('y'):
                return s[:-1] + 'ies'
            return s + 's'
        return map(make, nouns)
