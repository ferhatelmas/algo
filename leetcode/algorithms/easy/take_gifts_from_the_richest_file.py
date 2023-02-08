from typing import List


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        while k > 0:
            gifts.sort()
            m = gifts.pop()
            gifts.append(int(m**0.5))
            k -= 1
        return sum(gifts)
