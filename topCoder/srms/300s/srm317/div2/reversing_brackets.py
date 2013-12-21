class ReversingBrackets:
    def removeBrackets(self, s):
        if '[' in s:
            a, b = s.index('['), s.index(']')
            return s[:a] + s[a+1:b][::-1] + s[b+1:]
        return s
