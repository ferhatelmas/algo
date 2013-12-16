class SandwichBar:
    def whichOrder(self, available, orders):
        for i, o in enumerate(orders):
            if all(map(lambda e: e in available, o.split())):
                return i
        return -1
