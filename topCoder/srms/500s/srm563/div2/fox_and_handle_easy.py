class FoxAndHandleEasy:
    def isPossible(self, S, T):
        ls, lt = len(S), len(T)
        for i in xrange(lt):
            if T[i:i+ls] == T[:i] + T[i+ls:] == S:
                return 'Yes'
        return 'No'
