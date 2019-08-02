class Solution:
    def isScramble(self, s1, s2):
        l1, l2 = len(s1), len(s2)
        if l1 != l2:
            return False
        dp = [[[False] * (l1 + 1) for _ in range(l1)] for _ in range(l1)]
        for l in range(1, l1 + 1):
            for i in range(l1 - l + 1):
                for j in range(l1 - l + 1):
                    if l == 1:
                        dp[i][j][l] = s1[i] == s2[j]
                    else:
                        k = 1
                        while k < l and not dp[i][j][l]:
                            dp[i][j][l] = (dp[i][j][k] and dp[i + k][j + k][l - k]) or (
                                dp[i][j + l - k][k] and dp[i + k][j][l - k]
                            )
                            k += 1
        return dp[0][0][l1]
