class FoxAndFlowerShopDivTwo:
    def theMaxFlowers(self, flowers, r, c):
        def calc(i, j, k, l):
            return sum(f == "F" for e in flowers[i:j] for f in e[k:l])

        rc, cc = len(flowers), len(flowers[0])
        return max(
            calc(0, r, 0, cc),
            calc(r + 1, rc, 0, cc),
            calc(0, rc, 0, c),
            calc(0, rc, c + 1, cc),
        )
