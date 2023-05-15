from typing import List


class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        game, i, j = [False] * n, 0, 0
        while True:
            i = (i + j * k) % n
            if game[i]:
                break
            game[i] = True
            j += 1
        return [i + 1 for i, b in enumerate(game) if not b]
