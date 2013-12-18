class PackingParts:
    def pack(self, partSizes, boxSizes):
        r, boxSizes = 0, list(boxSizes)
        for p in partSizes:
            c = -1
            for i, b in enumerate(boxSizes):
                if b >= p:
                    c = i
                    break
            if c == -1:
                return r
            else:
                r += 1
                del boxSizes[c]
        return r
