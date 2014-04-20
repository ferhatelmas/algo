class TheProgrammingContestDivTwo:
    def find(self, T, requiredTime):
        s, t, p = 0, 0, 0
        for i in sorted(requiredTime):
            if T >= p + i:
                s += 1
                p += i
                t += p
            else:
                break
        return s, t
