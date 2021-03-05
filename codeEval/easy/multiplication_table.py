import sys

for i in xrange(1, 13):
    print " ".join(
        map(
            lambda x: "   "[: (3 - len(x))] + x, map(lambda x: str(x * i), range(1, 13))
        )
    )
