class ClockWalk:
    def finalPosition(self, flips):
        s = 12
        for i, f in enumerate(flips, 1):
            if f == "h":
                s += i
            else:
                s -= i
            s %= 12
        return 12 if s == 0 else s
