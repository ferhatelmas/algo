class DeerInZooDivTwo:
    def getminmax(self, N, K):
        return max(N - K, 0), N - (K / 2 + K % 2)
