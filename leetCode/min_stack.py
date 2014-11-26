class MinStack:

    def __init__(self):
        self.data = []
        self.datamin = []

    def push(self, x):
        self.data.append(x)
        if not self.datamin or x <= self.datamin[-1]:
            self.datamin.append(x)

    def pop(self):
        r = self.data.pop()
        if self.datamin and self.datamin[-1] == r:
            self.datamin.pop()

    def top(self):
        return self.data[-1]

    def getMin(self):
        return self.datamin[-1]
