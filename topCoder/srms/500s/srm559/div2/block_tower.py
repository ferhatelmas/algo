class BlockTower:
    def getTallest(self, blockHeights):
        m = 0
        for i in xrange(len(blockHeights) + 1):
            m = max(
                m,
                sum(e for e in blockHeights[:i] if e % 2 == 0)
                + sum(e for e in blockHeights[i:] if e % 2),
            )
        return m
