class ThreeCardMonte:
    def position(self, swaps):
        c = 1
        for e in swaps:
            if e == "L":
                if c <= 1:
                    c = 1 - c
            elif e == "R":
                if c >= 1:
                    c = 3 - c
            elif e == "E":
                if c == 0 or c == 2:
                    c = 2 - c
        return "LMR"[c]
