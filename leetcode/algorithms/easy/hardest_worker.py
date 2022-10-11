from typing import List


class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        worker, longest, current = n + 1, 0, 0
        for log in logs:
            t = log[1] - current
            if t > longest:
                longest, worker = t, log[0]
            elif t == longest:
                worker = min(worker, log[0])
            current = log[1]
        return worker
