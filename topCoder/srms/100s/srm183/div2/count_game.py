class CountGame:
    def howMany(self, maxAdd, goal, next):
        r = (goal - next + 1) % (maxAdd + 1)
        return r if r else -1
