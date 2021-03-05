class DifferentStrings:
    def minimize(self, A, B):
        def diff(s):
            return sum(map(lambda (a, b): a != b, zip(A, s)))

        la = len(A)
        return min(diff(B[i : i + la]) for i in xrange(len(B) - la + 1))
