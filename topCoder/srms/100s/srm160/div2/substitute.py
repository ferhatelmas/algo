class Substitute:
    def getValue(self, key, code):
        return "".join([str((key.index(c) + 1) % 10) for c in code if c in key])
