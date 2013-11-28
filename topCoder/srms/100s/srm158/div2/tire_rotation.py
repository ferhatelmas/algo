class TireRotation:
    def getCycle(self, initial, current):
        r = [initial, initial[2:][::-1] + initial[:2],
             initial[:2][::-1] + initial[2:][::-1], initial[2:] + initial[:2][::-1]]
        if current in r:
            return r.index(current) + 1
        return -1
