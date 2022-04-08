from collections import Counter


class Solution:
    def countBalls(self, lowLimit: int, highLimit: int) -> int:
        c = Counter(sum(int(j) for j in str(i)) for i in range(lowLimit, highLimit + 1))
        print(c)
        return c.most_common(1)[0][1]
