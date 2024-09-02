class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        def pad(num: int) -> str:
            return str(num).zfill(4)

        ls = [num1, num2, num3]
        return int("".join(min(ks) for ks in zip(*map(pad, ls))))
