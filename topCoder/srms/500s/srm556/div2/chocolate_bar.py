class ChocolateBar:
    def maxLength(self, letters):
        l = len(letters)
        return max(
            j-i if j-i == len(set(letters[i:j])) else 1
            for i in xrange(l)
            for j in xrange(i+1, l+1)
        )
