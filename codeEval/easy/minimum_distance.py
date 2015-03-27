from sys import argv


def min_distance(ls):
    return min(
        sum(abs(i-j) for j in ls)
        for i in xrange(min(ls), max(ls)+1)
    )


with open(argv[1], 'rb') as test_cases:
    for test in test_cases:
        print(min_distance(map(int, test.split())[1:]))
