from sys import stdin


def bet(p):
    if p > 0.5:
        return 10000 + 10000 * (2 * p - 1) * (1 - p)
    return 10000 + 10000 * (1 - 2 * p) * p


print("\n".join(str(bet(float(ln))) for i, ln in enumerate(stdin) if i))
