class ContiguousCacheEasy:
    def bytesRead(self, n, k, addresses):
        s, a, b = 0, 0, k - 1
        for i in addresses:
            if i < a:
                s += min(a - i, k)
                a, b = i, i + k - 1
            elif i > b:
                s += min(i - b, k)
                a, b = i - k + 1, i
        return s
