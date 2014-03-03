class MicrowaveSelling:
    def mostAttractivePrice(self, minPrice, maxPrice):
        def tr(n):
            for i, e in enumerate(str(n)[::-1]):
                if e != '9':
                    return i
            return len(str(n))
        return max(xrange(maxPrice, minPrice-1, -1), key=tr)
