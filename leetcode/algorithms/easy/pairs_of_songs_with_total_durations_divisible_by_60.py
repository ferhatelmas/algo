from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mods = [0] * 60
        for t in time:
            mods[t % 60] += 1

        cnt = sum(mods[i] * mods[60 - i] for i in range(1, 30))
        for i in [0, 30]:
            cnt += mods[i] * (mods[i] - 1) // 2
        return cnt
