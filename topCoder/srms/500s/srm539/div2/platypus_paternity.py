class PlatypusPaternity:
    def maxFamily(self, femaleCompatibility, maleCompatibility, siblingGroups):
        c = 0
        for s in siblingGroups:
            for f in femaleCompatibility:
                for m in maleCompatibility:
                    ok, curr = True, 0
                    for i, e in enumerate(s):
                        if e == "Y":
                            curr += 1
                            ok = ok and f[i] == m[i] == "Y"
                    if ok:
                        c = max(c, curr + 2)
        return c
