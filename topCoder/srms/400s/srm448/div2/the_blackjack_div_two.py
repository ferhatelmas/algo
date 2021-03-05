class TheBlackJackDivTwo:
    def score(self, cards):
        def cal(card):
            r, _ = card
            if r == "A":
                return 11
            elif r in "TJQK":
                return 10
            return int(r)

        return sum([cal(c) for c in cards])
