class LevelUp:
    def toNextLevel(self, expNeeded, received):
        for e in expNeeded:
            if received < e:
                return e - received
        return 0
