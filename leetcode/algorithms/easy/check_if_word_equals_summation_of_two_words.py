class Solution:
    k = {chr(97 + i): str(i) for i in range(0, 10)}

    def value(self, w: str) -> int:
        return int("".join(Solution.k[e] for e in w))

    def isSumEqual(self, first: str, second: str, target: str) -> bool:
        return self.value(first) + self.value(second) == self.value(target)
