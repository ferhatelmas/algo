class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        s = 0
        while mainTank >= 5:
            mainTank -= 5
            s += 50
            if additionalTank > 0:
                mainTank += 1
                additionalTank -= 1
        if mainTank > 0:
            s += 10 * mainTank
        return s
