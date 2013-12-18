import re

class IndicatorMotion:
    def getMotion(self, program, startState):
        s = startState
        for a, i in re.findall('(\w)(\d+)', program):
            for _ in xrange(int(i)):
                if a == 'L':
                    startState = {'|': '\\', '\\': '-', '-': '/', '/': '|'}[startState]
                elif a == 'R':
                    startState = {'\\': '|', '|': '/', '/': '-', '-': '\\'}[startState]
                elif a == 'F':
                    startState = {'\\': '/', '/': '\\', '-': '|', '|': '-'}[startState]
                s += startState
        return s
