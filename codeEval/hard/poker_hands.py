import sys

rankings = {
    (5,): 10,
    (4, 1): 7,
    (3, 2): 6,
    (3, 1, 1): 3,
    (2, 2, 1): 2,
    (2, 1, 1, 1): 1,
    (1, 1, 1, 1, 1): 0,
}


def count(ls):
    return sorted(((ls.count(e), e) for e in set(ls)), reverse=True)


def score(hand):
    counts, ranks = zip(*count(["0123456789TJQKA".index(e) for e, _ in hand]))
    if ranks == (14, 5, 4, 3, 2):
        ranks = (5, 4, 3, 2, 1)
    straight = len(ranks) == 5 and max(ranks) - min(ranks) == 4
    flush = len(set([e for _, e in hand])) == 1
    return max(rankings[counts], 4 * straight + 5 * flush), ranks


def compare(*args):
    return ["none", "left", "right"][cmp(*map(score, args))]


with open(sys.argv[1], "r") as test_cases:
    for test in test_cases:
        ls = test.strip().split()
        print compare(ls[:5], ls[5:])
