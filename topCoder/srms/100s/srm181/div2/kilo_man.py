class KiloMan:
    def hitsTaken(self, pattern, jumps):
        return sum(
            map(
                lambda (p, j): (p < 3 and j == "S") or (p > 2 and j == "J"),
                zip(pattern, jumps),
            )
        )
