class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        t, d = divmod(k, n - 1)
        return d if t % 2 == 0 else n - d - 1
