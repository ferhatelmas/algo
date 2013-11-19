class Justifier:
    def justify(self, textIn):
        width = max(map(len, textIn))
        return map(lambda s: s.rjust(width), textIn)
