class RPG:
    def dieRolls(self, dice):
        def die(d):
            n, x = map(int, d.split("d"))
            return [n, n * x, n * (x + 1) / 2.0]

        return map(int, map(sum, zip(*map(die, dice))))
