class TheTournamentDivTwo:
    def find(self, points):
        n = sum(points)
        return n / 2 if n % 2 == 0 else -1
