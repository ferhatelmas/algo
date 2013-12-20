class EsperantoNumbers:
    def nameThisNumber(self, x):
        o, s = ["unu", "du", "tri", "kvar", "kvin", "ses", "sep", "ok", "nau", "dek"], ''
        if x/10 >= 2:
            s += o[x/10-1]
        if x >= 10:
            s += 'dek'
        if x%10:
            if s:
                s += ' '
            s += o[x%10-1]
        return s
