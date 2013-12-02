class Multiples:
    def number(self, min, max, factor):
        return len(filter(lambda i: i%factor == 0, xrange(min, max+1)))
