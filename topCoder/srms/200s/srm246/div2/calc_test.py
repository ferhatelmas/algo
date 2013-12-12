import re

class CalcTest:
    def uniform(self, numbers):
        return map(lambda n: re.sub(r'\D', '.', re.sub(r' ', '', n)), numbers)
