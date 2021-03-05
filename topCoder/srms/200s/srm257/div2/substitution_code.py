class SubstitutionCode:
    def getValue(self, key, code):
        r = ""
        for e in code:
            if e in key:
                r += str((key.index(e) + 1) % 10)
        return r
