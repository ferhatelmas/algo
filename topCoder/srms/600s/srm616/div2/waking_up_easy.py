class WakingUpEasy:
    def countAlarms(self, volume, S):
        v, c = list(volume), 0
        while S > 0:
            c += 1
            S -= v[0]
            v = v[1:] + [v[0]]
        return c
