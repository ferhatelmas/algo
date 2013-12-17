class FixTheAverage:
    def add(self, list, target):
        return target * (len(list)+1) - sum(list)
