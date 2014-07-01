class MicroStrings:
    def makeMicroString(self, A, D):
        return ''.join(str(i) for i in xrange(A, -1, -D))
