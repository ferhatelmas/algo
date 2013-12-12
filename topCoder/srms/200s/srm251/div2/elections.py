from operator import itemgetter

class Elections:
    def visit(self, likelihoods):
        return min(map(lambda (i, n): (i, n.count('1')/float(len(n))), enumerate(likelihoods)),
                   key=itemgetter(1))[0]
