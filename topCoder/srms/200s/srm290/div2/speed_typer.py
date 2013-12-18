class SpeedTyper:
    def lettersToPractice(self, letters, times):
        avg, c, s = times[-1] / len(letters), 0, ''
        for l, t in zip(letters, times):
            if t-c > avg:
                s += l
            c = t
        return s
