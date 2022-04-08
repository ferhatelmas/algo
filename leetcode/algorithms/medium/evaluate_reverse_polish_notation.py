class Solution:
    def evalRPN(self, tokens):
        s = []
        for token in tokens:
            if token in "+-/*":
                i, j = s.pop(), s.pop()
                if token == "+":
                    res = j + i
                elif token == "-":
                    res = j - i
                elif token == "*":
                    res = j * i
                elif token == "/":
                    if min(i, j) <= 0 < max(i, j):
                        res = -(-j / i)
                    else:
                        res = j / i
                s.append(res)
            else:
                s.append(int(token))
        return s.pop()
