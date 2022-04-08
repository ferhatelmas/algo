def dist(x1, y1, x2, y2):
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


for _ in range(int(input())):
    r = int(input())
    a, b = map(int, input().split())
    c, d = map(int, input().split())
    e, f = map(int, input().split())

    l = [dist(a, b, c, d), dist(a, b, e, f), dist(c, d, e, f)]
    if sorted(l)[1] <= r:
        print("yes")
    else:
        print("no")
