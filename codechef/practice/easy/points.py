for _ in range(int(input())):
    input()
    n = int(input())
    points = []
    for _ in range(n):
        (x, y) = map(int, input().split())
        points.append((x, y))
    points = sorted(
        points, cmp=lambda p1, p2: p1[0] - p2[0] if p1[0] != p2[0] else p2[1] - p1[1]
    )

    path, x, y = 0, points[0][0], points[0][1]
    for x1, y1 in points:
        path += ((x1 - x) ** 2 + (y1 - y) ** 2) ** 0.5
        x, y = x1, y1

    print("%.2f" % path)
