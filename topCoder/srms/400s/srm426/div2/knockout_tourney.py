class KnockoutTourney:
    def meetRival(self, N, you, rival):
        if min(you, rival) % 2 == 1 and abs(you - rival) == 1:
            return 1
        return 1 + self.meetRival(N, you - you / 2, rival - rival / 2)
