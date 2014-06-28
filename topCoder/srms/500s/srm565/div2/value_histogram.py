from collections import Counter

class ValueHistogram:
    def build(self, values):
        c = Counter(values)
        h = max(c.values()) + 1
        return [
            ''.join(e)
            for e in zip(*[(c[i]*'X') + (h-c[i])*'.' for i in xrange(10)])
        ][::-1]
