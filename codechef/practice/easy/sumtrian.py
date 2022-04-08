for _ in range(int(raw_input())):
    n = int(raw_input())
    p = []
    for _ in range(n):
        p = map(
            lambda x, y: x + y,
            map(lambda x, y: x if x >= y else y, [0] + p, p + [0]),
            [int(x) for x in raw_input().split()],
        )
    print max(p)
