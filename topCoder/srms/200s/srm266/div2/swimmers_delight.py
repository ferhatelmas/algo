class SwimmersDelight:
    def longestJump(self, x, y):
        m = 10
        for i in range(2):
            for j in range(2):
                m = min(
                    m,
                    max(
                        x[i],
                        round(((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2) ** 0.5),
                        10 - x[j],
                    ),
                )
        return m
