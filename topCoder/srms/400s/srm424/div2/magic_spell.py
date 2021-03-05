class MagicSpell:
    def fixTheSpell(self, spell):
        s, i, r = [e for e in spell if e in "AZ"], -1, ""
        for e in spell:
            if e in "AZ":
                r += s[i]
                i -= 1
            else:
                r += e
        return r
