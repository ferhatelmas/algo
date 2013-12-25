class MnemonicMemory:
    def getPhrase(self, number, dictionary):
        d = {}
        for e in dictionary:
            l = len(e)
            d[l] = d.get(l, []) + [e]
        d = dict((k, sorted(v, reverse=True)) for k, v in d.items())
        return ' '.join([d[int(e)].pop() for e in number])
