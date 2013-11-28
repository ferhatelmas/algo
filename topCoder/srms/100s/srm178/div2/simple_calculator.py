import re

class SimpleCalculator:
    def calculate(self, input):
        a, o, b = re.match('(\d+)(\D)(\d+)', input).groups()
        a, b = int(a.lstrip('0')), int(b.lstrip('0'))
        if o == '+':
            return a + b
        elif o == '-':
            return a - b
        elif o == '*':
            return a * b
        return a / b
