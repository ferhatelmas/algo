class StringCompare:
    def simpleDifference(self, a, b):
        return len(filter(lambda (i, j): i == j, zip(a, b)))
