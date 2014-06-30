class MiniatureDachshund:
    def maxMikan(self, mikan, weight):
        ls, l, i = sorted(mikan), len(mikan), 0
        while i < l and ls[i] + weight <= 5000:
            weight += ls[i]
            i += 1
        return i
