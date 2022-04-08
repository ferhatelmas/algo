class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        while n > 0:
            n, x = divmod(n, 3)
            if x == 2:
                return False
        return True
