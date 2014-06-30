class KeyDungeonDiv2:
    def countDoors(self, doorR, doorG, keys):
        return sum(max(r - keys[0], 0) + max(g - keys[1], 0) <= keys[2]
                   for r, g in zip(doorR, doorG))
