class OneDimensionalRobotEasy:
    def finalPosition(self, commands, A, B):
        x = 0
        for c in commands:
            if c == "R":
                if x < B:
                    x += 1
            elif c == "L":
                if x > -A:
                    x -= 1
        return x
