from typing import List


class Solution:
    def minOperations(self, logs: List[str]) -> int:
        m = 0
        for l in logs:
            if l == "./":
                continue
            if l == "../":
                m = max(0, m - 1)
                continue
            m += 1
        return m
