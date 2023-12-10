from typing import List


class Solution:
    def countTestedDevices(self, batteryPercentages: List[int]) -> int:
        cnt, l = 0, len(batteryPercentages)
        for i, e in enumerate(batteryPercentages):
            if e > 0:
                cnt += 1
                for j in range(i + 1, l):
                    batteryPercentages[j] = max(0, batteryPercentages[j] - 1)
        return cnt
