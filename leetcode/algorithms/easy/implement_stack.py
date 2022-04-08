class Stack:
    def __init__(self):
        self.l = []

    def push(self, x):
        self.l.append(x)

    def pop(self):
        self.l.pop()

    def top(self):
        return self.l[-1]

    def empty(self):
        return len(self.l) == 0
