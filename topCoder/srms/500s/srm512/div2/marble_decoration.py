class MarbleDecoration:
    def maxLength(self, R, G, B):
        def m(a, b):
            return 2 * min(a, b) + 1 - int(a == b)

        return max(m(R, G), m(R, B), m(G, B))
