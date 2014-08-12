class Solution:
    # @param n, an integer
    # @return an integer
    cache = {}

    def climbStairs(self, n):
        if n <= 2:
            return n
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = self.climbStairs(n-1)
        if n > 1:
            self.cache[n] += self.climbStairs(n-2)
        return self.cache[n]
