class PenguinTiles:
    def minMoves(self, tiles):
        rc, cc = len(tiles), len(tiles[0])
        for i, r in enumerate(tiles):
            for j, c in enumerate(r):
                if c == ".":
                    return (rc - 1 != i) + (cc - 1 != j)
        return 0
