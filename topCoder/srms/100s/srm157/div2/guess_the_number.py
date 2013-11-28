class GuessTheNumber:
    def noGuesses(self, upper, answer):
        lower, c = 1, 0
        while True:
            x = (lower + upper) / 2
            c += 1
            if x == answer:
                break
            elif x > answer:
                upper = x-1
            else:
                lower = x+1
        return c
