class Solution:
    def selfDividing(self, n: int) -> bool:
        s = str(n)
        return "0" not in s and all(n % int(e) == 0 for e in s)

    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right + 1) if self.selfDividing(n)]
