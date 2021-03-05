class MirroredClock:
    def whatTimeIsIt(self, time):
        h, m = map(int, time.split(":"))
        return "%02d:%02d" % ((12 - h - (1 if m else 0)) % 12, (60 - m) % 60)
