class LeftOrRight:
    def maxDistance(self, program):
        m = 0
        for i in range(2):
            c = 0
            for e in program:
                if e == 'L':
                    c -= 1
                elif e == 'R':
                    c += 1
                else:
                    c += -1 if i%2 else 1
                m = max(m, abs(c))
        return m
