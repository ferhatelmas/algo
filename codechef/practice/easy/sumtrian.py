for _ in range(int(input())):
    n = int(input())
    p = []
    for _ in range(n):
        p = map(
            lambda x, y: x + y,
            map(lambda x, y: x if x >= y else y, [0] + p, p + [0]),
            [int(x) for x in input().split()],
        )
    print(max(p))
