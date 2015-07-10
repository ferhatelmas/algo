class Queue:
    def __init__(self):
        self.ls = []

    def push(self, x):
        self.ls.append(x)

    def pop(self):
        self.ls = self.ls[1:]

    def peek(self):
        return self.ls[0]

    def empty(self):
        return len(self.ls) == 0
