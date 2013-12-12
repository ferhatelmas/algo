class TriangleType:
    def type(self, a, b, c):
        s = sorted([a, b, c])
        if s[2] >= s[0] + s[1]:
            return 'IMPOSSIBLE'

        c = cmp(s[0]**2 + s[1]**2, s[2]**2)
        if c == 0:
            return 'RIGHT'
        elif c > 0:
            return 'ACUTE'
        return 'OBTUSE'
