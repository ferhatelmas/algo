class Aquarium:
    def peaceful(self, minSize, maxSize, fishSizes):
        def is_fine(n):
            for i in fishSizes:
                if (2 * i <= n <= 10 * i) or (2 * n <= i <= 10 * n):
                    return
            return n

        return len(filter(None, map(is_fine, xrange(minSize, maxSize + 1))))
