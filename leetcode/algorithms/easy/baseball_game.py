from typing import List


class Solution:
    def calPoints(self, ops: List[str]) -> int:
        rounds = []
        for op in ops:
            if op == "+":
                rounds.append(rounds[-1] + rounds[-2])
            elif op == "D":
                rounds.append(2 * rounds[-1])
            elif op == "C":
                rounds.pop()
            else:
                rounds.append(int(op))
        return sum(rounds)
