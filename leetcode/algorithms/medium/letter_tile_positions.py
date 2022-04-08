from itertools import chain, permutations


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        return len(
            {
                a
                for a in chain(
                    *(permutations(tiles, i) for i in range(1, len(tiles) + 1))
                )
            }
        )
