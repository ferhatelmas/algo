class DengklekTryingToSleep:
    def minDucks(self, ducks):
        A, B = min(ducks), max(ducks)
        return B-A+1 - len(ducks)
